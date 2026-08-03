---
date: 2026-04-30
source: chatgpt
title: "Outlook Compose Error Fix"
category: "Tech Support (General)"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_00000000a5f4722f8f12285475396bc0", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 240316, "width": 709}

**ChatGPT:** Yeah this is a classic **Outlook (especially “New Outlook” / OWA) compose error** — that red banner “**An internal error has occurred**” usually isn’t super descriptive, but there are a few common causes.

From your screenshot:
- Sending from **lstepas@minutemanst.com**
- Internal message
- Error appears right in compose window before sending

### Most likely causes (ranked for your situation)

#### 1. 🔐 Account / permission issue (VERY common)
If this user:
- Recently changed password  
- Has mailbox permission changes  
- Is using shared mailbox / delegated send  

👉 Outlook can fail silently like this.

**Fix:**
- Sign out of Outlook completely → sign back in  
- Or remove/re-add the account  
- If shared mailbox → confirm **Send As / Send on Behalf** still exists in M365 admin

---

#### 2. 🌐 “New Outlook” bug (this happens a LOT)
You mentioned earlier you're using **new Outlook** — it’s still kinda buggy.

**Quick test:**
- Open same mailbox in **Outlook Web (OWA)**  
- Or switch back to **Classic Outlook**

If it works there → not a policy issue, just client bug

---

#### 3. 📎 Hidden bad attachment / signature
Even if you don’t see it:
- Corrupt signature image
- Broken embedded object

**Fix:**
- Start a **brand new email (don’t reply/forward)**
- Remove signature
- Try sending just plain text

---

#### 4. 🛡️ Defender / transport rule interference
Since you were dealing with filtering earlier:

Possible triggers:
- Language filter
- DLP / transport rule
- Anti-spam policies

BUT → those usually bounce **after sending**, not during compose

So this is **less likely**, but still possible if:
- Add-ins are inspecting content live

---

#### 5. 🔌 Add-in issue (especially in New Outlook)
Things like:
- CRM plugins
- Email tracking tools

**Fix:**
- Disable add-ins temporarily
- Or try in web browser → if it works, it’s an add-in

---

### Fastest way to isolate (do this in order)

1. **Try sending in Outlook Web**
2. **Send a blank test email**
3. **Remove signature**
4. **Log out / back in**
5. **Try different sender (if shared mailbox)**

---

### If I had to bet (based on your environment)
👉 It’s either:
- New Outlook bug  
- OR permissions on that mailbox/sender

---

If you want, send me:
- Whether it fails in OWA
- If it’s a shared mailbox or primary
- If others have the same issue

I’ll pinpoint it fast instead of guessing.
