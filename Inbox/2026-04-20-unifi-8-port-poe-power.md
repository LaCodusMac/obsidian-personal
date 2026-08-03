---
date: 2026-04-20
source: chatgpt
title: "UniFi 8-Port PoE Power"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_00000000959871fda7821a2ff199927b", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 358567, "width": 1152}
8 port Poe UniFi switch I need power cable

**ChatGPT:** Yeah — that looks like a UniFi 8-port PoE switch (likely **US-8-60W** or **Lite 8 PoE** style). The important part: **it does NOT use a standard “PC power cable” — it needs a DC power adapter (brick).**

### 🔌 What you need
- **Voltage:** 48V (older US-8) or ~54V (Lite 8 PoE)
- **Current:** ~1–1.25A+
- **Connector:** standard barrel plug (looks like what you already have plugged in)

That matches Ubiquiti specs: these switches use an **external 48–57V DC adapter (~60W)** citeturn0search2

---

## 👍 Easiest fix (just buy replacement adapter)
Here are good options that will work:

### Direct replacement (most likely what you need)
product["turn0product1","48V Ubiquiti UniFi Switch Power Adapter (US-8-60W compatible)",{"render_as":"hero","description":"Plug-and-play replacement adapter for UniFi 8-port PoE switches using 48V DC input."}]

---

### If you have the newer Lite 8 PoE (54V version)
product["turn0product2","54V Adapter for UniFi Lite 8 PoE Switch",{"render_as":"block","description":"Correct higher-voltage adapter for USW-Lite-8-PoE models (around 54V output)."}]

---

### Alternative: power it via Ethernet (no brick)
If you don’t want a wall adapter:
product["turn0product3","Ubiquiti 60W PoE Injector",{"render_as":"block","description":"Lets you power the switch through Ethernet instead of using a DC power brick."}]

---

## ⚠️ Important (don’t skip this)
Before buying:
- Look at the **label on the bottom** of your switch  
- Confirm model:
  - **US-8 / US-8-60W → 48V**
  - **USW-Lite-8-PoE → 54V**

Using the wrong voltage = won’t power on or could damage it.

---

## 💡 Quick tip from your setup
That cable in your photo looks like the **DC barrel already**, meaning:
- You’re missing the **power brick (wall adapter)** that feeds that cable

---

If you want, send me the **bottom label pic** and I’ll tell you *exactly* which one to buy so you don’t guess.
