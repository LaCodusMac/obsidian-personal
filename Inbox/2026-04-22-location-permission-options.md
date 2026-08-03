---
date: 2026-04-22
source: chatgpt
title: "Location Permission Options"
category: "Tech Support (General)"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_0000000002e471f78742889db91a95aa", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 619144, "width": 691}

**ChatGPT:** That popup is just Google asking for permission to use your location so it can show nearby results (like local “Wally’s” spots).

Here’s what each option actually means:

### 🔹 **Precise (Exact location)**
- Uses your GPS/location data
- Gives **very accurate nearby results**
- Best if you’re trying to find something close (restaurants, stores, etc.)

### 🔹 **Approximate (Neighborhood)**
- Uses a rough location (like your general area)
- Still shows nearby results, just less precise
- Good middle ground for privacy

### 🔹 **Continue not allowing**
- Google won’t use your location at all
- Results may be **less relevant** (you’ll see random locations, like that Australia result in your screenshot)

### 🔹 **Allow this time**
- One-time permission (it’ll ask again later)

---

### 👍 What you should pick
- If you're just trying to find a local place → **Allow this time (Precise)**
- If you care about privacy → **Approximate**
- If you don’t want tracking at all → **Continue not allowing**

---

If you're seeing weird results (like places in other countries), it’s because location is blocked — so enabling it (even temporarily) will fix that immediately.

If you want, I can show you how to make it **always allow** or **completely block it system-wide** on your phone.

**You:** Every time I allow it and refresh it changes my location from New Hampshire to Australia Melbourne. I changed it to allow precise location in settings and tried it with WiFi on/off

**ChatGPT:** Yeah—that’s not normal. If it keeps snapping to **Melbourne, Australia**, something is overriding your real location. This usually comes down to one of a few things:

---

## 🚨 Most likely causes (based on what you described)

### 1. **VPN is on (even if you forgot about it)**
This is the #1 cause of exactly what you're seeing.

- Apps like:
  - NordVPN  
  - ExpressVPN  
  - Proton VPN  
  - Even some antivirus apps  
- Can route your traffic through **Australia servers**

👉 Check:
- Settings → **Connections / Network → VPN**
- Or look for a **key icon 🔑** in your status bar (I actually see one in your screenshot 👀)

If that’s on → **turn it off** and refresh Google

---

### 2. **Private DNS or custom DNS**
You mentioned you recently had DNS issues — this is a big clue.

If you're using:
- Custom DNS (like AdGuard, NextDNS, Pi-hole, etc.)
- Or your UniFi setup changed DNS routing

Google might think you're somewhere else.

👉 Check:
- Settings → **Connections → Private DNS**
- Set it to:
  - **Automatic** or **Off**

---

### 3. **Google account location / region mismatch**
Sometimes Google locks onto a region based on account activity.

👉 Try:
- Scroll to bottom of Google search page
- Check location (it’ll probably say Melbourne)
- Tap it → update location manually

Or go to:
- Google → Settings → **Search settings → Region**

---

### 4. **Browser/app glitch (less likely but happens)**
If Chrome is bugging out:

👉 Try:
- Clear Chrome cache:
  - Settings → Apps → Chrome → Storage → **Clear Cache**
- Or test in:
  - Incognito mode
  - Another browser (like Firefox)

---

## 🔍 What I think is happening (based on your setup)
You:
- Run UniFi networking
- Just fixed DNS issues
- Might be using custom routing or VPN at some level

👉 **Most likely culprit: VPN or DNS routing through Australia**

---

## ✅ Quick fix checklist (do this in order)

1. Turn OFF any VPN  
2. Set **Private DNS → Automatic**  
3. Toggle **Location OFF → ON**  
4. Refresh Google  
5. Try “Allow this time (Precise)” again  

---

If it still happens after that, tell me:
- What phone you’re using (looks like Samsung?)
- If you have anything like AdGuard / Pi-hole / UniFi DNS filtering on

I can help you trace it exactly — this is fixable, just needs the right knob turned.

**You:** TotalAV

**ChatGPT:** Yep—that’s your problem. **entity["software","TotalAV","antivirus software"]** is almost definitely causing this.

TotalAV includes:
- a **VPN / “Safe Browsing VPN”**
- sometimes a **WebShield / DNS filter**

Those can route your traffic through random countries — and Australia (Melbourne) is a common endpoint.

---

## 🔧 Fix it (fast)

### Option 1 — Turn off the VPN inside TotalAV
1. Open **TotalAV**
2. Look for:
   - **VPN**
   - or “Secure Browsing”
3. Toggle it **OFF**

👉 Then refresh Google — your location should snap back to New Hampshire immediately.

---

### Option 2 — Disable TotalAV completely (quick test)
1. Go to **Settings → Apps → TotalAV**
2. Force Stop
3. Refresh Google

If it fixes it → you’ve confirmed 100%

---

### Option 3 — Remove it (honest advice)
I’m gonna be straight with you:

- On Android, apps like TotalAV are **more trouble than they’re worth**
- They mess with:
  - DNS
  - VPN routing
  - Web traffic (like what you're seeing)

👉 Your phone already has:
- Google Play Protect
- Built-in security

**Most IT people don’t run apps like TotalAV on phones at all**

---

## 💡 Why it showed Melbourne specifically
TotalAV likely:
- Auto-connected to a **VPN exit node in Australia**
- Google saw that IP → assumed you’re there

Even with **precise location ON**, Google sometimes prioritizes IP location if it conflicts.

---

## ✅ What I’d do (best setup)
- Uninstall TotalAV  
- Keep location ON (Precise)  
- Leave DNS on Automatic  

---

If you want, I can suggest a **clean, no-BS mobile security setup** that won’t break your networking (especially with your UniFi + homelab setup).

**You:** Is totalav safe(this is all for my aun)

**ChatGPT:** Short answer: **Yes, TotalAV is “safe” in the sense that it’s not malware** — but that doesn’t mean it’s a good choice, especially for your aunt.

Here’s the honest breakdown:

---

## ✅ The good
- It **does detect viruses and malware** reasonably well  
- Independent tests show **high detection rates (around ~98–99%)** citeturn0search0  
- It’s **easy to use**, which is nice for non-tech users citeturn0search4  

👉 So it *does work* as antivirus.

---

## ⚠️ The problems (this is the important part)

### 1. Aggressive upselling & pricing
- Cheap first year → **expensive renewal later** citeturn0search0  
- Many users complain about **unexpected charges or auto-renewals** citeturn0search1turn0search3  

---

### 2. Extra features cause issues (what YOU just experienced)
- Includes:
  - VPN  
  - Web filtering / DNS  
- These can:
  - Change location (like your Australia issue)
  - Break browsing or apps  

👉 This is exactly what happened to you.

---

### 3. Not top-tier protection
- It’s considered **“standard” protection**, not best-in-class citeturn0search0  
- Missing things like:
  - Built-in firewall  
  - More advanced detection features citeturn0search4  

---

### 4. Overkill (especially for phones)
On Android:
- You already have:
  - Google Play Protect  
  - Built-in security  
- Antivirus apps often just:
  - Slow things down  
  - Add unnecessary layers  

---

## 🧠 My recommendation (especially for your aunt)

### 👍 Best option (simple & safe)
- **Uninstall TotalAV**
- Leave:
  - Phone updated  
  - Play Protect ON  

👉 That’s honestly the cleanest, least-problem setup

---

### 👍 If she *really* wants antivirus
Go with something more stable like:
- Bitdefender  
- Norton  

(less intrusive, fewer weird issues)

---

## 💬 Real talk (IT perspective)
TotalAV isn’t a virus or scam…  
But it sits in that category of:
> “Works, but causes more problems than it solves”

And your location bug is a perfect example of that.

---

## ✅ Bottom line
- **Safe?** → Yes  
- **Good choice?** → Not really  
- **Would I put it on a family member’s phone?** → No  

---

If you want, tell me what device your aunt uses (Android/iPhone/PC), and I’ll give you a **super simple, foolproof setup** for her that won’t break anything like this.
