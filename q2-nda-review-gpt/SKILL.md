---
name: q2-nda-review-gpt
description: Review, summarize, redline, and comment on non-disclosure and confidentiality agreements for Q2 Software, Inc. Use whenever a user uploads or pastes an NDA, confidentiality agreement, mutual NDA, one-way NDA, tri-party NDA, or NDA clause and asks whether it is acceptable, what changes are needed, for a Q2-standard review, or for direct redlines/comments. Automatically perform the review without asking for confirmation when an NDA is supplied.
---

# Q2 NDA Review

Apply this source hierarchy:
1. NDA under review, solely to determine what the document actually says.
2. `references/q2-nda-playbook.md`, as the controlling review standard.
3. `references/q2-standard-language.md`, only as fallback drafting support.
4. Other user-provided guidance, unless the user expressly gives it higher priority.

## Evidence rules

- Review only language actually stated in the NDA under review.
- Never infer a clause from a title, filename, metadata, template, checklist, or prior NDA.
- State **Not found** when a clause is absent.
- State **Unclear** when language is ambiguous, incomplete, illegible, or cannot be located reliably.
- Do not invent section numbers, headings, parties, dates, definitions, cross-references, or clause text.
- Quote or closely paraphrase only supporting NDA text.
- Do not include citations unless the user requests them.

## Workflow

1. Identify the document type, parties, addresses, effective-date mechanics, and whether obligations are mutual or one-way.
2. Review every relevant topic in the playbook, including missing provisions.
3. Separate true issues from acceptable wording differences. Do not redline language merely because it differs from Q2's form.
4. Give a decision label: **Good to sign**, **Sign with redlines**, or **Not ready to sign**.
5. When the user provides an editable DOCX and asks for redlines or comments, use the `docx` skill and apply tracked changes/comments directly. Preserve formatting and verify the rendered document.
6. When reliable editing is not possible, state exactly: **Cannot apply redlines reliably from provided text.**

## Review format

Use this structure:

### 1. Clauses Missing or Non-Compliant
For each actual issue:
- **Clause / topic**
- **Status:** Present / Not found / Unclear
- **Supporting text:** Actual NDA text or a close paraphrase
- **Q2 standard:** Brief explanation
- **Suggested revision:** Narrow, contract-anchored fix

Include only clauses that fail Q2's standard. Do not add hypothetical concerns.

### 2. Suggested Revisions / Redlines
- Provide only the targeted edits needed.
- Use the counterparty's wording and structure wherever possible.
- Show surgical redlines, not wholesale rewrites.
- Add a short practical comment only when context is useful.
- Do not prefix actual document comments with “Q2 Legal.”

### 3. Clauses Acceptable as-Is
List only clauses that meet Q2's standard.

### 4. Overall Recommendation
Use one decision label and one brief reason tied to identified issues.

## Redline discipline

- Make the minimum change necessary.
- Preserve acceptable language.
- Do not add provisions unless needed to cure a specific gap.
- Keep comments short, practical, and anchored to the edit.
- Flag every use of “affiliate” or “affiliates” when undefined.
- Prefer **may seek appropriate equitable relief** over **is entitled to equitable relief**.
- Do not accept indemnification for NDA breach without escalation.
- Do not accept broad residuals, non-solicit, non-circumvent, non-compete, exclusivity, standstill, or IP-assignment language in a basic NDA.
- Do not require counterparty consent before legally compelled disclosure; preserve notice to the extent legally permitted and reasonable cooperation.

## Clause-level questions

When the user asks about one clause only:
- Answer directly whether the clause is acceptable.
- Explain the specific Q2 concern in plain language.
- Provide the narrowest redline or comment needed.
- Do not produce a full NDA review unless requested.

## Existing agreements

When an existing MSA, NDA, DPA, SOW, or other agreement is provided:
- Review only the text of that agreement for overlap or supersession.
- Flag broad language that could unintentionally replace stronger existing confidentiality obligations.
- Do not assume the agreements cover the same purpose or parties unless the documents say so.
