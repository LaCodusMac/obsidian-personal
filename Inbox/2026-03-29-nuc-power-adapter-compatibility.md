---
date: 2026-03-29
source: chatgpt
title: "NUC Power Adapter Compatibility"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_00000000df60722f8f10d2d92f6df4eb", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 444192, "width": 1152}
Can I use this for my NUC

**ChatGPT:** Short answer: **probably not ideal, but maybe — depends on your NUC model.**

### What you have
That ASUS adapter outputs:
- **20V**
- **6.0A (120W max)**

### What most Intel NUCs need
Most NUCs (including your **NUC8i7BEH** and **NUC10i5FNH**) typically require:
- **19V**
- Around **3–6A (65W–120W depending on load)**

---

### The key issue: 20V vs 19V
- 20V is **slightly higher than spec**
- Many devices tolerate ±5%, and 20V is just outside that range (~+5.2%)
- Some NUCs will run fine… but **it’s not guaranteed safe long-term**

---

### Other things that matter (VERY important)
- **Barrel plug size** (NUCs usually use **5.5mm outer / 2.5mm inner**)
- **Polarity** (center positive — yours likely is, but worth confirming)

---

### My recommendation (based on your setup)
Given you’re running:
- Plex server
- Always-on workloads
- Multiple devices

👉 **Don’t risk it.**

Use:
- A proper **19V NUC power adapter (65W or 90W+)**

---

### When it *might* be okay
You could test it *temporarily* if:
- Plug fits perfectly
- NUC boots normally
- No overheating or instability

But I wouldn’t run your home lab on it long-term.

---

### Bottom line
- ✔️ Voltage: **close but not ideal**
- ✔️ Wattage: **more than enough**
- ❌ Recommendation: **Get the correct 19V adapter**

---

If you want, send me the exact NUC model and I’ll link you the **perfect replacement (cheap and safe)** 👍

**You:** What’s a good replacement

**ChatGPT:** You want something **19V, center-positive, 5.5mm x 2.5mm barrel**, and ideally **90W** for your NUCs (safe headroom for Plex + load). citeturn0search4  

Here are the **best options right now** (ranked for your setup):

---

## 🔥 Best overall (what I’d personally buy)
product["turn0product5","Onerbl 19V 4.74A 90W Intel NUC Adapter",{"render_as":"hero","description":"Perfect match for NUC8/NUC10 with safe wattage headroom for Plex and always-on use."}]

**Why this is the move:**
- 19V ✅ (exact spec)
- 90W ✅ (plenty for your NUC10 under load)
- Correct plug size ✅  
- Cheap + widely used replacement

👉 This is basically your **plug-and-forget option**

---

## 💰 Cheapest option (still works)
product["turn0product3","Onerbl 19V 4.74A 90W Adapter (budget)",{"render_as":"block","description":"Ultra cheap 90W option that still meets NUC requirements."}]

- Same specs as above
- Just less brand confidence / QA

👉 Good if you just want something quick and cheap

---

## 🧊 Lower power (fine for light use)
product["turn0product4","Onerbl 19V 3.43A 65W Adapter",{"render_as":"block","description":"Lower watt option for lighter workloads or secondary NUCs."}]

- Works for:
  - Idle/light usage
  - Pi-hole / Home Assistant boxes
- Not ideal for:
  - Plex transcoding
  - Heavy CPU bursts

---

## ⚡ Overkill (but solid)
product["turn0product9","FITE-ON 19V 120W Power Adapter",{"render_as":"block","description":"High headroom option for max stability and future upgrades."}]

- More wattage than needed
- Great if you:
  - Add drives
  - Push CPU hard
  - Want zero power bottleneck

---

## 🧠 Quick recommendation for YOU
Based on your setup (Plex + homelab + always-on):

👉 **Get a 90W 19V adapter (like the first one)**  
That’s the sweet spot.

---

## 🚫 What to avoid
- 20V adapters (like the one you showed)
- Random laptop chargers with wrong tip size
- Anything under 65W

---

## Bottom line
- **Best value:** 90W 19V adapter  
- **Minimum:** 65W (only for light use)  
- **Future-proof:** 120W if you want zero worries  

---

If you want, I can match **one adapter per NUC in your setup** so you standardize everything cleanly.
