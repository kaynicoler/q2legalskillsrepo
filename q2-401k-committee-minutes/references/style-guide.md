5 files


# Q2 401(k) Committee Minutes — Formatting Reference
 
Extracted from Q2's approved example minutes via XML inspection. Follow exactly.
 
---
 
## Page Setup
- US Letter: `12240 x 15840` DXA
- Margins: top/right/bottom/left = `1440` DXA (1 inch all sides)
- Header: `720`, Footer: `720`, Gutter: `0`
---
 
## Title Block (3 paragraphs, centered, NOT bold)
```
MINUTES OF THE MEETING
OF THE Q2 401K INVESTMENT PLAN COMMITTEE
[Month Day, Year]
```
- Style: `Normal`, alignment: `center`
- `<w:ind w:left="-270"/>` on first line only
- Font: theme minor font (`minorHAnsi`)
- **NOT bold** — this is a common mistake to avoid
---
 
## Opening Paragraph
- Style: `Normal`, alignment: `both` (justified)
- Spacing: `after="0"`, `line="240"` (single-spaced)
- Indent: `left="-360"`, `firstLine="270"`
- `autoSpaceDE="0"`, `autoSpaceDN="0"`, `adjustRightInd="0"`
- Begin: `The meeting of the Q2 Holdings, Inc. 401(k) Investment Plan Committee (the "Committee") was held virtually at...`
- Use smart quotes: `"` and `"`
---
 
## Section Headings — ListParagraph + upperRoman list
Section headings use a **numbered list** (Roman numerals I., II., III.) with `ListParagraph` style.
**Bold + underline** on the heading text.
 
In docx-js, create a `numbering` definition with:
- `reference: "section-headings"`
- `levels: [{ level: 0, format: LevelFormat.UPPER_ROMAN, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 1080, hanging: 720 } } } }]`
Each section heading paragraph:
```js
new Paragraph({
  style: "ListParagraph",
  numbering: { reference: "section-headings", level: 0 },
  spacing: { after: 240 },
  alignment: AlignmentType.JUSTIFIED,
  children: [
    new TextRun({ text: "Section Title Here", bold: true, underline: { type: UnderlineType.SINGLE } })
  ]
})
```
 
---
 
## Body Paragraphs
- Style: `Normal`, alignment: `both` (justified)
- Spacing: `after: 240`
- Font: theme minor (`minorHAnsi`) — in docx-js use default font, do not override
---
 
## Bullet Lists (market index returns, plan data highlights)
Use `ListParagraph` style with a bullet numbering definition:
- `reference: "body-bullets"`
- `levels: [{ level: 0, format: LevelFormat.BULLET, text: "\u00B7", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 630, hanging: 360 } } } }]`
Bullet paragraph:
```js
new Paragraph({
  style: "ListParagraph",
  numbering: { reference: "body-bullets", level: 0 },
  spacing: { after: 240 },
  alignment: AlignmentType.JUSTIFIED,
  children: [new TextRun({ text: "...", bold: false })]
})
```
Bold specific terms within bullets (e.g., index names) with inline `TextRun({ bold: true })`.
 
---
 
## Motion Line ("Upon a motion...")
- Style: `Normal`, alignment: `left` (NOT justified)
- Spacing: `after: 240`
- Plain text, no bold
---
 
## RESOLVED Paragraph
- Style: `Normal`, alignment: `both` (justified)
- Spacing: `after: 240`
- "RESOLVED" is bold only; rest of text is normal weight
- No underline on RESOLVED paragraph text
```js
new Paragraph({
  spacing: { after: 240 },
  alignment: AlignmentType.JUSTIFIED,
  children: [
    new TextRun({ text: "RESOLVED", bold: true }),
    new TextRun({ text: ", that the Committee approved..." })
  ]
})
```
 
---
 
## Adjournment Paragraph
Same as body paragraph: `Normal`, justified, `spacing after: 240`.
 
---
 
## Signature Block
Use 5 tab characters to push text to the right side of the page. No special indent.
```js
// "Respectfully submitted:" line
new Paragraph({
  spacing: { after: 0 }, // no extra space
  alignment: AlignmentType.JUSTIFIED,
  children: [
    new TextRun({ text: "\t\t\t\t\t" }),
    new TextRun({ text: "Respectfully submitted:" })
  ]
})
// Blank line
new Paragraph({ spacing: { after: 0, line: 240 } })
// Signature underline
new Paragraph({
  spacing: { after: 0, line: 240 },
  alignment: AlignmentType.JUSTIFIED,
  children: [
    new TextRun({ text: "\t\t\t\t\t" }),
    new TextRun({ text: "______________________________" })
  ]
})
// Chair name — no spacing override needed
new Paragraph({
  spacing: { after: 0, line: 240 },
  children: [
    new TextRun({ text: "\t\t\t\t\t" }),
    new TextRun({ text: "Scott Kerr, Committee Chair" })
  ]
})
```
 
---
 
## What the July 2026 Doc Got Wrong (do not repeat)
1. **Title block was bold** — example is NOT bold
2. **Section headings used manual Roman numerals** (e.g., `**I.  CALL TO ORDER**`) — example uses ListParagraph + numbered list
3. **Section heading text was ALL CAPS** — example is Title Case, bold, underlined
4. **Signature block was left-aligned** — example uses 5 tab stops to push right
5. **Content was too detailed** — the example keeps sections to 1-4 sentences max
---
 
## Opening Paragraph Template
```
The meeting of the Q2 Holdings, Inc. 401(k) Investment Plan Committee (the "Committee") was held 
[virtually / at {location}] at {time} (Central) on {date}. Present at the meeting were Committee 
members {names, with (Chair) after chair — Melanie Jones is NOT a Committee member}. Also in 
attendance by invitation were {Melanie Jones if present, }Kristen Reilly (Recording Secretary) of 
Q2, and {advisor first/last names} of Alliant Retirement Consulting, the Retirement Plan Advisor 
to the Committee. {Absence statement: "There were no absences." OR "[Name] and [Name] were absent."}
```
 
**Attendance classification (standing rules):**
- Committee members: Scott Kerr (Chair), Jonathan Price, Kim Rutledge, Keri Wright, John Breeden, Michael Quincey
- Q2 staff (always "Also in attendance"): Melanie Jones, Kristen Reilly (Recording Secretary)
- Alliant advisors (always "Also in attendance"): Jonathan Taporco, Drew Whitney, Sunit Patel, Paige Larson
- Absences: single sentence, no reasons — "X and Y were absent." not "X was absent (sabbatical)."
---
 
## Content Depth Rules
- **1–3 sentences per section** (market review may use brief bullets)
- No speaker dialogue or attribution beyond "Alliant presented" / "Taporco reviewed"
- Watchlist: fund name + status + RESOLVED block if replacement approved
- No scorecard scores, ticker symbols, or alpha percentages in final minutes
- Financial figures: match materials exactly for plan assets; round index returns to one decimal
