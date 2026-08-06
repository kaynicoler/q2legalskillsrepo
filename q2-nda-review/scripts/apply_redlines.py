#!/usr/bin/env python3
"""
apply_redlines.py — One-shot tracked-change and comment inserter for Q2 NDA Review.

Usage:
    python apply_redlines.py <input.docx> <redlines.json> <output.docx>

redlines.json format:
{
  "author": "Q2 Legal",
  "date": "2025-01-01T00:00:00Z",
  "changes": [
    {
      "type": "replace",
      "find": "exact text to find in document",
      "delete": "text to mark as deleted (must be substring of find)",
      "insert": "replacement text",
      "comment": "Two-sentence comment. Concern sentence. Proposal sentence."
    },
    {
      "type": "insert",
      "after": "exact text after which to insert (use '' for end of doc)",
      "insert": "new clause text to insert",
      "comment": "Two-sentence comment. Concern sentence. Proposal sentence."
    },
    {
      "type": "comment_only",
      "find": "exact text to anchor the comment to",
      "comment": "Comment text for clauses that cannot be reliably redlined."
    }
  ]
}

Notes:
- "find" must match a contiguous text run in the document (after XML run-merging).
- All text matching is done on the plain-text rendering of each paragraph.
- Changes are applied in order; paragraphs are modified in-place, so earlier
  changes can affect later find targets if they share the same paragraph.
- If a "find" string is not located, the change is skipped and reported in stderr.
- Comments anchor to the specific del/ins element, not the whole paragraph.
- Run formatting (bold, italic, etc.) is preserved: only the matched runs are touched.
- Insert-after works correctly whether the anchor paragraph is in the body or a table cell.
"""

import sys
import json
import shutil
import zipfile
import re
import copy
from pathlib import Path
from datetime import datetime, timezone
from lxml import etree

# OOXML namespaces
NS = {
    'w':   'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'w14': 'http://schemas.microsoft.com/office/word/2010/wordml',
    'r':   'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
}
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

def w(tag):
    return f'{{{W}}}{tag}'


# ── Text extraction ───────────────────────────────────────────────────────────

def get_text(para):
    """Return plain text of a paragraph by joining all w:t elements."""
    parts = []
    for t in para.iter(w('t')):
        parts.append(t.text or '')
    return ''.join(parts)


def find_para_for_text(paragraphs, search_text):
    """Find the first paragraph whose plain text contains search_text."""
    for i, para in enumerate(paragraphs):
        if search_text in get_text(para):
            return i, para
    return None, None


# ── Run-level helpers ─────────────────────────────────────────────────────────

def get_runs(para):
    """Return direct w:r children of a paragraph (not inside ins/del wrappers)."""
    return [c for c in para if c.tag == w('r')]


def iter_content_children(para):
    """
    Yield (element, is_run) for all content children of a paragraph,
    skipping w:pPr.  Descends into existing w:ins / w:del wrappers so we
    can read their text, but yields the wrapper element, not its children.
    """
    for child in para:
        if child.tag == w('pPr'):
            continue
        yield child


def build_run_map(para):
    """
    Walk content children and build a flat list of (element, char_start, char_end)
    so we can locate exactly which elements cover a text range.

    Elements considered:
      - w:r          → plain run
      - w:ins > w:r  → already-tracked insertion (treat as readable text, preserve)
      - w:del > w:r  → already-tracked deletion (characters are logically absent; skip)
      - w:bookmarkStart, w:bookmarkEnd, w:commentRangeStart, etc. → zero-width, preserve
      - w:hyperlink  → treat like a run container

    Returns: (flat_runs, full_text)
      flat_runs: list of dicts with keys:
        'el'    – the element (w:r, or the w:ins/w:del wrapper)
        'text'  – plain text contribution
        'start' – char offset in full_text
        'end'   – char offset (exclusive)
        'type'  – 'run' | 'ins_wrapper' | 'del_wrapper' | 'other'
    """
    flat = []
    pos = 0

    def collect(container):
        nonlocal pos
        for child in container:
            tag = child.tag
            if tag == w('pPr'):
                continue
            elif tag == w('r'):
                text = ''.join((t.text or '') for t in child.iter(w('t')))
                flat.append({'el': child, 'text': text, 'start': pos,
                             'end': pos + len(text), 'type': 'run'})
                pos += len(text)
            elif tag == w('ins'):
                # Treat the whole w:ins wrapper as one map entry — its combined text.
                # Recording one entry per sub-run caused the wrapper to be emitted
                # once for each run it contained during the rebuild pass.
                text = ''.join(
                    (t.text or '')
                    for sub in child
                    if sub.tag == w('r')
                    for t in sub.iter(w('t'))
                )
                flat.append({'el': child, 'text': text, 'start': pos,
                             'end': pos + len(text), 'type': 'ins_wrapper'})
                pos += len(text)
            elif tag == w('del'):
                # Deleted text is not part of the visible string — skip chars but record element
                flat.append({'el': child, 'text': '', 'start': pos,
                            'end': pos, 'type': 'del_wrapper'})
            elif tag == w('hyperlink'):
                # Preserve the hyperlink wrapper as one atomic entry so the
                # relationship and clickable behaviour survive the rebuild pass.
                # Collect its combined visible text for offset accounting.
                text = ''.join(
                    (t.text or '')
                    for sub in child.iter(w('r'))
                    for t in sub.iter(w('t'))
                )
                flat.append({'el': child, 'text': text, 'start': pos,
                             'end': pos + len(text), 'type': 'hyperlink'})
                pos += len(text)
            else:
                # bookmarks, comment ranges, proofErr, etc. — zero-width, preserve
                flat.append({'el': child, 'text': '', 'start': pos,
                            'end': pos, 'type': 'other'})

    collect(para)
    full_text = ''.join(e['text'] for e in flat)
    return flat, full_text


def clone_run_with_text(source_run, new_text):
    """
    Deep-copy a w:r element and replace all w:t text with new_text.
    Preserves rPr (bold, italic, font, size, etc.).
    """
    new_run = copy.deepcopy(source_run)
    t_els = new_run.findall('.//' + w('t'))
    if not t_els:
        t_el = etree.SubElement(new_run, w('t'))
        t_el.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        t_el.text = new_text
    else:
        for i, t_el in enumerate(t_els):
            t_el.text = new_text if i == 0 else ''
            t_el.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    return new_run


def make_del_wrapper(runs_or_text, author, date, change_id):
    """
    Wrap one or more runs in a w:del element.
    runs_or_text: list of w:r elements, OR a plain string (creates bare delText run).
    """
    del_el = etree.Element(w('del'))
    del_el.set(w('id'), str(change_id))
    del_el.set(w('author'), author)
    del_el.set(w('date'), date)

    if isinstance(runs_or_text, str):
        run = etree.SubElement(del_el, w('r'))
        dt = etree.SubElement(run, w('delText'))
        dt.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        dt.text = runs_or_text
    else:
        for r in runs_or_text:
            # Convert w:t → w:delText inside each copied run
            new_r = copy.deepcopy(r)
            for t_el in new_r.findall('.//' + w('t')):
                t_el.tag = w('delText')
            del_el.append(new_r)

    return del_el


def make_ins_wrapper(runs_or_text, author, date, change_id):
    """
    Wrap one or more runs in a w:ins element.
    runs_or_text: list of w:r elements, OR a plain string (creates bare text run).
    """
    ins_el = etree.Element(w('ins'))
    ins_el.set(w('id'), str(change_id))
    ins_el.set(w('author'), author)
    ins_el.set(w('date'), date)

    if isinstance(runs_or_text, str):
        run = etree.SubElement(ins_el, w('r'))
        t = etree.SubElement(run, w('t'))
        t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
        t.text = runs_or_text
    else:
        for r in runs_or_text:
            ins_el.append(copy.deepcopy(r))

    return ins_el


def range_overlaps_atomic(flat, start, end):
    """Return atomic element type if [start, end) overlaps preserved content."""
    for entry in flat:
        if entry['type'] not in ('hyperlink', 'ins_wrapper'):
            continue
        if start < entry['end'] and end > entry['start']:
            return entry['type']
    return None


def position_inside_atomic(flat, position):
    """Return atomic element type if position falls strictly inside preserved content."""
    for entry in flat:
        if entry['type'] not in ('hyperlink', 'ins_wrapper'):
            continue
        if entry['start'] < position < entry['end']:
            return entry['type']
    return None


def atomic_label(kind):
    return 'hyperlink text' if kind == 'hyperlink' else 'an existing tracked insertion'


# ── Core replace — formatting-preserving ─────────────────────────────────────

def rebuild_para_with_replace(para, find_text, delete_text, insert_text,
                               author, date, base_id):
    """
    Replace delete_text with insert_text inside a paragraph using tracked changes,
    preserving the formatting of untouched runs.

    Strategy:
      1. Build a run map so we know which runs cover which character offsets.
      2. Locate delete_text within the find_text span.
      3. Split runs at the delete boundaries:
         - Runs before the delete zone → keep as-is
         - Runs fully inside the delete zone → wrap in w:del
         - Runs straddling a boundary → split into kept + deleted fragments,
           cloning the run's rPr for both halves
      4. Insert w:ins with the replacement text after the w:del.
         The inserted run inherits rPr from the first deleted run (if any).
      5. Runs after the delete zone → keep as-is.

    Returns (success, del_el, ins_el, reason).
    """
    flat, full_text = build_run_map(para)

    if find_text not in full_text:
        return False, None, None, "find text is not present in the paragraph"

    # Locate find_text in full_text, then locate delete_text within that span
    find_start = full_text.find(find_text)
    find_end = find_start + len(find_text)

    if delete_text:
        # Search for delete_text only within the find span
        rel = find_text.find(delete_text)
        if rel == -1:
            # delete_text not found inside find span — insert-only
            return _do_insert_within_para(para, flat, full_text, find_text,
                                          insert_text, author, date, base_id)
        del_start = find_start + rel
        del_end = del_start + len(delete_text)

        atomic = range_overlaps_atomic(flat, del_start, del_end)
        if atomic:
            return (False, None, None,
                    f"target overlaps {atomic_label(atomic)} and cannot be safely redlined")
    else:
        # Empty delete — pure insertion at find location
        return _do_insert_within_para(para, flat, full_text, find_text,
                                      insert_text, author, date, base_id)

    # Build del_el and ins_el — collect deleted runs and a reference run for
    # formatting inheritance in a single pass over the flat map.
    pPr = para.find(w('pPr'))

    del_runs = []      # runs to go into the w:del wrapper
    ref_run = None     # first deleted run — used to inherit formatting for insertion

    for entry in flat:
        el = entry['el']
        estart = entry['start']
        eend = entry['end']
        etype = entry['type']

        if etype in ('del_wrapper', 'other', 'ins_wrapper', 'hyperlink'):
            continue

        run_text = entry['text']
        if not run_text:
            continue

        fully_inside = estart >= del_start and eend <= del_end
        straddles_start = estart < del_start and eend > del_start
        straddles_end   = estart < del_end   and eend > del_end

        if fully_inside:
            if ref_run is None:
                ref_run = el
            del_runs.append(el)
        elif straddles_start:
            del_text = run_text[del_start - estart : min(eend, del_end) - estart]
            if del_text:
                if ref_run is None:
                    ref_run = el
                del_runs.append(clone_run_with_text(el, del_text))
        elif straddles_end:
            del_text = run_text[:del_end - estart]
            if del_text:
                if ref_run is None:
                    ref_run = el
                del_runs.append(clone_run_with_text(el, del_text))

    # Build del_el and ins_el, insert them at the right position
    del_el = None
    ins_el = None

    if del_runs:
        del_el = make_del_wrapper(del_runs, author, date, base_id)
    elif delete_text:
        del_el = make_del_wrapper(delete_text, author, date, base_id)

    if insert_text:
        if ref_run is not None:
            ins_run = clone_run_with_text(ref_run, insert_text)
            ins_el = make_ins_wrapper([ins_run], author, date, base_id + 1)
        else:
            ins_el = make_ins_wrapper(insert_text, author, date, base_id + 1)

    # Find insertion point: just before the first run that is >= del_start
    # We need to insert del_el + ins_el in the right place among new_children.
    # The easiest approach: find the index of the first "after" run in new_children.
    # We'll do this by rebuilding in two passes.

    # Rebuild: walk flat again, assembling final child list in order
    final_children = []
    if pPr is not None:
        final_children.append(copy.deepcopy(pPr))

    inserted = False
    for entry in flat:
        el = entry['el']
        estart = entry['start']
        eend = entry['end']
        etype = entry['type']

        if etype in ('del_wrapper', 'other'):
            final_children.append(copy.deepcopy(el))
            continue

        if etype in ('ins_wrapper', 'hyperlink'):
            final_children.append(copy.deepcopy(el))
            continue

        run_text = entry['text']
        if not run_text:
            final_children.append(copy.deepcopy(el))
            continue

        fully_before = eend <= del_start
        fully_after  = estart >= del_end
        fully_inside = estart >= del_start and eend <= del_end

        if fully_before:
            final_children.append(copy.deepcopy(el))

        elif fully_inside:
            if not inserted:
                if del_el is not None:
                    final_children.append(del_el)
                if ins_el is not None:
                    final_children.append(ins_el)
                inserted = True
            # Don't append the original run — it's absorbed into del_el

        elif fully_after:
            if not inserted:
                if del_el is not None:
                    final_children.append(del_el)
                if ins_el is not None:
                    final_children.append(ins_el)
                inserted = True
            final_children.append(copy.deepcopy(el))

        else:
            # Straddling
            if estart < del_start:
                keep_len = del_start - estart
                kept_text = run_text[:keep_len]
                del_text  = run_text[keep_len:min(eend, del_end) - estart]
                after_text_part = run_text[min(eend, del_end) - estart:]

                if kept_text:
                    final_children.append(clone_run_with_text(el, kept_text))
                if not inserted:
                    if del_el is not None:
                        final_children.append(del_el)
                    if ins_el is not None:
                        final_children.append(ins_el)
                    inserted = True
                if after_text_part:
                    final_children.append(clone_run_with_text(el, after_text_part))
            else:
                keep_len = del_end - estart
                del_text_part = run_text[:keep_len]
                kept_text     = run_text[keep_len:]

                if not inserted:
                    if del_el is not None:
                        final_children.append(del_el)
                    if ins_el is not None:
                        final_children.append(ins_el)
                    inserted = True
                if kept_text:
                    final_children.append(clone_run_with_text(el, kept_text))

    if not inserted:
        if del_el is not None:
            final_children.append(del_el)
        if ins_el is not None:
            final_children.append(ins_el)

    # Replace para's children with final_children
    for child in list(para):
        para.remove(child)
    for child in final_children:
        para.append(child)

    return True, del_el, ins_el, None


def _do_insert_within_para(para, flat, full_text, after_text,
                            insert_text, author, date, base_id):
    """Insert insert_text immediately after after_text within the paragraph."""
    pos = full_text.find(after_text)
    if pos == -1:
        return False, None, None, "anchor text is not present in the paragraph"
    split_pos = pos + len(after_text)

    atomic = position_inside_atomic(flat, split_pos)
    if atomic:
        return (False, None, None,
                f"insertion point falls inside {atomic_label(atomic)} and cannot be safely edited")

    pPr = para.find(w('pPr'))
    final_children = []
    if pPr is not None:
        final_children.append(copy.deepcopy(pPr))

    inserted = False
    for entry in flat:
        el = entry['el']
        estart = entry['start']
        eend = entry['end']
        etype = entry['type']

        if etype in ('del_wrapper', 'other', 'ins_wrapper', 'hyperlink'):
            final_children.append(copy.deepcopy(el))
            continue

        run_text = entry['text']
        if not run_text:
            final_children.append(copy.deepcopy(el))
            continue

        if eend <= split_pos:
            final_children.append(copy.deepcopy(el))
            if eend == split_pos and not inserted:
                ins_el = make_ins_wrapper(insert_text, author, date, base_id)
                final_children.append(ins_el)
                inserted = True
        elif estart >= split_pos:
            if not inserted:
                ins_el = make_ins_wrapper(insert_text, author, date, base_id)
                final_children.append(ins_el)
                inserted = True
            final_children.append(copy.deepcopy(el))
        else:
            # Split point is inside this run
            kept_before = run_text[:split_pos - estart]
            kept_after  = run_text[split_pos - estart:]
            if kept_before:
                final_children.append(clone_run_with_text(el, kept_before))
            ins_el = make_ins_wrapper(insert_text, author, date, base_id)
            final_children.append(ins_el)
            inserted = True
            if kept_after:
                final_children.append(clone_run_with_text(el, kept_after))

    if not inserted:
        ins_el = make_ins_wrapper(insert_text, author, date, base_id)
        final_children.append(ins_el)

    for child in list(para):
        para.remove(child)
    for child in final_children:
        para.append(child)

    return True, None, ins_el, None


# ── New paragraph insertion — table-safe ─────────────────────────────────────

def insert_paragraph_at_end_of_body(body, insert_text, author, date, change_id):
    """
    Insert a new paragraph at the true end of the document body.

    Inserts immediately before w:sectPr (which must remain the last body child),
    or appends to the body if no sectPr is present.  This ensures the paragraph
    lands in the document body rather than inside the last table cell — which is
    what body.findall('.//w:p')[-1] would return when the document ends with a table.
    """
    new_para = etree.Element(w('p'))
    ins_el = etree.SubElement(new_para, w('ins'))
    ins_el.set(w('id'), str(change_id))
    ins_el.set(w('author'), author)
    ins_el.set(w('date'), date)
    run = etree.SubElement(ins_el, w('r'))
    t = etree.SubElement(run, w('t'))
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    t.text = insert_text

    sect_pr = body.find(w('sectPr'))
    if sect_pr is not None:
        sect_pr.addprevious(new_para)
    else:
        body.append(new_para)

    return new_para


def insert_new_paragraph_after(body, anchor_para, insert_text, author, date, change_id):
    """
    Insert a new paragraph with full tracked-insertion markup after anchor_para.

    Table-safe: uses anchor_para.getparent() instead of body.index(), so this
    works whether the anchor paragraph is a direct body child or nested inside
    a table cell (w:tbl > w:tr > w:tc > w:p).

    Returns the new paragraph element.
    """
    new_para = etree.Element(w('p'))
    ins_el = etree.SubElement(new_para, w('ins'))
    ins_el.set(w('id'), str(change_id))
    ins_el.set(w('author'), author)
    ins_el.set(w('date'), date)
    run = etree.SubElement(ins_el, w('r'))
    t = etree.SubElement(run, w('t'))
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    t.text = insert_text

    parent = anchor_para.getparent()
    if parent is None:
        # Fallback: anchor directly in body
        idx = list(body).index(anchor_para)
        body.insert(idx + 1, new_para)
    else:
        siblings = list(parent)
        idx = siblings.index(anchor_para)
        parent.insert(idx + 1, new_para)

    return new_para


# ── Comment machinery ─────────────────────────────────────────────────────────

def add_comment_to_xml(comments_root, comment_id, author, date, text):
    """Append a <w:comment> element to the comments XML tree."""
    comment = etree.SubElement(comments_root, w('comment'))
    comment.set(w('id'), str(comment_id))
    comment.set(w('author'), author)
    comment.set(w('date'), date)
    para = etree.SubElement(comment, w('p'))
    run = etree.SubElement(para, w('r'))
    t = etree.SubElement(run, w('t'))
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    t.text = text


def wrap_element_with_comment_markers(target_el, comment_id):
    """
    Wrap a specific element (w:del or w:ins) with comment range start/end markers.
    The comment bubble highlights only that element, not the whole paragraph.
    """
    start = etree.Element(w('commentRangeStart'))
    start.set(w('id'), str(comment_id))
    end = etree.Element(w('commentRangeEnd'))
    end.set(w('id'), str(comment_id))

    target_el.addprevious(start)
    target_el.addnext(end)

    ref_run = etree.Element(w('r'))
    rPr = etree.SubElement(ref_run, w('rPr'))
    rStyle = etree.SubElement(rPr, w('rStyle'))
    rStyle.set(w('val'), 'CommentReference')
    ref = etree.SubElement(ref_run, w('commentReference'))
    ref.set(w('id'), str(comment_id))
    end.addnext(ref_run)


def wrap_para_with_comment_markers(para, comment_id):
    """
    Fallback: wrap the entire paragraph content with comment range markers.
    Used for comment_only changes.
    """
    start = etree.Element(w('commentRangeStart'))
    start.set(w('id'), str(comment_id))
    end = etree.Element(w('commentRangeEnd'))
    end.set(w('id'), str(comment_id))

    children = [c for c in para if c.tag != w('pPr')]
    if children:
        children[0].addprevious(start)
        children[-1].addnext(end)
    else:
        para.append(start)
        para.append(end)

    ref_run = etree.SubElement(para, w('r'))
    rPr = etree.SubElement(ref_run, w('rPr'))
    rStyle = etree.SubElement(rPr, w('rStyle'))
    rStyle.set(w('val'), 'CommentReference')
    ref = etree.SubElement(ref_run, w('commentReference'))
    ref.set(w('id'), str(comment_id))


# ── ID collision prevention ───────────────────────────────────────────────────

def get_max_existing_revision_id(doc_tree):
    """Scan document for existing w:ins and w:del id attributes, return max."""
    max_id = 0
    for el in doc_tree.iter(w('ins'), w('del')):
        id_val = el.get(w('id'))
        if id_val and id_val.isdigit():
            max_id = max(max_id, int(id_val))
    return max_id


def get_unique_rel_id(rels_text):
    """Find a relationship ID not already used in the rels XML."""
    existing = re.findall(r'Id="(rId\w+)"', rels_text)
    existing_set = set(existing)
    i = 1
    while f'rId{i}' in existing_set:
        i += 1
    return f'rId{i}'


# ── Main ──────────────────────────────────────────────────────────────────────

def apply_redlines(input_path, redlines_path, output_path):
    with open(redlines_path) as f:
        payload = json.load(f)

    author = payload.get('author', 'Q2 Legal')
    date = payload.get(
        'date',
        datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')
    )
    changes = payload.get('changes', [])

    if not isinstance(changes, list):
        raise ValueError("redlines.json field 'changes' must be a list")
    for i, change in enumerate(changes):
        if not isinstance(change, dict):
            raise ValueError(f"changes[{i}] must be an object")

    input_path = Path(input_path)
    redlines_path = Path(redlines_path)
    if not input_path.is_file():
        raise FileNotFoundError(f"input DOCX not found: {input_path}")
    if not redlines_path.is_file():
        raise FileNotFoundError(f"redlines JSON not found: {redlines_path}")

    import tempfile, os as _os

    # Keep the caller's requested destination separate from the scratch file.
    # If the destination is locked we fail immediately with a clear message
    # rather than silently finishing but writing somewhere unexpected.
    requested_output_path = Path(output_path)
    requested_output_path.parent.mkdir(parents=True, exist_ok=True)
    if requested_output_path.exists():
        try:
            requested_output_path.unlink()
        except PermissionError:
            print(
                f"ERROR: output file '{requested_output_path}' is locked by another "
                f"process and cannot be overwritten. Close the file and try again.",
                file=sys.stderr,
            )
            sys.exit(1)

    # Work on a temp file; move to the requested destination when finished.
    tmp_fd, tmp_path = tempfile.mkstemp(suffix='.docx')
    _os.close(tmp_fd)
    work_path = Path(tmp_path)

    shutil.copy2(input_path, work_path)

    with zipfile.ZipFile(work_path, 'r') as z:
        doc_xml = z.read('word/document.xml')
        try:
            comments_xml = z.read('word/comments.xml')
        except KeyError:
            comments_xml = (
                b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                b'<w:comments xmlns:w="http://schemas.openxmlformats.org/'
                b'wordprocessingml/2006/main"></w:comments>'
            )
        try:
            rels_xml = z.read('word/_rels/document.xml.rels')
        except KeyError:
            # Create a minimal relationships file so we can always add the
            # comments relationship; without this the comments part is invisible
            # to Word even when the content-type entry is present.
            rels_xml = (
                b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                b'<Relationships xmlns="http://schemas.openxmlformats.org/'
                b'package/2006/relationships"></Relationships>'
            )
        all_files = {name: z.read(name) for name in z.namelist()}

    doc_tree = etree.fromstring(doc_xml)
    comments_tree = etree.fromstring(comments_xml)
    body = doc_tree.find('.//' + w('body'))
    paragraphs = body.findall('.//' + w('p'))

    skipped = []

    # Start change IDs above any already in the document to avoid collisions
    change_id = get_max_existing_revision_id(doc_tree) + 1

    # Start comment IDs above any already in the comments part
    existing_comment_ids = [
        int(c.get(w('id'), 0))
        for c in comments_tree.findall(w('comment'))
    ]
    comment_id = (max(existing_comment_ids) + 1) if existing_comment_ids else 0

    for change in changes:
        ctype = change.get('type')
        comment_text = change.get('comment', '')

        if ctype == 'replace':
            find_text   = change.get('find', '')
            delete_text = change.get('delete', find_text)
            insert_text = change.get('insert', '')
            if not find_text:
                skipped.append('SKIP replace: empty find text')
                continue
            para_idx, para = find_para_for_text(paragraphs, find_text)
            if para is None:
                skipped.append(f"SKIP replace: could not find '{find_text[:60]}'")
                continue
            ok, del_el, ins_el, reason = rebuild_para_with_replace(
                para, find_text, delete_text, insert_text, author, date, change_id)
            if not ok:
                skipped.append(
                    f"SKIP replace: {reason or 'rebuild failed'} for '{find_text[:60]}'"
                )
                continue
            change_id += 2
            if comment_text:
                add_comment_to_xml(comments_tree, comment_id, author, date, comment_text)
                anchor_el = del_el if del_el is not None else ins_el
                if anchor_el is not None:
                    wrap_element_with_comment_markers(anchor_el, comment_id)
                else:
                    wrap_para_with_comment_markers(para, comment_id)
                comment_id += 1

        elif ctype == 'insert':
            after_text  = change.get('after', '')
            insert_text = change.get('insert', '')
            if after_text == '':
                # End-of-document: add a body-level paragraph immediately before
                # w:sectPr so it lands in the document body, not a table cell.
                new_para = insert_paragraph_at_end_of_body(
                    body, insert_text, author, date, change_id)
                change_id += 1
                paragraphs = body.findall('.//' + w('p'))
                if comment_text:
                    add_comment_to_xml(comments_tree, comment_id, author, date, comment_text)
                    ins_el = new_para.find('.//' + w('ins'))
                    if ins_el is not None:
                        wrap_element_with_comment_markers(ins_el, comment_id)
                    else:
                        wrap_para_with_comment_markers(new_para, comment_id)
                    comment_id += 1
                continue
            else:
                _, anchor_para = find_para_for_text(paragraphs, after_text)
            if anchor_para is None:
                skipped.append(f"SKIP insert: could not find anchor '{after_text[:60]}'")
                continue
            new_para = insert_new_paragraph_after(
                body, anchor_para, insert_text, author, date, change_id)
            change_id += 1
            paragraphs = body.findall('.//' + w('p'))
            if comment_text:
                add_comment_to_xml(comments_tree, comment_id, author, date, comment_text)
                ins_el = new_para.find('.//' + w('ins'))
                if ins_el is not None:
                    wrap_element_with_comment_markers(ins_el, comment_id)
                else:
                    wrap_para_with_comment_markers(new_para, comment_id)
                comment_id += 1

        elif ctype == 'comment_only':
            find_text = change.get('find', '')
            if not find_text:
                skipped.append('SKIP comment_only: empty find text')
                continue
            para_idx, para = find_para_for_text(paragraphs, find_text)
            if para is None:
                skipped.append(f"SKIP comment_only: could not find '{find_text[:60]}'")
                continue
            if comment_text:
                add_comment_to_xml(comments_tree, comment_id, author, date, comment_text)
                wrap_para_with_comment_markers(para, comment_id)
                comment_id += 1

        else:
            skipped.append(f"SKIP unknown type: {ctype}")

    new_doc_xml = etree.tostring(
        doc_tree, xml_declaration=True, encoding='UTF-8', standalone=True)
    new_comments_xml = etree.tostring(
        comments_tree, xml_declaration=True, encoding='UTF-8', standalone=True)

    all_files['word/document.xml'] = new_doc_xml
    all_files['word/comments.xml'] = new_comments_xml

    rels_text = rels_xml.decode('utf-8')
    if 'comments.xml' not in rels_text:
        rel_id = get_unique_rel_id(rels_text)
        rels_text = rels_text.replace(
            '</Relationships>',
            f'<Relationship Id="{rel_id}" '
            f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments" '
            f'Target="comments.xml"/></Relationships>'
        )
    all_files['word/_rels/document.xml.rels'] = rels_text.encode('utf-8')

    ct_xml = all_files.get('[Content_Types].xml', b'').decode('utf-8')
    if 'comments.xml' not in ct_xml:
        ct_xml = ct_xml.replace(
            '</Types>',
            '<Override PartName="/word/comments.xml" '
            'ContentType="application/vnd.openxmlformats-officedocument'
            '.wordprocessingml.comments+xml"/></Types>'
        )
        all_files['[Content_Types].xml'] = ct_xml.encode('utf-8')

    with zipfile.ZipFile(work_path, 'w', zipfile.ZIP_DEFLATED) as zout:
        for name, data in all_files.items():
            zout.writestr(name, data)

    # Move temp file to the originally requested destination.
    try:
        shutil.move(str(work_path), str(requested_output_path))
    except (PermissionError, shutil.Error):
        # If the atomic move fails (e.g. cross-device), fall back to copy + delete.
        try:
            shutil.copy2(str(work_path), str(requested_output_path))
        except Exception as exc:
            print(f"ERROR: could not write output to '{requested_output_path}': {exc}",
                  file=sys.stderr)
            sys.exit(1)
        finally:
            try:
                work_path.unlink()
            except Exception:
                pass

    if skipped:
        print('\nSkipped changes:', file=sys.stderr)
        for s in skipped:
            print(f'  {s}', file=sys.stderr)

    print(f'Done. Output: {requested_output_path}')


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: apply_redlines.py <input.docx> <redlines.json> <output.docx>')
        sys.exit(1)
    apply_redlines(sys.argv[1], sys.argv[2], sys.argv[3])
