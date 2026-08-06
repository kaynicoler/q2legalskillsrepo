---
name: q2-playbook-builder
description: >
  Build a Q2 contract review playbook for any agreement type from the negotiation
  history (Q2 template plus vendor or customer redline rounds). Use whenever the user
  asks to "build a playbook," "build a contract review playbook," "generate a playbook
  from negotiations," "create a playbook from redlines," "turn these contracts into a
  playbook," or points at a folder of redlined agreements and wants a reusable review
  guide. Works for any Q2 contract type — NDA, MSA, SaaS, DPA, vendor agreement,
  customer agreement, partnership agreement, SOW, amendment, marketplace developer
  agreement, or any other commercial contract Q2 negotiates. Output is a populated
  Q2 playbook Excel file with 17 columns of guidance per clause, plus Executive
  Summary, Open Issues, AI Review Prompts, and Clause Library sheets.
---
 
# Q2 Playbook Builder — Convert Redline History into Reusable Review Playbook
 
You are acting as a senior commercial contracts attorney for Q2 Software, Inc. building
a contract review playbook from historical negotiation records. The playbook captures
Q2's actual negotiated positions across vendors and produces a reusable guide future
reviewers can apply to new contracts of the same type.
 
This skill is for converting completed negotiation history into durable playbook rules.
It is NOT for reviewing a single contract — for that, use `q2-contract-review`.
 
---
 
## Step 0: Resolve Skill Paths
 
Before doing any work, locate this skill's install directory. The bundled scripts and
reference files live inside the skill directory, NOT the bash working directory.
 
**In bash**, find the skill directory by running:
 
```bash
SKILL_DIR=$(find /sessions -path "*/skills/q2-playbook-builder" -type d 2>/dev/null | head -1)
echo "Skill directory: $SKILL_DIR"
ls "$SKILL_DIR/scripts/" "$SKILL_DIR/references/"
```
 
All subsequent commands that reference `scripts/` or `references/` MUST be prefixed
with `$SKILL_DIR/`. For example:
- `python3 "$SKILL_DIR/scripts/extract_redlines.py" ...`
- `--template "$SKILL_DIR/references/playbook-template.xlsx"`
If using the Read tool instead of bash, use the Windows path where this SKILL.md lives
(the parent directory of this file) to locate `scripts/` and `references/`.
 
**Save all output files** to the user's workspace folder (the mounted folder the user
selected), not to the skill directory or the bash working directory.
 
---
 
## Step 1: Confirm Scope
 
Ask the user (if not already provided):
 
1. **Contract type** (e.g., "Partner Marketplace Developer Agreement," "Mutual NDA," "SaaS Subscription Agreement"). This becomes the title of the playbook.
2. **Source folder path** — the folder containing one subfolder per counterparty, with all rounds of redlines and the executed copy. If the structure is different (e.g., flat folder, single counterparty), confirm before proceeding.
3. **Template baseline** — which document is Q2's starting template? Confirm with the user if unclear. The template is the comparator for identifying deviations.
4. **Review depth** — full review of every interim redline (default), or template + first counterparty redline + Q2 response + executed copy only (faster).
5. **Scope filter** — include every clause any vendor negotiated (recommended), only clauses negotiated by 2+ vendors, or all clauses in the agreement.
6. **Output folder** — default to the user's workspace folder (the mounted folder the user selected in Cowork).
Use the `AskUserQuestion` tool for the confirm step before doing any work.
 
---
 
## Step 2: Inventory the Folder
 
Confirm the folder contains:
- Q2's template or first draft (the comparator).
- For each counterparty: an opening counterparty redline, at least one Q2 response, ideally one execution copy.
- Optionally: SDK agreements, term sheets, side letters, amendments, schedules.
Flag and report (do not silently skip):
- Counterparty folders with no Q2 response (Q2's positions unclear).
- Counterparty folders with no executed copy (deal may not have closed).
- Files outside the expected naming convention.
---
 
## Step 3: Extract Redlines
 
Use the bundled `scripts/extract_redlines.py` to pull insertions, deletions, and comments
from every `.docx` in every vendor subfolder. The script reads the underlying XML so it
captures author attribution, even when Word's "Reviewing pane" view obscures it.
 
First, ensure openpyxl is installed (needed for Step 7):
```bash
pip install openpyxl --break-system-packages -q
```
 
To process all vendor subfolders under the source folder at once, use the `--all` flag:
```bash
python3 "$SKILL_DIR/scripts/extract_redlines.py" --all "<source_folder>" "<output_dir>/extractions"
```
 
To process a single vendor subfolder:
```bash
python3 "$SKILL_DIR/scripts/extract_redlines.py" --folder "<vendor_subfolder>" "<output_dir>/extractions/<vendor_name>"
```
 
The output is one `.txt` file per agreement document, with three sections per file:
INSERTIONS, DELETIONS, COMMENTS — each tagged by author.
 
---
 
## Step 4: Read the Q2 Template
 
Read Q2's starting template in full. The template establishes the comparator. Identify
every distinct clause that may be negotiated: parties, definitions, scope, license grant,
agency appointment, fees, taxes, audit, security, data use, AI/ML use, confidentiality,
publicity, indemnification, LOL, term/termination, governing law, assignment, EULA,
exhibits.
 
---
 
## Step 5: For Each Clause, Trace the Negotiation
 
For every clause that appeared in any counterparty redline:
 
1. **Q2's starting position** — verbatim from the template.
2. **What counterparties commonly asked for** — patterns across vendors (mutuality, narrowing, deletion, addition).
3. **How Q2 responded** — from the Q2 response redlines.
4. **What language Q2 ultimately accepted** — from the executed copies.
5. **Where positions were inconsistent across vendors** — note explicitly.
Distinguish:
- **Preferred position** — Q2's opening or what Q2 holds firm on.
- **Acceptable fallback** — language Q2 has agreed to repeatedly.
- **Limited fallback** — language Q2 has accepted only for specific vendor profiles (size, deal value, data sensitivity).
- **Consistently rejected** — positions Q2 has rejected across the record.
Apply the add-on instruction: where Q2 accepted a counterparty position in one agreement
but rejected in others, do not automatically treat the accepted language as a fallback.
Identify the business or legal context. If the context is unclear, classify as "requires
escalation" rather than "acceptable fallback."
 
---
 
## Step 6: Build the Playbook Rules
 
For each clause, create one playbook row. Each row has 17 columns matching the Q2 playbook
template:
 
| Column | Content |
|---|---|
| Name | Short name of issue/clause |
| Type | Rule (standard guidance), Question (reviewer must investigate), or Risk (clause creates business/legal risk) |
| Text | Main playbook guidance — Q2's position clearly and practically |
| Fallback Position 1 | First acceptable fallback |
| Fallback Position 2 | Second acceptable fallback |
| Fallback Position 3 | Final fallback or escalation |
| Reviewer's Note | Practical guidance — negotiation patterns, when to escalate, what to watch for |
| Preferred Language 1 | Q2's preferred clause text |
| Preferred Language 2 | Alternative acceptable language |
| Preferred Language 3 | Additional variant |
| Suggested Comment 1 | Short Word comment for counterparty |
| Suggested Comment 2 | Firmer or fallback comment |
| Suggested Comment 3 | Escalation/final-position comment |
| Recommendation Prompt | Short prompt for an AI reviewer to detect this issue in future contracts |
| Low Risk Criteria | When the clause/deviation is low risk |
| Medium Risk Criteria | When medium risk |
| High Risk Criteria | When high risk — escalate |
 
**Drafting standards:**
- Be precise and conservative; do not overstate Q2's position if history is mixed.
- Use "may accept" only where history supports acceptance.
- Use "should reject" only where Q2 consistently rejected the position or the risk is clearly material.
- Where Q2's treatment was inconsistent, include escalation guidance.
- Suggested comments must be short enough to paste into Word (one or two sentences).
- Recommendation Prompt must be specific enough for an AI reviewer to detect the issue.
**Bad guidance to avoid:**
- "Review carefully"
- "Consider whether acceptable"
- "Standard provision"
**Good guidance pattern:**
- "Q2 should reject language that allows the partner to use Q2 customer data for benchmarking, analytics, product improvement, AI training, or unrelated business purposes unless the use is expressly limited to aggregated and de-identified data and approved by Q2."
Save the rules as a JSON file (list of objects with these 17 keys):
`name`, `type`, `text`, `fallback_1`, `fallback_2`, `fallback_3`, `reviewer_note`,
`preferred_language_1`, `preferred_language_2`, `preferred_language_3`,
`suggested_comment_1`, `suggested_comment_2`, `suggested_comment_3`,
`recommendation_prompt`, `low_risk`, `medium_risk`, `high_risk`
 
See `$SKILL_DIR/references/example-rule.json` for the expected JSON shape.
 
---
 
## Step 7: Write the Excel Playbook
 
Use the bundled `scripts/write_playbook.py` to populate the playbook template with the
rules. Run from bash:
 
```bash
python3 "$SKILL_DIR/scripts/write_playbook.py" \
    --template "$SKILL_DIR/references/playbook-template.xlsx" \
    --rules "<working_dir>/rules.json" \
    --exec-summary "<working_dir>/exec_summary.md" \
    --open-issues "<working_dir>/open_issues.md" \
    --ai-prompts "<working_dir>/ai_prompts.md" \
    --clause-library "<working_dir>/clause_library.md" \
    --out "<output_folder>/Q2 <Contract Type> - Contract Review Playbook.xlsx"
```
 
The script:
- Writes one row per rule to the `PlaybookChecks` sheet.
- Adds four summary sheets in this order: Executive Summary, Open Issues, AI Review Prompts, Clause Library.
- Preserves the original `CheckTypes` sheet.
- Formats headers, sets column widths, freezes the header row.
- Sets row heights to fit wrapped text.
Filename convention: `Q2 [Contract Type] - Contract Review Playbook.xlsx`
 
---
 
## Step 8: Generate the Four Summary Sheets
 
**Executive Summary** — overall negotiation patterns, most frequently negotiated clauses, where Q2 was most flexible, where Q2 was least flexible, attorney escalation triggers.
 
**Open Issues** — clauses where Q2's historical positions were inconsistent. For each, explain the inconsistency and recommend whether the playbook should adopt a standard position, fallback position, or escalation rule.
 
**AI Review Prompts** — one prompt per major playbook issue, written so an AI reviewer can detect the issue in a new draft.
 
**Clause Library** — preferred language extracted from Q2's strongest and most repeated negotiated positions. Do not invent new legal positions unless clearly labeled as a recommended standardization.
 
---
 
## Step 9: Quality Control
 
Before finalizing, verify:
 
- [ ] Every row is grounded in the actual redline history (no invented positions).
- [ ] Each fallback reflects language Q2 actually accepted or a reasonable synthesis of accepted language.
- [ ] High-risk criteria are specific and actionable.
- [ ] Suggested comments are short enough to paste into Word.
- [ ] Preferred language is distinguished from acceptable fallback language.
- [ ] No clause included merely because it is common in contracts — must be relevant to this contract type or supported by reviewed history.
- [ ] All 17 columns are populated for every row (use empty string for genuinely-not-applicable fields, not None).
- [ ] Workbook opens correctly and all sheets render.
---
 
## Step 10: Present to User
 
Call `mcp__cowork__present_files` with the Excel file path. Provide a brief summary:
- Number of vendors reviewed.
- Number of playbook rows generated.
- Key findings worth flagging (3-5 bullets).
- Open issues that may need escalation or further Q2 input.
Do NOT recap every clause. The user can open the workbook.
 
---
 
## Output Standards
 
- File name: `Q2 [Contract Type] - Contract Review Playbook.xlsx`
- Save to the user's workspace folder (the mounted folder the user selected).
- File must open in Excel without formula errors.
- All columns labeled per Q2 playbook template.
- Header row formatted (bold, Q2-color fill, wrap text).
- Freeze panes at row 2 so headers stay visible while scrolling.
---
 
## Escalation Rules
 
Stop and ask Q2 Legal before finalizing the playbook if:
 
- The folder contains fewer than 3 vendor negotiations (not enough pattern data — flag explicitly).
- Q2's positions are inconsistent on a high-risk clause (LOL cap, indemnity scope, security obligations).
- A new clause type appears in counterparty redlines that Q2's template doesn't address (e.g., AI/ML training).
- The agreements show Q2 accepted a position Q2 should not have (rare; flag for follow-up).
---
 
## Quality Checks the Skill Should Run
 
- Confirm Q2 template is identifiable in the folder.
- Confirm each vendor folder has at least one counterparty redline AND one Q2 response.
- Confirm executed copies exist (deal closed) — if not, note this and treat redline history as in-flight positions.
- Validate the rules JSON has 17 fields per rule before writing the Excel.
- Confirm the output file opens and has the expected sheet order.
---
 
## Future Enhancements
 
When user requests, this skill can be extended to:
 
- Generate the playbook directly as a Word memo for attorney review (instead of Excel).
- Run a tabular review across vendors first (one row per vendor, columns = clauses) before synthesis.
- Diff a new playbook against an existing playbook to surface what's changed.
- Re-run the playbook against a new contract version (the next time Q2 updates its template) to surface what playbook rows are now stale.
---
 
## Reference Materials
 
- `$SKILL_DIR/references/playbook-template.xlsx` — blank 17-column playbook template (canonical Q2 schema).
- `$SKILL_DIR/scripts/extract_redlines.py` — batch redline extractor.
- `$SKILL_DIR/scripts/write_playbook.py` — Excel writer that populates the template from a rules list.
- `$SKILL_DIR/references/example-rule.json` — one example playbook rule showing the JSON shape expected by the writer.
