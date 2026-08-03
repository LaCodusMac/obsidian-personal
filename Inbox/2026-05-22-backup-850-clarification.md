---
date: 2026-05-22
source: chatgpt
title: "Backup 850 Clarification"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Back ups 850

**ChatGPT:** What do you mean by “Back ups 850”?  
Do you mean:

- a backup power supply / UPS rated at 850VA,
- backup reps/sets in lifting,
- backup storage size,
- or something else?

**You:** Backup power supply

**ChatGPT:** If you mean an 850VA UPS (battery backup power supply), that’s usually enough for:

- a modem/router
- small home networking gear
- an Intel NUC like your entity["product","Intel NUC10i5FNH","Mini PC"]
- Synology NAS
- maybe one monitor

It is usually **not** enough for:
- gaming PCs with GPUs
- space heaters
- full AV setups
- laser printers

For your homelab/Home Assistant/Plex setup, an 850VA unit is actually a pretty reasonable starting point.

Good options:

- entity["product","APC Back-UPS 850VA","UPS battery backup"] — very common, reliable, easy battery replacements
- entity["product","CyberPower CP850PFCLCD","UPS battery backup"] — better for modern active PFC power supplies
- entity["product","APC BX850M","UPS battery backup"] — compact/simple

For your setup specifically, I’d prioritize:
1. modem/router
2. switch
3. NAS
4. primary NUC running Plex/Home Assistant

That gives you graceful shutdown protection and keeps the network alive during short outages. An 850VA UPS would probably give roughly:
- 30–60+ minutes for networking-only
- 10–25 minutes with NAS + NUCs attached

Avoid plugging these into battery backup outlets:
- printers
- speakers/subwoofers
- large TVs
- power strips with surge filtering chained together

If you want, I can also help you:
- size the UPS properly for your exact gear,
- estimate runtime,
- or recommend the best one under a budget.

**You:** APC Back-UPS 850VA — very common, reliable, easy battery replacements

**ChatGPT:** image_group{"layout":"carousel","aspect_ratio":"1:1","query":["APC Back-UPS 850VA BX850M","APC Back-UPS 850VA rear outlets","APC Back-UPS 850VA home office setup","APC Back-UPS 850VA LCD display"],"num_per_query":1}

The entity["product","APC BX850M","UPS battery backup"] is a solid choice for what you’re doing.

Why it fits your setup well:
- Reliable for homelab/network gear
- Replaceable batteries
- Automatic voltage regulation (helps with brownouts/sags)
- USB connection for graceful shutdowns
- Quiet unless on battery
- Compact enough for an apartment or desk setup

For your gear, it should comfortably handle:
- modem/router
- switch
- entity["product","Intel NUC10i5FNH","Mini PC"]
- Synology NAS
- maybe one monitor

A realistic expectation:
- networking only → potentially over an hour
- NAS + NUC + networking → usually around 10–20+ minutes depending on load

One important thing:
If you eventually add:
- a gaming PC,
- GPU AI box,
- or larger server hardware,

you’ll probably want to move up to a 1500VA model later.

Also:
APC units integrate nicely with:
- entity["software","Home Assistant","Home automation platform"]
- entity["software","Proxmox VE","Virtualization platform"]
- Synology DSM
- Linux via apcupsd/NUT

So you can automate clean shutdowns during outages.

**You:** {"asset_pointer": "sediment://file_00000000e6bc71f597ab3cc62bb55900", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 556966, "width": 1152}

**ChatGPT:** Yep — that’s the entity["product","APC Back-UPS 850VA","UPS battery backup"].

From the picture:
- Green power light = normal operation
- No warning lights/alarm visible
- Looks like you’re using the battery-backed outlets correctly
- Dust level is normal but worth cleaning eventually for airflow

A few recommendations for your setup specifically:

- Keep the UPS slightly away from carpet if possible  
  Carpet traps heat. Even a small wood board/platform underneath helps.

- Don’t overload it with high-draw devices  
  Good:
  - NUCs
  - modem/router
  - switch
  - NAS

  Avoid:
  - gaming desktop
  - heater
  - printer
  - subwoofer

- Use the USB cable to a server/NUC  
  That lets:
  - entity["software","Home Assistant","Home automation platform"]
  - Linux
  - Synology DSM
  trigger graceful shutdowns during outages.

- Test it once
  With your equipment running:
  1. save work
  2. unplug UPS from wall
  3. confirm devices stay on
  4. plug back in after ~30 seconds

If you want, I can also help you:
- estimate your current runtime from the gear attached,
- identify which outlets are battery vs surge-only,
- or help connect it into Home Assistant/Proxmox monitoring.

**You:** I need to get notifications

**ChatGPT:** You can get outage + low battery notifications pretty easily with that UPS.

Best option for your setup is probably:

- UPS USB → your Linux/Proxmox/Home Assistant machine
- Use NUT (Network UPS Tools)
- Send notifications to:
  - Home Assistant app
  - Discord
  - mobile push
  - email
  - Telegram

Since you already run entity["software","Home Assistant","Home automation platform"] and Linux systems, this is actually a great fit.

Basic setup flow:

### 1. Connect UPS USB
Plug the UPS USB cable into:
- your primary NUC
- or Synology NAS
- or Proxmox host

### 2. Install UPS monitoring
On Ubuntu/Linux:
```bash
sudo apt update
sudo apt install nut
```

Or easier:
- use the Home Assistant NUT integration
- or Synology UPS Server if NAS-connected

### 3. Example alerts
You can trigger alerts for:
- power outage
- restored power
- battery below 50%
- runtime remaining under 5 minutes
- automatic shutdown initiated

### 4. Home Assistant notification example
Example automation:
```yaml
alias: UPS On Battery
trigger:
  - platform: state
    entity_id: binary_sensor.ups_status
    to: "on"
action:
  - service: notify.mobile_app_iphone
    data:
      title: "UPS Alert"
      message: "Power outage detected. Running on battery."
```

You can also build a dashboard showing:
- battery %
- estimated runtime
- load %
- voltage

Honestly this is one of the best “first real infrastructure” upgrades for a homelab because:
- you protect Plex/NAS corruption,
- get outage awareness,
- and can automate clean shutdowns.
