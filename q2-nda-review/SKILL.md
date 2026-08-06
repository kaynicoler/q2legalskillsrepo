---
name: q2-nda-review
description: Review NDAs and counterparty NDA redlines for Q2 Software, Inc. in Claude Cowork. Use when the user asks Cowork to assess counterparty changes, perform a full NDA review, explain a clause, recommend a response, or create a surgically redlined Word document. Review-only requests must return a concise legal assessment without editing files. Create or modify a DOCX only when the user expressly asks Cowork to apply redlines, add comments, or return a marked-up document.
---
 
# Q2 NDA Review for Claude Cowork
 
Use this source priority:
1. NDA under review
2. `references/q2_nda_review_playbook.md`
3. Q2 standard NDA templates available in the assigned Cowork folder
4. Other Q2 guidance available in the assigned Cowork folder
Review only what the NDA actually states. Do not infer missing language from a template, filename, heading, metadata, or prior form. If language is missing, say `Not found.` If language is ambiguous, say `Unclear.` Do not invent section numbers, parties, dates, headings, clauses, or counterparty edits.
 
## 1. Select exactly one mode
 
### Mode A: Review counterparty redlines
 
Use when the user asks Cowork to review, assess, summarize, accept, reject, or explain counterparty changes.
 
In this mode:
- Review only the counterparty's actual tracked changes, comments, or clearly identified edits.
- Do not perform a full clause-by-clause review unless the user also asks for one.
- Do not edit, compare, duplicate, rename, unzip, or create files.
- Do not run `apply_redlines.py`.
- Do not create a redlined DOCX.
- Do not narrate file operations, commands, internal planning, or hidden reasoning.
- Do not repeat the same issue in multiple sections.
- Do not treat unchanged language as a counterparty redline.
Return:
 
### Overall view
One or two sentences stating whether the changes are generally acceptable, require limited pushback, or contain material issues.
 
### Counterparty changes
For each actual change:
- **Change:** concise description
- **Recommendation:** Accept / Accept with clarification / Push back
- **Why:** one or two practical sentences tied to Q2's standard
- **Suggested response:** only when action is needed; provide a surgical revision or short comment
### Priority
Group only actual changes under:
- Must fix
- Prefer to fix
- Accept
Keep the answer concise and business-friendly.
 
### Mode B: Full NDA review
 
Use when the user asks whether the NDA is acceptable as a whole, requests a complete review, or provides an NDA without limiting the request to particular redlines.
 
Return:
1. Clauses Missing or Non-Compliant
2. Suggested Revisions / Redlines
3. Clauses Acceptable as-Is
4. Overall Recommendation: Good to sign / Sign with redlines / Not ready to sign
For each issue state:
- Clause or topic
- Status: Present / Not found / Unclear
- Supporting text from the NDA
- Whether it meets Q2's standard
- Short suggested revision if needed
Only list actual failures in the non-compliant section. Do not manufacture hypothetical concerns.
 
### Mode C: Apply redlines to a Word document
 
Use only when the user expressly asks Cowork to apply edits, add comments, prepare counter-redlines, or return a marked-up DOCX.
 
In this mode:
1. Read the NDA and the playbook.
2. Identify the minimum changes needed.
3. Preserve the counterparty's wording, formatting, defined terms, and clause order where possible.
4. Add comments only for material or non-obvious edits.
5. Author comments as `Q2 Legal`.
6. Save the final document in the user-assigned Cowork output folder. Do not overwrite the source document unless the user expressly requests that.
7. Use a clear filename such as `[original-name] - Q2 Redline.docx`.
8. After saving, provide only a short summary of material edits and the saved file location.
Use `apply_redlines.py` only when the source is a reliably editable DOCX and exact text anchors can be identified. The script is at `/mnt/skills/user/q2-nda-review/scripts/apply_redlines.py`. The script syntax is:
 
`python /mnt/skills/user/q2-nda-review/scripts/apply_redlines.py <input.docx> <redlines.json> <output.docx>`
 
If the source text is incomplete, image-only, corrupted, or cannot be edited reliably, state exactly:
 
`Cannot apply redlines reliably from provided text.`
 
Never create a document merely because a DOCX was supplied.
 
## 2. Q2 review standards
 
Apply `references/q2_nda_review_playbook.md` as the controlling standard.
 
Key rules:
- Prefer mutual obligations when both parties may disclose.
- Require a purpose-limited use restriction.
- Require at least reasonable care.
- Limit disclosure to representatives with a need to know and confidentiality duties.
- Require prompt notice of known unauthorized disclosure.
- For compelled disclosure, prefer prior notice unless legally prohibited and reasonable cooperation.
- Flag `Affiliate` or `Affiliates` whenever used but undefined.
- Prefer a defined agreement term and 2-5 year confidentiality survival, with trade secrets protected while they remain trade secrets.
- Accept routine backup retention subject to continuing confidentiality obligations.
- Prefer `may seek appropriate equitable relief` rather than automatic entitlement language.
- Reject NDA-breach indemnification, broad residuals, non-solicit or non-circumvent restrictions, IP assignment, and one-way fee shifting.
- Texas is preferred. New York and Delaware are acceptable. UK law may be acceptable for international matters.
- Do not redline language merely because it differs from Q2's template when it is functionally acceptable.
## 3. Counterparty-redline decision rules
 
For each actual redline, ask:
1. Does it materially reduce Q2's protection or add a new obligation?
2. Is it outside the playbook's preferred or fallback position?
3. Is it reciprocal or one-sided?
4. Can a narrow edit cure it?
5. Is it merely stylistic or administratively reasonable?
Use:
- **Accept:** functionally acceptable or favorable to Q2
- **Accept with clarification:** likely acceptable, but genuinely ambiguous
- **Push back:** materially weakens Q2's position or adds a prohibited term
Avoid exaggerated language such as `dangerous`, `guts the clause`, or `major red flag` unless the actual wording warrants it. Do not speculate about Q2's industry exposure, acquisition scenarios, or the counterparty's motives.
 
## 4. Redline and comment style
 
Make the minimum change necessary. Preserve acceptable language.
 
Use short comments such as:
- `Revised to keep the disclosure restriction mutual.`
- `Restored a reasonable-care standard.`
- `Narrowed use to the stated Purpose.`
- `Revised to notice and reasonable cooperation only.`
- `Q2 prefers “may seek” for equitable relief.`
Do not cite Q2's internal playbook or templates in counterparty-facing comments.
 
## 5. Cowork execution discipline
 
Cowork may work autonomously with local files, but the final response must contain only the requested work product.
 
Never show:
- shell commands or command output
- task logs or progress logs
- tool names
- temporary paths
- XML or DOCX internals
- internal planning or debate
- statements such as `Now I need to...`, `Let me...`, or `I am going to...`
Do not create extra intermediate deliverables in the user's output folder. Temporary working files must remain outside the output folder and be removed when the task is complete.
