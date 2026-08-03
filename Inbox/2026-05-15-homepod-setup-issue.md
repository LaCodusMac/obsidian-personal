---
date: 2026-05-15
source: chatgpt
title: "HomePod Setup Issue"
category: "Home, Apartment & Shopping"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_00000000334c71fdb469e8cbb105e16b", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 448878, "width": 709}
Still getting this after full firmware

**ChatGPT:** Since you already:
- fully restored firmware,
- got the other 3 HomePods working,
- and this one specifically throws **Setup Failed (100)**,

this is usually one of these:

1. **Activation Lock / ownership issue**
2. **Corrupted Wi-Fi or Thread hardware**
3. **Bad NAND/storage on the HomePod**
4. Rarely: Home app/iCloud corruption

The important detail is:
> it *appears* in Home and starts setup, but dies at the final provisioning stage.

That means the firmware restore itself likely succeeded.

Try these in this exact order:

---

## 1. Remove every trace of this HomePod from Home

On iPhone:
- Home app
- Tap `...`
- Home Settings
- Look under:
  - Speakers & TVs
  - Default Room
  - Home Hubs & Bridges

If you see a ghost entry for this HomePod:
- remove it completely

Then:

### On Apple TV
Go to:
- Settings
- AirPlay & HomeKit

Remove any stale room/device references.

---

## 2. Disable Private Wi-Fi Address + iCloud Relay temporarily

This fixes a surprising number of setup 100 failures.

On iPhone:
- Settings
- Wi-Fi
- tap your network

Turn OFF temporarily:
- Private Wi-Fi Address
- Limit IP Address Tracking

If using:
- Pi-hole
- AdGuard
- custom DNS
- VLANs
- enterprise Wi-Fi
- WPA3-only

temporarily simplify to:
- normal WPA2
- 2.4/5 GHz combined
- standard DHCP/DNS

---

## 3. Force setup on a different Apple device

Use:
- another iPhone
or
- an iPad

signed into your Apple ID.

Sometimes the HomeKit token on one device gets stuck.

---

## 4. Try setup FAR away from the other HomePods

The other HomePods and Apple TVs can sometimes interfere during provisioning.

Temporarily:
- unplug the other HomePods
- maybe even unplug Apple TVs
- setup only this device alone

---

## 5. Check if it gets stuck on software personalization

If setup fails after:
- selecting room
- Siri transfer
- HomeKit sync

then the internal storage may be failing.

A bad sign is:
- repeated firmware restores
- successful restore but setup always fails identically
- long hangs before failure

That often means:
- damaged flash storage
- failed wireless chip
- board-level issue

---

## 6. Try setup on a completely different Wi-Fi network

Best test:
- hotspot from another phone

Do NOT restore from backup/home config.
Set it up as fresh.

If it works there:
- your network/HomeKit environment is the issue.

If it still fails:
- likely hardware.

---

Given everything you've already done, I’m leaning toward:
- hardware issue
OR
- hidden activation/ownership state corruption.

Especially because the other three units work fine in the same environment.

**You:** How much troubleshooting is worth it. How can I identify if it’s hardware locked

**ChatGPT:** At this point, I’d give it maybe **30–45 more minutes max** of troubleshooting before deciding whether the unit is worth keeping/returning/parting out.

Because you already:
- restored firmware,
- got other HomePods working,
- can detect this one,
- and consistently hit the same setup failure,

you’ve already eliminated a lot of the common problems.

## How to tell if it’s Activation Locked

Usually if it’s truly locked to another Apple ID, Apple is much more explicit.

You’d normally see:
- “This HomePod is linked to an Apple ID”
- “Enter the Apple ID password used to set up this HomePod”
- “Remove this accessory from Find My”

If you are **NOT** seeing that, it’s probably **not a normal Activation Lock**.

---

## Signs it’s more likely hardware

### Strong indicators:
- Full restore succeeds but setup always fails
- Fails at the same percentage every time
- Takes unusually long during “configuring”
- Gets warm/hot during setup then errors
- Appears in Home app briefly then disappears
- Can’t complete room assignment
- Error 100 repeatedly after restore

This often points to:
- failing NAND/storage
- Wi-Fi chip issue
- Thread/Bluetooth radio problem
- board communication fault

---

## One very useful test

### Does it appear in AirPlay temporarily?

Try:
- open Control Center
- AirPlay audio list

If the HomePod appears and can sometimes play audio before setup fully completes, that suggests:
- Wi-Fi works
- audio hardware works

and narrows it toward HomeKit provisioning/storage issues.

If it NEVER appears properly:
- radio hardware may be damaged.

---

## Best final test (most revealing)

Do this:

1. Unplug all other HomePods
2. Use a different iPhone/iPad
3. Use a phone hotspot Wi-Fi
4. Create a temporary new Home in Home app
5. Try setup there

If it STILL fails:
> it’s almost certainly hardware.

That test removes:
- your network
- your HomeKit config
- your Apple TV hub
- your current Home database

all at once.

---

## Realistically

Used HomePods with:
- seller resets,
- prior account weirdness,
- power issues,
- or failed updates

often die exactly like this.

Especially if they were:
- pallet/liquidation units,
- “untested,”
- or “powers on” listings.

The fact the other 3 work is actually a good sign for your environment — it isolates this unit specifically.

---

## If you want a fast decision tree

### Return/seller issue if:
- sold as fully working
- still under buyer protection

### Keep for parts if:
- you got it cheap in a lot
- power/audio still works
- cosmetic condition is good

### Continue troubleshooting ONLY if:
- it occasionally progresses farther
- behavior changes between attempts
- it works on another network/device

Otherwise you’re probably at diminishing returns.
