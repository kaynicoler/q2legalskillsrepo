---
name: q2-policy-data-extractor
description: "Extract all key policy data from an insurance policy PDF and add it as a structured sheet to Q2's Policy Data Extraction workbook. Use this skill whenever Kristen uploads or points to an insurance policy PDF (policy, binder, renewal, endorsement, package) and wants data extracted, added to the workbook, or structured for tracking. Trigger on phrases like \"pull policy data\", \"add this policy to the workbook\", \"extract data from this policy\", \"add a sheet for this policy\", \"populate the tracker\", \"read this policy and pull the terms\", or any variation of capturing structured policy data in the Excel master tracker. Even if the user just uploads a policy PDF and says something vague like \"process this\" or \"do the usual\" in an Insurance Docs context, use this skill."
version: v1
updated: 2026-08-11T22:17:58.498Z
created: 2026-07-04T23:11:30.294Z
---
# Q2 Policy Data Extractor

This skill reads an insurance policy PDF from end to end and adds a fully-populated data sheet to Kristen's Policy Data Extraction workbook, following the established Field | Value | Policy Reference format used across all existing sheets.

## Workbook Location

The workbook lives at: `C:\Users\KReilly\OneDrive - Q2e\000 Legal Ops\Insurance Docs\Policy data extraction.xlsx`

In the bash sandbox, this is: `/sessions/hopeful-practical-brahmagupta/mnt/Insurance Docs/Policy data extraction.xlsx`

If the workbook has been moved, check the Insurance Docs folder for an xlsx file with "policy" and "data" or "extraction" in the name.

## Step 1 — Read the Entire Policy PDF

Always read all pages before writing any data. For large PDFs (20+ pages), read in batches of 10–15 pages to avoid output limits. Use pdfplumber:

```
import pdfplumber
with pdfplumber.open(pdf_path) as pdf: all_text = &quot;&quot; for i, page in enumerate(pdf.pages): text = page.extract_text() or &quot;&quot; print(f&quot;--- PAGE {i+1} ---&quot;) print(text) all_text += text + &quot;\n&quot;

```

If `extract_text()` returns empty or near-empty strings across multiple pages, the PDF is likely scanned. In that case, tell Kristen and ask whether to proceed with OCR (pytesseract + pdf2image).

Pay attention to:

- **Cover pages / transmittal** (usually pages 1–5): contain billing, premium breakdowns, and broker contacts but are not the policy itself
- **Declarations page**: the authoritative source for policy number, limits, retentions, premium, dates, and named insured; always prioritize Declarations over other pages for these fields
- **Policy body**: insuring clauses, exclusions, definitions, conditions
- **Schedule of Forms**: lists all endorsements by form number and edition date
- **Endorsements**: read each one; they often modify exclusions, add covered parties, or restrict coverage in ways that matter

## Step 2 — Propose a Sheet Name

Name the sheet after the policy line, short and clear. Examples:

- `Employed Lawyers`
- `Cyber - $5M xs $0`
- `D&O - Primary $10M`
- `EPL & Fiduciary`
- `Workers Comp`
- `Auto`
- `GL Primary`

If a sheet with that name already exists, ask Kristen whether to overwrite it or use a different name (e.g., `Employed Lawyers 2026`).

## Step 3 — Extract Policy Data

Extract all of the following. If a field is not stated in the policy, write `Not stated` in Value and `N/A` in Policy Reference. Never guess or fill in from general insurance knowledge.

For every field, include a specific **Policy Reference** pointing to where in the document the data came from (e.g., `Item 3, Declarations p.11`, `Section II(A), p.13`, `Endorsement No. 1, p.33`). This makes the extraction auditable.

### POLICY IDENTIFICATION

- Policy Number
- Policy Form / Form Numbers (from Schedule of Forms header or Declarations)
- Insurer / Carrier
- Named Insured (as stated on Declarations, including any "dba")
- Additional Named Insureds (if any)
- Principal Address
- Policy Period — effective date, expiration date, and local standard time notation if stated
- Policy Type / Coverage Line
- Claims-Made Notice (verbatim from Declarations if present)
- Date Issued / Date of Declarations
- Producing Agent / Broker Name
- Complaint Contact (if stated)

### COVERAGE & LIMITS

- Maximum Aggregate Limit of Liability
- Per Claim / Per Occurrence / Each Wrongful Act Limit (if separate from aggregate)
- All sublimits with dollar amounts
- Defense Costs treatment — note whether defense is **inside** the limit (eroding) or **in addition to** the limit

### INSURING CLAUSES

- Each insuring clause with its label and a one-sentence description of what it covers
- Note the coverage trigger (claims-made, wrongful act definition, who qualifies as an insured)

### PROFESSIONAL SERVICES / COVERED ACTIVITIES

- How the policy defines the scope of covered professional services or legal services
- Who qualifies as an "Insured Person" (employees, former employees, leased workers, contract lawyers, etc.)
- Any notable carve-outs from the definition

### RETENTIONS / DEDUCTIBLES

- Each retention or deductible with its dollar amount and the claim type or insuring clause it applies to
- Any $0 retentions and exceptions
- Whether the retention applies to defense costs, loss only, or both

### PREMIUM & FINANCIAL

- Total Annual Premium
- Premium by coverage part if broken out
- Taxes and fees (if stated separately)
- Terrorism / TRIA premium (if stated)
- Broker commission rate (if shown)
- Payment terms / installment structure (if stated)

### EXTENDED REPORTING PERIOD (ERP / TAIL)

- Optional ERP period(s) and premium(s)
- ERP purchase deadline
- Any automatic ERP provisions
- Whether ERP is available and under what conditions
- Limits impact — does ERP share the expiring policy limit or get a fresh limit?

### PENDING AND PRIOR LITIGATION DATE

- The specific retroactive/pending and prior date stated on Declarations

### ENDORSEMENTS

- Numbered list of all endorsements with form number, edition date, and a brief description of the operational effect (one sentence each)
- Flag endorsements that are unusual, restrictive, or provide important carve-backs

### KEY EXCLUSIONS

- Each named exclusion with a brief description
- Any carve-backs or exceptions — these are often as important as the exclusion itself
- Flag exclusions with broad carve-backs that restore significant coverage

### NOTICE & REPORTING REQUIREMENTS

- Claim notice — method, deadline, and to whom (exact address if stated)
- Circumstance / potential claim notice — whether and how it can be given before a formal claim
- Notice of cancellation by insured / by company
- Address for claims notices
- Address for all other notices

### CONDITIONS & ADMINISTRATIVE

- Defense / duty to defend or duty to pay (note which applies)
- Consent to settle (insured's right to consent vs. hammer clause)
- Related claims / interrelated wrongful acts
- Allocation
- Cancellation terms
- Territory / Coverage Territory
- Currency
- Subrogation rights
- Severability of application / innocent insured protections
- Other notable conditions (choice of law, dispute resolution, etc.)

### REVIEWER NOTES / OPEN ITEMS

- Numbered observations, gaps, or renewal flags
- Items that seem low relative to Q2's risk profile
- Restrictive language that may warrant renewal negotiation
- Unusual endorsements or conditions worth flagging for broker or outside counsel
- Any discrepancies between the binder/transmittal and the policy itself
- Any missing, unclear, or inconsistent information

## Step 4 — Write the Sheet

Use the bundled script at `scripts/write_policy_sheet.py`. Save the extracted data as a JSON file first, then run the script:

```
# 1. Save your extracted data to a JSON file
Format: list of [field, value, reference] lists
Use null for value/reference on section header rows
python /path/to/skill/scripts/write_policy_sheet.py \ --workbook &quot;/sessions/hopeful-practical-brahmagupta/mnt/Insurance Docs/Policy data extraction.xlsx&quot; \ --sheet-name &quot;Employed Lawyers&quot; \ --data /tmp/policy_data.json

```

The data JSON is a list of rows. Each row is a 3-element list `[field, value, reference]`. Use `null` for value and reference on **section header rows**:

```
[
[&quot;POLICY IDENTIFICATION&quot;, null, null], [&quot;Policy Number&quot;, &quot;0814-24-32&quot;, &quot;Item 1, Declarations p.11&quot;], [&quot;Insurer / Carrier&quot;, &quot;Federal Insurance Company (Chubb)&quot;, &quot;Item 2, Declarations p.11&quot;], [&quot;COVERAGE &amp; LIMITS&quot;, null, null], [&quot;Maximum Aggregate Limit&quot;, &quot;$5,000,000&quot;, &quot;Item 3, Declarations p.11&quot;] ]

```

The script handles: copying styles from the `EPL & Fiduciary` reference sheet, setting column widths (A=45, B=65, C=40), wrapping text, and freezing row 1.

## Accuracy Standards

- Base every field value on the actual policy text — do not fill in from general insurance knowledge.
- If a field is not stated, write `Not stated` in Value and `N/A` in Policy Reference.
- Distinguish the Declarations from the cover letter and premium bills — bills are not authoritative for policy terms.
- For ambiguous language, write what the policy says verbatim and flag it in Reviewer Notes.

## Completing the Task

After saving the workbook, present it to Kristen using `mcp**cowork**present_files` so she can open it directly. Note how many rows were written and which sheet was added.
