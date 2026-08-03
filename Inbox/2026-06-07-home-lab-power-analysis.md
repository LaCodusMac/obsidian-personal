---
date: 2026-06-07
source: chatgpt
title: "Home Lab Power Analysis"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_0000000066f0722f93057ac66b6a7b36", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 205951, "width": 709}

**ChatGPT:** Your Home Lab smart plug is currently reporting:

- **Power:** 149.3 W
- **Voltage:** 120.4 V
- **Current:** 1.41 A
- **Power Factor:** 88%
- **Total Energy Used:** 107.205 kWh

A few observations:

### The numbers don't quite agree
At 120.4V and 1.41A, apparent power would be about:

120.4 × 1.41 ≈ **170 VA**

With an 88% power factor:

170 × 0.88 ≈ **150 W**

That matches the **149.3W** reading almost perfectly.

So the plug appears to be measuring correctly.

### What is using ~150W?
Based on your homelab inventory, 150W is very reasonable for:

- NUC10 running Docker/Plex
- NUC8 running Proxmox + HA
- Synology DS423
- UniFi gear (UXG Max, switch, AP, Cloud Key)
- Raspberry Pis

That's actually a pretty efficient homelab.

### Cost estimate
If it averaged 150W 24/7:

- 0.15 kW × 24 hr = **3.6 kWh/day**
- ~108 kWh/month

At:
- $0.20/kWh → ~$22/month
- $0.25/kWh → ~$27/month
- $0.30/kWh → ~$32/month

### One thing that looks odd
The screenshot shows:
- **Power = 149.3W**
- **Instantaneous demand = 0.3W**

Those should normally be similar. That often happens when:
- One sensor hasn't updated yet
- Home Assistant is pulling different Zigbee attributes
- The device reports cumulative demand and real-time power separately

If you tell me:
- What exact smart plug this is (Zooz, ThirdReality, Sonoff, etc.)
- What is plugged into it

I can help determine whether that **0.3W instantaneous demand** reading is a reporting issue or a configuration problem in Zigbee2MQTT/Home Assistant.

**You:** Thirdreality with whole home lab routed through

**ChatGPT:** Yep — **~149W for your whole homelab is totally believable and pretty good**.

At 24/7:

**149W ≈ 3.58 kWh/day ≈ 107 kWh/month**

That matches your plug’s **107.205 kWh** if it has been tracking around a month.

Rough monthly cost:

- **$0.20/kWh:** ~$21/month
- **$0.25/kWh:** ~$27/month
- **$0.30/kWh:** ~$32/month

For your setup, the main draw is probably:

**Synology + UniFi PoE switch/AP/Cloud Key + NUCs + modem/router + Raspberry Pis.**

One caution: make sure the **ThirdReality plug is rated for the load**. At **1.41A**, you are well under a normal 15A smart plug limit, so electrically it’s fine. But I’d avoid plugging a UPS or power strip with heaters/fans/extra gear into it later unless you keep checking the amps.
