---
date: 2026-07-10
source: chatgpt
title: "Word Formatting Issue"
category: "Tech Support (General)"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** I have numerous documents I’ve saved for RFP’s and bids. They’ve been properly formatted and placed on Minuteman letterhead. However, when I opened them this morning \(to use them as reference for another bid\) the formatting is way off and they’re not on the letterhead. Could there be some setting that is causing this to happen?
Help me with this ticket

**ChatGPT:** Yes. Since **all** of the documents changed rather than just one, I'd approach this as either a Word/display issue or a template issue rather than assuming the files are corrupted.

I'd walk through these in order:

1. **Determine scope**
   - Is it happening to every document or only certain ones?
   - Does it happen on another computer?
   - Are the files stored on OneDrive, SharePoint, or a network drive?

2. **Check View settings in Word**
   - Verify they're opening in **Print Layout** (View → Print Layout).
   - If they're opening in Draft or Web Layout, headers/letterhead can appear missing or different.

3. **Check if the letterhead is in the Header**
   - Double-click the top of the page.
   - If the Minuteman letterhead is in the header, see if it still exists.
   - If it's there but not visible, check whether **Different First Page** or section breaks changed.

4. **Display options**
   - File → Options → Display.
   - Ensure **Show drawings and text boxes on screen** is enabled.
   - Ensure **Print drawings created in Word** is checked.

5. **Template attachment**
   - File → Options → Add-ins → Manage Templates (or Developer → Document Template if enabled).
   - See whether the document is attached to a different template than it was originally.
   - If "Automatically update document styles" became enabled, it can dramatically change formatting.

6. **Compatibility Mode**
   - If the title bar says Compatibility Mode, save a copy as a modern `.docx` and see if formatting returns.

7. **Normal.dotm**
   - If every document suddenly looks different, the user's Normal template may have become corrupted.
   - Starting Word in Safe Mode (`winword /safe`) is a quick test.
   - If Safe Mode displays correctly, an add-in or template is likely involved.

8. **Compare with Version History**
   - If stored in SharePoint or OneDrive, check Version History.
   - This helps determine whether the file itself changed or Word is simply displaying it incorrectly.

### Questions I'd ask the user
- Did this start today?
- Did Office update recently?
- Is every document affected?
- Are they opening from SharePoint/OneDrive or a local drive?
- Is the letterhead completely gone, or is the text just shifted?
- If you open the same document on another computer, does it look normal?

### Most likely causes (in order)
1. Word opening in the wrong view or display settings.
2. Header/section formatting changed.
3. Template (`.dotx`/`.dotm`) or style update.
4. OneDrive/SharePoint sync conflict causing a bad saved version.
5. Office update or add-in affecting document rendering.

If this were an enterprise support ticket, I'd first have them **open one of the documents in Word on the web or another PC**. That immediately tells you whether you're dealing with a **document problem** or a **problem with that specific installation of Word**, which saves a lot of troubleshooting time.
