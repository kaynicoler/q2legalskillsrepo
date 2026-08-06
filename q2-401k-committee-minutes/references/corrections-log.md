# Corrections Applied by Kristen — July 28, 2026
 
These changes were made by hand to the AI-drafted July 6, 2026 minutes and must be reflected in all future drafts.
 
---
 
## 1. Attendee Classification — Melanie Jones is a Guest, Not a Committee Member
 
**Wrong:** "Committee members Scott Kerr (Chair), Jonathan Price, Kim Rutledge, Keri Wright, and Melanie Jones"
**Correct:** "Committee members Scott Kerr (Chair), Jonathan Price, Kim Rutledge, and Keri Wright. Also in attendance by invitation were Melanie Jones and Kristen Reilly (Recording Secretary) of Q2..."
 
**Rule:** Melanie Jones attends by invitation (Q2 staff), not as a Committee member. She belongs in the "Also in attendance" clause alongside Kristen Reilly.
 
---
 
## 2. Absences — Combine Into One Sentence
 
**Wrong:** "Michael Quincey was absent (sabbatical), and John Breeden was absent."
**Correct:** "Michael Quincey and John Breeden were absent."
 
**Rule:** List all absent members in a single sentence. Do not include absence reasons (e.g., sabbatical) in the minutes.
 
---
 
## 3. Opening Paragraph — No Spacing Override
 
**Wrong (in code):** `spacing: { after: 0, line: 240, lineRule: LineRuleType.AUTO }`
**Correct:** No `spacing` property on the opening paragraph — let it inherit document defaults.
 
---
 
## 4. Section Headings — No `rFonts` on Heading Paragraphs
 
The corrected document does NOT set `w:rFonts w:cstheme="minorHAnsi"` on the section heading `<w:pPr><w:rPr>`. Do not add font overrides to heading paragraphs.
 
---
 
## 5. RESOLVED Language — Add "unanimously" When Vote Was Unanimous
 
**Wrong:** "RESOLVED, that the Committee approves..."
**Correct:** "RESOLVED, that the Committee unanimously approves..."
 
**Rule:** When the vote is unanimous (which is typical), include "unanimously" in the RESOLVED clause.
 
---
 
## 6. Body Paragraph Bold — Some Body Paragraphs Are Bold (Not All)
 
In the corrected document, certain body paragraphs are bold at the paragraph level (not just inline bold on figures). This occurs on paragraphs that contain **mixed bold/normal inline runs** — Word applies bold to the paragraph `<w:rPr>` when the majority of runs are bold. Do not try to replicate paragraph-level bold in docx-js; instead use inline `TextRun({ bold: true })` for key figures and terms, and leave the paragraph-level rPr without bold. The rendering will appear correct.
 
---
 
## 7. Call to Order — Merged Into Approval of Minutes Section
 
**Wrong:** Separate "Call to Order" section + "Approval of Prior Meeting Minutes" section (two headings)
**Correct:** Single heading: **"Approval of Minutes"** — with the call to order noted in the body text of that section.
 
**Rule:** Do not create a separate "Call to Order" section. Fold it into the first agenda item (Approval of Minutes) with a brief sentence: "Scott Kerr (Chair) called the meeting to order."
 
---
 
## Summary of Rules for Future Drafts
 
| Item | Rule |
|---|---|
| Melanie Jones | Always in "Also in attendance" clause, not Committee members |
| Absences | Single sentence, no reasons given |
| Call to Order | Folded into Approval of Minutes section, not its own heading |
| RESOLVED (unanimous) | Include "unanimously" |
| Absence reasons | Do not include (e.g., do not say "sabbatical") |
