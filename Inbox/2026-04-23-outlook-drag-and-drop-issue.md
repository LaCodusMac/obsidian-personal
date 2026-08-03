---
date: 2026-04-23
source: chatgpt
title: "Outlook Drag-and-Drop Issue"
category: "Tech Support (General)"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Hi, Me again --   quick question, in my old outlook I was able to drag attachments into CW --  now I am not able to do that from my email, I have to save the item first... is this correct ? - help me troubleshoot

**ChatGPT:** Short answer: **No — that’s not “how it’s supposed to be.”** You *should* still be able to drag attachments, but the behavior depends on which Outlook + ConnectWise combo you’re using. Let’s narrow it down.

---

## 🔍 First — what changed?
There are two big Outlook differences that break drag-and-drop:

### 1. **New Outlook vs Classic Outlook**
If you’re using the newer version of entity["software","Microsoft Outlook","email client"] (the one that looks more like the web app), drag-and-drop is **limited or broken** in a lot of cases.

👉 In **New Outlook**:
- Attachments are sandboxed (web-based)
- Dragging directly into apps like entity["software","ConnectWise Manage","PSA software"] often **does NOT work**

👉 In **Classic Outlook (desktop)**:
- Drag/drop attachments → CW tickets **should work fine**

---

## 🧪 Quick checks (do these in order)

### ✅ 1. Are you in “New Outlook”?
- Look top right in Outlook
- If you see a toggle that says **“New Outlook” is ON**

👉 Try switching it OFF → go back to classic  
Then test drag + drop again

---

### ✅ 2. Are you dragging the *attachment* or the *email*?
This matters more than it should:

- Dragging the **email itself** → usually works
- Dragging the **attachment preview icon** → may fail in New Outlook

👉 Workaround:
- Open the email
- Drag from the attachment *bar* (not preview pane)

---

### ✅ 3. Are you using the CW thick client or browser?
- If you’re dragging into **browser-based CW**
  - Some browsers block file object transfer from Outlook

👉 Try:
- Different browser (Chrome vs Edge)
- Or drag into **File Explorer first → then into CW**

---

### ✅ 4. Permissions / admin weirdness
Less common but real:
- Running Outlook as admin but browser not (or vice versa) breaks drag/drop

👉 Fix:
- Make sure both apps run at same privilege level

---

## 🛠️ Known Workarounds (if it’s the new Outlook issue)

If you're stuck on New Outlook:

- Drag email → Desktop → then into CW
- Or use:
  - “Save All Attachments”
  - Copy/paste (sometimes works for small files)
- Or revert to Classic Outlook (best fix IMO)

---

## 💡 Real-world IT takeaway (based on your setup)
Given your help desk background, this is almost certainly:

> **New Outlook + web-based ConnectWise = drag/drop limitation**

Microsoft basically rebuilt Outlook as a web wrapper, and it **breaks old COM-style integrations** like this.

---

## 👍 What I’d do in your shoes
- If this is daily workflow → **go back to Classic Outlook**
- If you *have* to stay on new:
  - Accept the save-first workflow OR
  - Build a quick temp folder habit (fast enough once you get used to it)

---

If you want, tell me:
- Which Outlook version you’re on (screenshot helps)
- Whether CW is browser or desktop

I can give you a **exact fix tailored to your setup** instead of generic troubleshooting.

**You:** We need to use outlook new

**ChatGPT:** Got it — if you’re **locked into New Outlook**, then what you’re seeing is expected behavior, not a misconfiguration.

### ⚠️ The key point
In **entity["software","Microsoft Outlook","email client"] (New Outlook)**, Microsoft changed how attachments are handled. Because it runs more like a web app, attachments are **sandboxed**, and that breaks classic drag-and-drop workflows into tools like **entity["software","ConnectWise Manage","PSA software"]**.

So yes:
> ❗ You generally *cannot reliably drag attachments directly from New Outlook into ConnectWise anymore.*

---

## 🧠 What’s actually happening
New Outlook:
- Stores attachments in a protected web layer (not exposed as a file handle)
- Doesn’t expose the same “real file path” Windows apps expect
- Therefore drag/drop into external apps often fails or forces a save step

That’s why you now have to:
> Save → then upload → instead of drag directly

---

## 🛠️ Best working options (New Outlook compatible)

### ✅ Option 1 — Save + Drag from File Explorer (fastest)
1. Click attachment in email
2. **Save As** (or “Download all”)
3. Drag from File Explorer into ConnectWise

👉 This is the most reliable workaround

---

### ✅ Option 2 — “Drag email instead of attachment”
Sometimes works better than dragging the file itself:
- Drag the **entire email message** into ConnectWise
- Attachments may come along depending on CW config

---

### ✅ Option 3 — Use Copy/Paste (surprisingly works in some cases)
- Copy attachment in Outlook
- Paste into CW ticket attachment area

(Not consistent, but worth trying)

---

### ⚙️ Option 4 — Check ConnectWise upload behavior
In some setups, ConnectWise:
- Only accepts files via upload button (not OS drag events from sandboxed apps)
- Especially true in browser-based CW

---

## 💡 Reality check (important)
This isn’t something you’re “doing wrong.” It’s a **platform limitation**:

- Old Outlook = Windows-native integration → drag/drop works
- New Outlook = web-based container → restricted file access

Microsoft intentionally tightened this for security.

---

## 👍 Practical recommendation for your workflow
Since you’re in IT/help desk style workflows:

**Fastest stable method is:**
> Attachment → Save → Drag from Explorer → CW

It’s one extra step, but it’s the least fragile under New Outlook.

---

If you want, I can help you streamline it further (like a 2-click “save all attachments to CW temp folder” workflow or Power Automate shortcut).
