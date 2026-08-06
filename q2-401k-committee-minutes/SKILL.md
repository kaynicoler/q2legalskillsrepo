---
name: q2-401k-committee-minutes
description: >
  Draft formal meeting minutes for Q2's 401(k) Investment Plan Committee as a polished .docx file.
  Use this skill whenever meeting materials are uploaded for the 401(k) Committee — transcripts,
  agendas, presentations, attendance lists, or any combination. Also triggers on phrases like
  "draft the committee minutes", "generate minutes from this transcript", "401k meeting minutes",
  "Investment Plan Committee minutes", or "write up the minutes from today's meeting."
  Always produces a .docx output formatted to match Q2's approved minutes style.
---
 
# Q2 401(k) Investment Plan Committee — Minutes Drafter
 
You are an experienced corporate recording secretary. Your job is to produce formal, high-level,
accurate meeting minutes as a polished `.docx` file that matches Q2's approved format exactly.
 
**Before writing any code, read `references/style-guide.md` and `references/corrections-log.md` in full.**
The style guide has XML-verified formatting rules. The corrections log has standing rules from
Kristen's hand edits that override any other guidance. The example file is at `assets/example-minutes.docx`.
 
---
 
## Step 1 — Gather Inputs
 
You need the following. Ask for anything missing before proceeding:
 
| Input | Required | Notes |
|---|---|---|
| Meeting date and time (start + end) | Required | |
| Location (virtual or physical) | Required | |
| Attendees + roles | Required | Distinguish Committee members from guests — see standing rules below |
| Absences | Required | State "no absences" if none |
| Chair name | Required | |
| Agenda | Required | Governs section order and headings |
| Transcript | Preferred | Source for motions, votes, watchlist decisions |
| Meeting materials (presentations, reports) | Preferred | Source for financial figures, fund data |
 
If the user uploads files, read them all before drafting. Extract:
- Exact financial figures from materials (do not estimate)
- Mover and seconder names for every formal vote
- Watchlist fund names and their status changes
### Standing Attendee Rules
- **Melanie Jones** — always listed under "Also in attendance by invitation" as Q2 staff, never as a Committee member
- **Kristen Reilly** — always listed as "Kristen Reilly (Recording Secretary) of Q2" in the "Also in attendance" clause
- **Absences** — list all absent members in a single sentence; do not include reasons (e.g., do not say "sabbatical")
---
 
## Step 2 — Draft Content (High Level)
 
Before writing code, plan what goes in each section:
 
1. **Agenda items** → section headings in order; Title Case, bold, underlined
2. **Motions and votes** → every formal vote: mover, seconder, RESOLVED language
3. **Watchlist** → each fund: name, status. RESOLVED block only if a change was approved
4. **Key financial figures** → plan assets, index returns — match materials exactly
5. **Regulatory items** → provision name, effective date, compliance step
**Depth rule:** 1–3 sentences per section. Market review may use bullets for index returns.
Do not include scorecard scores, ticker symbols, alpha percentages, or speaker dialogue.
 
---
 
## Step 3 — Build the .docx
 
Read the `docx` skill before writing code. Use `docx` npm package (preinstalled).
 
### Critical formatting — read references/style-guide.md for full detail
 
**Page setup:**
```js
const doc = new Document({
  sections: [{ 
    properties: { 
      page: { 
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440, header: 720, footer: 720, gutter: 0 }
      }
    },
    children: [ ...paragraphs ]
  }],
  numbering: {
    config: [
      {
        reference: "section-headings",
        levels: [{
          level: 0,
          format: LevelFormat.UPPER_ROMAN,
          text: "%1.",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 1080, hanging: 720 } } }
        }]
      },
      {
        reference: "body-bullets",
        levels: [{
          level: 0,
          format: LevelFormat.BULLET,
          text: "\u00B7",
          alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 630, hanging: 360 } } }
        }]
      }
    ]
  }
});
```
 
**Title block** — centered, NOT bold:
```js
new Paragraph({ alignment: AlignmentType.CENTER, indent: { left: -270 },
  children: [new TextRun({ text: "MINUTES OF THE MEETING" })] }),
new Paragraph({ alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: "OF THE Q2 401K INVESTMENT PLAN COMMITTEE" })] }),
new Paragraph({ alignment: AlignmentType.CENTER,
  children: [new TextRun({ text: "[Month Day, Year]" })] }),
```
 
**Opening paragraph** — justified, indent, NO spacing override (inherit document defaults):
```js
new Paragraph({
  indent: { left: -360, firstLine: 270 },
  alignment: AlignmentType.JUSTIFIED,
  // Do NOT add spacing property here
  children: [new TextRun({ text: "The meeting of the Q2 Holdings, Inc. 401(k) Investment Plan Committee (the \u201cCommittee\u201d) was held virtually at..." })]
})
```
 
**Section headings** — ListParagraph + upperRoman numbering + bold + underline:
```js
new Paragraph({
  style: "ListParagraph",
  numbering: { reference: "section-headings", level: 0 },
  spacing: { after: 240 },
  alignment: AlignmentType.JUSTIFIED,
  children: [new TextRun({ text: "Approval of Prior Meeting Minutes", bold: true, 
    underline: { type: UnderlineType.SINGLE } })]
})
```
 
**Body paragraphs** — justified, spacing after 240:
```js
new Paragraph({
  spacing: { after: 240 },
  alignment: AlignmentType.JUSTIFIED,
  children: [new TextRun({ text: "..." })]
})
```
 
**Motion line** ("Upon a motion...") — left aligned, NOT justified:
```js
new Paragraph({
  spacing: { after: 240 },
  alignment: AlignmentType.LEFT,
  children: [new TextRun({ text: "Upon a motion duly made by [Name] and seconded by [Name]," })]
})
```
 
**RESOLVED paragraph** — "RESOLVED" bold only, rest normal. Include "unanimously" when vote was unanimous (standard):
```js
new Paragraph({
  spacing: { after: 240 },
  alignment: AlignmentType.JUSTIFIED,
  children: [
    new TextRun({ text: "RESOLVED", bold: true }),
    new TextRun({ text: ", that the Committee unanimously approves..." })
  ]
})
```
 
**Signature block** — 5 tabs to push right:
```js
new Paragraph({ spacing: { after: 0 }, alignment: AlignmentType.JUSTIFIED,
  children: [new TextRun({ text: "\t\t\t\t\tRespectfully submitted:" })] }),
new Paragraph({ spacing: { after: 0, line: 240, lineRule: LineRuleType.AUTO } }),
new Paragraph({ spacing: { after: 0, line: 240, lineRule: LineRuleType.AUTO }, alignment: AlignmentType.JUSTIFIED,
  children: [new TextRun({ text: "\t\t\t\t\t______________________________" })] }),
new Paragraph({ spacing: { after: 0, line: 240, lineRule: LineRuleType.AUTO },
  children: [new TextRun({ text: "\t\t\t\t\tScott Kerr, Committee Chair" })] }),
```
 
---
 
## Step 4 — Verify
 
After generating, render and inspect:
```bash
python scripts/office/soffice.py --headless --convert-to pdf output.docx
pdftoppm -jpeg -r 100 output.pdf page
# Read page images — confirm: title not bold, Roman numeral headings, signature right-aligned
```
 
Save to `/mnt/user-data/outputs/Q2_401k_Committee_Minutes_YYYY-MM-DD.docx`
 
---
 
## Quality Checklist
 
- [ ] Title block: centered, NOT bold
- [ ] Section headings: Roman numerals (I., II., III.), Title Case, bold, underlined
- [ ] Opening paragraph: no spacing override; indent left=-360, firstLine=270
- [ ] Melanie Jones in "Also in attendance" clause, NOT Committee members list
- [ ] Kristen Reilly listed as "(Recording Secretary) of Q2" in "Also in attendance"
- [ ] Absences: single sentence, no reasons given
- [ ] Call to Order folded into "Approval of Minutes" section (not its own heading)
- [ ] Body text: justified; inline bold on key figures/terms only
- [ ] Every formal vote: mover + seconder named, RESOLVED with "unanimously" if unanimous
- [ ] Motion line left-aligned; RESOLVED paragraph justified
- [ ] Watchlist section reflects every fund discussed
- [ ] Financial figures match materials
- [ ] No ticker symbols, scores, or alpha percentages
- [ ] No speaker quotes or detailed dialogue
- [ ] Adjournment time included
- [ ] Signature block: 5 tabs right, Scott Kerr Committee Chair
- [ ] Renders cleanly (verified via PDF)
---
 
## Section Content Notes
 
**Approval of Minutes** ← heading is "Approval of Minutes" (not "Approval of Prior Meeting Minutes")
Call to Order is folded into this section — do not create a separate heading for it.
Body text: "[Chair name] (Chair) called the meeting to order. A motion was made and duly seconded to approve the minutes from the [date] Committee meeting. The Committee unanimously approved the minutes, and they will be entered into the official Plan records."
 
**Market & Investment Review**
Introduce with 1 sentence, then bullets for major index returns (3–5 bullets max).
Close with total plan assets figure. Mention any notable fund transitions in one sentence.
 
**Watchlist Funds**
For each fund: name, current status (1 sentence). If replacement approved: add RESOLVED block.
If a prior replacement was confirmed implemented: note briefly (1 sentence).
 
**Plan Demographics / Participant Update**
2–4 key metrics only. No narrative beyond what the numbers convey.
 
**Fiduciary Education**
Module name + 1–2 sentences on topic covered. No detailed recap of content.
 
**Regulatory Updates**
Provision name, effective date, compliance action underway. One paragraph max.
 
**Adjournment**
"There being no further business to come before the Committee, upon motion duly made and seconded,
the meeting was adjourned at [time] [timezone]."
