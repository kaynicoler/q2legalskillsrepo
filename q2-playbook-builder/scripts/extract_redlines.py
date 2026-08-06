#!/usr/bin/env python3
"""Extract tracked changes and comments from .docx files.
 
Usage:
    # Single file:
    python3 extract_redlines.py path/to/file.docx output_dir
 
    # Batch a vendor folder (all .docx within):
    python3 extract_redlines.py --folder path/to/vendor/ output_dir
 
    # Batch every vendor subfolder in a contract-type folder:
    python3 extract_redlines.py --all path/to/contract_type_folder/ output_dir
 
Output: one .txt file per .docx, with three sections:
    === INSERTIONS (N) === [author] text
    === DELETIONS (N) === [author] text
    === COMMENTS (N) === [author] text
"""
import zipfile
import re
import sys
import os
import argparse
from pathlib import Path
 
 
def extract(docx_path):
    """Return (doc_xml, insertions, deletions, comments)."""
    try:
        with zipfile.ZipFile(docx_path) as z:
            with z.open('word/document.xml') as f:
                doc_xml = f.read().decode('utf-8', errors='replace')
            try:
                with z.open('word/comments.xml') as f:
                    cmt_xml = f.read().decode('utf-8', errors='replace')
            except KeyError:
                cmt_xml = None
    except Exception as e:
        print(f"  [error reading {docx_path}: {e}]", file=sys.stderr)
        return None, [], [], []
 
    # Insertions <w:ins>...<w:t>text</w:t></w:ins>
    insertions = []
    for m in re.finditer(r'<w:ins\b[^>]*w:author="([^"]*)"[^>]*>(.*?)</w:ins>',
                         doc_xml, re.DOTALL):
        author = m.group(1)
        inner = m.group(2)
        texts = re.findall(r'<w:t[^>]*>([^<]*)</w:t>', inner)
        text = ''.join(texts).strip()
        if text:
            insertions.append((author, text))
 
    # Deletions <w:del>...<w:delText>text</w:delText></w:del>
    deletions = []
    for m in re.finditer(r'<w:del\b[^>]*w:author="([^"]*)"[^>]*>(.*?)</w:del>',
                         doc_xml, re.DOTALL):
        author = m.group(1)
        inner = m.group(2)
        texts = re.findall(r'<w:delText[^>]*>([^<]*)</w:delText>', inner)
        text = ''.join(texts).strip()
        if text:
            deletions.append((author, text))
 
    # Comments
    comments = []
    if cmt_xml:
        for m in re.finditer(
            r'<w:comment\b[^>]*w:author="([^"]*)"[^>]*>(.*?)</w:comment>',
            cmt_xml, re.DOTALL,
        ):
            author = m.group(1)
            inner = m.group(2)
            texts = re.findall(r'<w:t[^>]*>([^<]*)</w:t>', inner)
            text = ' '.join(texts).strip()
            if text:
                comments.append((author, text))
 
    return doc_xml, insertions, deletions, comments
 
 
def write_extraction(docx_path, out_dir):
    _, ins, dels, cmts = extract(docx_path)
    name = Path(docx_path).stem.replace(' ', '_')
    out_path = Path(out_dir) / f"{name}.txt"
    with open(out_path, 'w') as f:
        f.write(f"=== INSERTIONS ({len(ins)}) ===\n")
        for a, t in ins:
            f.write(f"[{a}] {t}\n")
        f.write(f"\n=== DELETIONS ({len(dels)}) ===\n")
        for a, t in dels:
            f.write(f"[{a}] {t}\n")
        f.write(f"\n=== COMMENTS ({len(cmts)}) ===\n")
        for a, t in cmts:
            f.write(f"[{a}] {t}\n")
    print(f"  {Path(docx_path).name}: {len(ins)} ins, {len(dels)} dels, {len(cmts)} cmts")
 
 
def process_folder(folder, out_dir):
    """Process every .docx in a folder."""
    docxs = sorted(Path(folder).glob('*.docx'))
    if not docxs:
        print(f"  (no .docx files in {folder})", file=sys.stderr)
        return
    os.makedirs(out_dir, exist_ok=True)
    for d in docxs:
        write_extraction(d, out_dir)
 
 
def process_all(parent_folder, out_dir):
    """Process every vendor subfolder."""
    parent = Path(parent_folder)
    if not parent.is_dir():
        print(f"Not a directory: {parent}", file=sys.stderr)
        sys.exit(1)
    subfolders = [p for p in parent.iterdir() if p.is_dir()]
    if not subfolders:
        # Treat as flat folder
        process_folder(parent, out_dir)
        return
    for sub in sorted(subfolders):
        vendor = sub.name
        print(f"=== {vendor} ===")
        sub_out = Path(out_dir) / vendor
        os.makedirs(sub_out, exist_ok=True)
        process_folder(sub, sub_out)
 
 
def main():
    ap = argparse.ArgumentParser(description="Extract tracked changes from .docx files.")
    ap.add_argument('input', help='File or folder path')
    ap.add_argument('output', help='Output directory')
    ap.add_argument('--folder', action='store_true',
                    help='Treat input as a folder of .docx files (batch mode)')
    ap.add_argument('--all', action='store_true',
                    help='Treat input as a parent folder; process every vendor subfolder')
    args = ap.parse_args()
 
    if args.all:
        process_all(args.input, args.output)
    elif args.folder or os.path.isdir(args.input):
        process_folder(args.input, args.output)
    else:
        os.makedirs(args.output, exist_ok=True)
        write_extraction(args.input, args.output)
 
 
if __name__ == '__main__':
    main()
