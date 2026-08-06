11 files


# DOCX Output Rules
 
**Always produce a finished Word (.docx) file.** Do not output the notice as plain text only. The file must use the bundled Q2 letterhead template.
 
## Primary approach: Edit the bundled template
 
A Q2 letterhead template is bundled with this skill at `references/q2-notice-template.docx`. **Always use this template.** Do not build documents from scratch with docx-js unless the template is unavailable.
 
### Step-by-step process
 
**1. Read the docx skill first:**
```
Read /mnt/skills/public/docx/SKILL.md
```
 
**2. Locate the bundled template.** The skill directory is wherever this SKILL.md lives. The template is at:
```
<skill_directory>/references/q2-notice-template.docx
```
If the skill is installed at `/mnt/skills/user/vendor-notice-engine/`, the template is at:
`/mnt/skills/user/vendor-notice-engine/references/q2-notice-template.docx`
 
**3. Unpack the template:**
```bash
python3 /mnt/skills/public/docx/scripts/office/unpack.py <path-to-template> /home/claude/notice-working/
```
 
**4. Edit `word/document.xml`** — replace all placeholders with notice-specific content (see placeholder list below).
 
**5. Clean up the template** (see Template cleanup section below).
 
**6. Repack:**
```bash
python3 /mnt/skills/public/docx/scripts/office/pack.py /home/claude/notice-working/ /mnt/user-data/outputs/<filename>.docx --original <path-to-template>
```
 
**7. Validate** — the pack script runs validation automatically. Fix any errors before presenting.
 
### Template placeholders
 
The bundled template contains these placeholders in `word/document.xml`. Replace each with the notice-specific value:
 
| Placeholder | Replace with |
|---|---|
| `[NOTICE DATE]` | Date of the notice (e.g., "June 24, 2026") |
| `[COUNTERPARTY LEGAL NAME]` | Vendor's full legal entity name |
| `[ADDRESS LINE 1]` | Street address |
| `[ADDRESS LINE 2]` | Second address line (if none, see cleanup below) |
| `[CITY, STATE ZIP]` | City, State ZIP |
| `[CONTACT NAME]` | Appears in Attn line and salutation — replace both |
| `[CONTACT TITLE]` | Recipient title (may be empty) |
| `[DELIVERY METHOD]` | In the "Sent via..." line |
| `[COUNTERPARTY EMAIL]` | Vendor notice email |
| `[COUNTERPARTY SHORT NAME]` | Short name used in body (e.g., "Celigo," "m3ter") |
 
The **opening paragraph** (from "Pursuant to Section [SECTION NO.]..." through "[EXPIRATION DATE].") must be **fully replaced** with notice-type-specific content. Do not try to fill individual placeholders within it — the paragraph structure differs by notice type.
 
The **data handling, certification, and closing paragraphs** are template boilerplate that must also be fully replaced or removed depending on the notice type. After replacing the opening paragraph, search for and delete every one of these stale template paragraphs (they will all be replaced by fresh content in the step below):
- The "Upon the conclusion of services..." data deletion paragraph
- The "Please confirm in writing..." certification paragraph
- The "Finally, Q2 requests that [VENDOR] certify in writing..." techniques/methods paragraph
- The "Should you have any questions or believe your records reflect a different expiration date..." duplicate closing
Then insert the closing paragraphs from the notice-type template in `references/notice-types/` **in this exact order — no exceptions:**
 
1. Data handling paragraph ("Upon the [expiration / termination] of the Agreement...")
2. Certification delivery paragraph ("Please deliver any written certification of destruction to Q2 Software, Inc., Attn: Legal Operations...")
3. Questions paragraph ("Please direct any questions regarding this notice to the undersigned.")
**The certification delivery paragraph always comes before the questions paragraph.** Do not reverse this order. The underlying DOCX template has these in a different sequence — ignore the template order and always write the paragraphs in the order listed above.
 
### Font size
 
After all replacements, change all font sizes from 11pt to 10pt:
```python
xml = xml.replace('w:val="22"', 'w:val="20"')
```
 
## Q2 letterhead specification
 
**Page setup**
- Paper: US Letter (12240 × 15840 DXA)
- Margins: top 864, right 1152, bottom 1008, left 1152 (DXA)
- Header distance: 720 DXA; Footer distance: 720 DXA
**Font**
- Default font: `Avenir LT Std 35 Light` (fallback: `Calibri`)
- Font size: 10pt throughout body and address block (`sz: 20` in docx-js)
- Exception: signature name line is bold 10pt
**Body paragraph formatting**
- Date, address block, delivery line, re line, salutation: left-aligned (default)
- All body paragraphs from opening paragraph through certification paragraph: fully justified (`AlignmentType.JUSTIFIED`)
- Signature block lines: left-aligned (default)
- Empty `Paragraph({})` for every blank line between sections
**Header**
The header contains the Q2 logo image (approximately 0.555 inches square, 799465 × 799465 EMU). Appears on every page (use the `default` header).
 
**Footer**
The footer contains a Q2 footer banner image (approximately 4.44 inches wide × 0.274 inches tall, 6393815 × 393065 EMU). Appears on every page (use the `default` footer).
 
**Signature image**
Embedded inline, approximately 1.7 inches wide × 0.57 inches tall (2449458 × 819192 EMU). If no signature image is available, leave a blank paragraph as a signing space.
 
> **When a prior Q2 notice is uploaded alongside the vendor agreement:** Extract the branding images from that template document and reuse them. This preserves the actual Q2 logo and footer assets.
 
## Template cleanup after placeholder replacement
 
The Q2 letterhead template has three address fields separated by `<w:br/>` line breaks: `[ADDRESS LINE 1]`, `[ADDRESS LINE 2]`, and `[CITY, STATE ZIP]`. When `[ADDRESS LINE 2]` is not needed (single-line street address), replacing it with an empty string leaves a blank `<w:t/>` run that creates an unwanted blank line between the street address and the city/state/zip line.
 
**Required fix — use str_replace to remove the ADDRESS LINE 2 run-pair when no second address line exists:**
 
After replacing `[ADDRESS LINE 1]` and `[CITY, STATE ZIP]`, check whether the vendor address has a second line (e.g., a suite number, floor, or c/o line). 
 
- **If ADDRESS LINE 2 is needed:** replace `[ADDRESS LINE 2]` with the actual value. Done.
- **If ADDRESS LINE 2 is not needed:** use str_replace to delete both the `[ADDRESS LINE 2]` run and the `<w:br/>` run that follows it. Remove this exact block from `word/document.xml`:
```xml
      <w:r>
        <w:rPr>
          <w:rFonts w:eastAsia="Times New Roman" w:cs="Times New Roman"/>
          <w:sz w:val="22"/>
          <w:szCs w:val="22"/>
        </w:rPr>
        <w:t>[ADDRESS LINE 2]</w:t>
      </w:r>
      <w:r>
        <w:rPr>
          <w:sz w:val="22"/>
          <w:szCs w:val="22"/>
        </w:rPr>
        <w:br/>
      </w:r>
```
 
Replace it with nothing (empty string). This leaves the street address run and city/state/zip run on consecutive lines with no gap. **Do not leave `[ADDRESS LINE 2]` unreplaced in the document** — an unfilled placeholder renders as a blank line in Word.
 
Also remove the `<w:attachedTemplate>` reference in `word/settings.xml` and its corresponding relationship in `word/_rels/settings.xml.rels` — the template references a local file path on the original author's machine and will fail validation.
 
## Extracting images from an uploaded Q2 template
 
If the user uploads a prior Q2 notice to use as a format reference:
 
```bash
python3 /mnt/skills/public/docx/scripts/office/unpack.py /mnt/user-data/uploads/<template>.docx /home/claude/template-unpacked/
# Images will be in /home/claude/template-unpacked/word/media/
# Typical contents:
#   image1.png  — Scott Kerr signature (383×129 px)
#   image2.emf  — Q2 logo (vector; use image3.png as PNG fallback)
#   image3.png  — footer banner
```
 
Read image files as binary buffers and pass them to `ImageRun` when building the new document.
 
## Node.js script pattern
 
```javascript
const { Document, Packer, Paragraph, TextRun, AlignmentType,
        ImageRun, Header, Footer } = require('docx');
const fs = require('fs');
const path = require('path');
 
// Load images (adjust paths after unpacking the template)
const sigImage    = fs.readFileSync('/home/claude/template-unpacked/word/media/image1.png');
const logoImage   = fs.readFileSync('/home/claude/template-unpacked/word/media/image3.png');
const footerImage = fs.readFileSync('/home/claude/template-unpacked/word/media/image3.png');
 
const FONT = 'Avenir LT Std 35 Light';
const SIZE = 20; // 10pt
 
function body(text) {
  // Justified body paragraph, 10pt Avenir
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    children: [new TextRun({ text, font: FONT, size: SIZE })]
  });
}
 
function left(text, bold = false) {
  // Left-aligned paragraph (date, address, re line, salutation, signature block)
  return new Paragraph({
    children: [new TextRun({ text, font: FONT, size: SIZE, bold })]
  });
}
 
function blank() {
  return new Paragraph({ children: [new TextRun({ text: '', font: FONT, size: SIZE })] });
}
 
const doc = new Document({
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 864, right: 1152, bottom: 1008, left: 1152,
                  header: 720, footer: 720, gutter: 0 }
      }
    },
    headers: {
      default: new Header({
        children: [
          new Paragraph({
            children: [
              new ImageRun({
                data: logoImage,
                transformation: { width: 60, height: 60 },
                type: 'png'
              })
            ]
          })
        ]
      })
    },
    footers: {
      default: new Footer({
        children: [
          new Paragraph({
            children: [
              new ImageRun({
                data: footerImage,
                transformation: { width: 427, height: 27 },
                type: 'png'
              })
            ]
          })
        ]
      })
    },
    children: [
      // DATE
      left('[DATE]'),
      blank(),
 
      // VENDOR ADDRESS BLOCK — use line breaks within one paragraph
      new Paragraph({
        children: [
          new TextRun({ text: '[VENDOR LEGAL NAME]', font: FONT, size: SIZE, break: 0 }),
          new TextRun({ text: '[VENDOR NOTICE ADDRESS LINE 1]', font: FONT, size: SIZE, break: 1 }),
          new TextRun({ text: 'Attention: [RECIPIENT NAME], [RECIPIENT TITLE]', font: FONT, size: SIZE, break: 1 }),
        ]
      }),
      blank(),
 
      // DELIVERY LINE
      left('Via [DELIVERY METHOD]'),
      blank(),
 
      // RE LINE — adapt based on notice type
      left('Re: [NOTICE TYPE] — [AGREEMENT TITLE] dated [AGREEMENT EFFECTIVE DATE]'),
      blank(),
 
      // SALUTATION
      left('[SALUTATION]:'),
      blank(),
 
      // BODY PARAGRAPHS — justified, adapted per notice type template
      body('[OPENING PARAGRAPH — from the applicable notice type template]'),
      blank(),
 
      body('[SERVICE END / TERMINATION EFFECTIVE DATE PARAGRAPH]'),
      blank(),
 
      body('[DATA HANDLING PARAGRAPH — when applicable]'),
      blank(),
 
      body('[CERTIFICATION DELIVERY PARAGRAPH]'),
      blank(),
 
      // CLOSING
      left('Sincerely,'),
      blank(),
 
      // SIGNATURE IMAGE
      new Paragraph({
        children: [
          new ImageRun({
            data: sigImage,
            transformation: { width: 170, height: 57 },
            type: 'png'
          })
        ]
      }),
      blank(),
 
      // SIGNATURE BLOCK
      left('Scott Kerr', true),  // bold
      left('Senior Vice President, General Counsel'),
      left('Q2 Software, Inc.'),
    ]
  }]
});
 
// Filename convention: YYYYMMDD_Q2_[VendorName]_[NoticeType].docx
const today = new Date();
const dateStr = today.toISOString().slice(0,10).replace(/-/g,'');
const vendorSlug = 'VendorName'; // replace with actual vendor name, spaces → underscores
const noticeSlug = 'Notice_Type'; // replace: Notice_of_Non-Renewal, Termination_for_Cause, etc.
const outPath = path.join('/mnt/user-data/outputs', `${dateStr}_Q2_${vendorSlug}_${noticeSlug}.docx`);
 
Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(outPath, buf);
  console.log('Saved:', outPath);
});
```
 
> **ImageRun `transformation` sizes** are in pixels at screen resolution. EMU values from the template: logo ≈ 60×60 px, signature ≈ 170×57 px, footer banner ≈ 427×27 px. Adjust if the rendered output looks wrong.
 
## Re line by notice type
 
Adapt the Re line based on the selected notice type:
- **Standard Termination / Non-Renewal:** `Re: Notice of Non-Renewal — [Agreement Title] dated [Date]`
- **Termination for Cause (breach notice):** `Re: Notice of Breach — [Agreement Title] dated [Date]`
- **Termination for Cause (termination):** `Re: Notice of Termination for Cause — [Agreement Title] dated [Date]`
- **Termination for Convenience:** `Re: Notice of Termination for Convenience — [Agreement Title] dated [Date]`
- **Confirmation of Expiration:** `Re: Confirmation of Agreement Expiration — [Agreement Title] dated [Date]`
If an order form or SOW is involved, append it: `; Order Form dated [Date]`
 
## Output filename convention
 
`YYYYMMDD_Q2_[VendorName]_[NoticeType].docx`
 
Examples:
- `20260623_Q2_Ceros_Notice_of_Non-Renewal.docx`
- `20260623_Q2_Acme_Termination_for_Cause.docx`
- `20260623_Q2_DataCorp_Termination_for_Convenience.docx`
- `20260623_Q2_WidgetCo_Confirmation_of_Expiration.docx`
## Validation
 
After generating the file:
```bash
python3 /mnt/skills/public/docx/scripts/office/validate.py /mnt/user-data/outputs/<filename>.docx
```
 
If validation fails, inspect the error and fix before presenting the file.
