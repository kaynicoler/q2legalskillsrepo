# Extraction Checklist
 
Pull every field below from the uploaded documents and, where applicable, from incorporated terms fetched via `web_fetch` in Step 3. If a field is not present in any reviewed source, mark it as `[NOT FOUND IN DOCUMENTS]` and flag it in the Internal Notes for Legal Ops.
 
When a field comes from fetched online terms rather than the uploaded documents, note the source (e.g., "per Celigo Terms of Service at https://...") so Legal Ops can verify against the version in effect at signing.
 
## Agreement identification
 
Do not collapse the MSA and order form into a single "Agreement" entry. Identify each operative document separately by its actual title, date, and role.
 
| Field | What to look for |
|---|---|
| MSA title and date | Full title and effective date of the master agreement providing governing terms |
| MSA termination status | Does the MSA expressly terminate with the order form, or does it continue independently? (Most MSAs continue — flag if documents are silent) |
| Operative order form / SOW title and date | Title and **effective date** of the current operative commercial document (order form, SOW, renewal, subscription order) — must be the most recent non-superseded document. Use effective date if stated; use signature date only if no effective date exists. |
| Operative addenda / supplements | List of any addenda or supplements determined operative or unclear in Step 2 — title, **full exact date** (day, month, year — never month-year only), and subject matter of each. If only month and year appear in the document, extract exactly what is stated and flag as `[CONFIRM EXACT ADDENDUM DATE]`. |
| Addendum survival status | For each addendum: Operative (expressly carried forward), Superseded (expressly replaced or terminated), or Unclear (newer order form is silent — flag for Legal Ops) |
| Parties | All parties to the agreement, including full legal entity names |
| Q2 entity name | Which Q2 entity is the contracting party (Q2 Software, Inc., Q2 Holdings, Inc., a subsidiary, etc.) |
| Vendor legal name | Full legal name of the vendor entity |
| Effective date | Date the MSA became effective |
| Amendment chain | List of amendments, if any, with dates and what they modified |
| Incorporated terms | Any terms incorporated by reference (online terms, vendor policies, etc.) — note whether the actual text is uploaded |
 
## Term and renewal
 
Pull all fields from the most recent **operative** order form, renewal document, amendment, or SOW (as established in Step 2). Do not populate term or renewal fields from a superseded document.
 
| Field | What to look for |
|---|---|
| Source document for term | Name and date of the operative document used to calculate term dates (must not be a superseded order form) |
| Initial term | Length of the original term as stated in the operative document |
| Renewal mechanic | Auto-renew, mutual agreement to renew, fixed term with no renewal, or other — cite the provision |
| Renewal term length | If auto-renew, length of each renewal term (e.g., "one-year terms") |
| Renewal date | The specific calendar date on which the agreement renews (e.g., "September 1 each year"), if stated — state separately from term end date |
| Current term start date | When the current term began, per the operative document |
| Current term end date | When the current term expires — if renewal is on September 1, current term ends August 31 immediately preceding that date. State as a specific calendar date, not a duration. |
| Next auto-renewal date | The date the agreement will next automatically renew if notice is not sent — state as a specific calendar date, separate from current term end date |
| Master agreement status | Whether the master agreement continues after the order form expires, or whether it expressly terminates with the order form — flag if documents are silent |
 
## Notice and termination
 
| Field | What to look for |
|---|---|
| Required notice period | How much advance notice is required (e.g., 60 days, 90 days) |
| Notice deadline | Computed date: term end minus required notice period |
| Termination rights | What termination rights exist (standard, for cause, for convenience) — cite section numbers |
| Termination for cause provisions | Specific cause triggers (breach, nonpayment, insolvency, etc.) and any cure period |
| Termination for convenience provisions | Whether either party may terminate without cause, and any conditions |
| Non-renewal provisions | How to prevent auto-renewal, if applicable |
 
## Notice delivery
 
| Field | What to look for |
|---|---|
| Required delivery method | How notice must be delivered (email, certified mail, overnight courier, etc.) |
| Vendor notice address | Physical address for notice delivery, per the notice clause |
| Vendor notice email | Email address for notice delivery, per the notice clause |
| Required recipient | Named individual or role who must receive notice |
 
## Post-termination obligations
 
| Field | What to look for |
|---|---|
| Data return or deletion | Whether the agreement requires return, deletion, or destruction of Q2 data |
| Confidential information return or destruction | Whether confidential information must be returned or destroyed |
| Certification requirement | Whether written certification of destruction is required |
| Destruction timeline | Whether the agreement specifies a deadline for destruction/certification (e.g., "within 30 days of termination"). If silent, note "Agreement silent" — the notice will use 30 business days from date of letter as default. |
| Post-term data export window | Any period after termination during which Q2 may export data |
| Transition or wind-down obligations | Any required transition assistance or wind-down services |
| Surviving provisions | Sections that survive termination or expiration |
 
## Signatory and sender
 
| Field | What to look for |
|---|---|
| Q2 signatory on original agreement | Who signed for Q2 originally (informational only — the notice sender is Scott Kerr unless the user says otherwise) |
| Vendor signatory on original agreement | Who signed for the vendor (potential notice recipient) |
 
## Services
 
| Field | What to look for |
|---|---|
| Services description | Brief description of the services provided under the agreement |
| Contract value | Annual or total contract value, if stated (informational for Legal Ops context) |
