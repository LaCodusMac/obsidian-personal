---
date: 2026-06-07
source: chatgpt
title: "Wi-Fi Network Detection Issue"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_00000000462c722f9a6fd739e67202ca", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 384684, "width": 709}

**ChatGPT:** This looks like the Wi-Fi setup screen for a device (possibly a smart lock, HomePod accessory, camera, or IoT device) that can only see certain types of Wi-Fi networks.

The message **"No Wi-Fi Networks Detected"** usually means one of these:

1. **Your phone is connected to a 5 GHz-only network**
   - Many smart home devices only support 2.4 GHz.
   - If your UniFi setup uses a combined SSID, the device may not be seeing the 2.4 GHz radio.

2. **The IoT network is hidden**
   - Hidden SSIDs often don't appear in setup apps.
   - You can use "Join Hidden Network" if that's the case.

3. **WPA3-only security**
   - Some older IoT devices cannot join WPA3.
   - In UniFi, set the IoT SSID to **WPA2/WPA3 Transition** or **WPA2 Only**.

4. **The device is too far from the AP**
   - During setup, move within a few feet of your UniFi AP.

5. **5 GHz or 6 GHz only SSID**
   - The device may require 2.4 GHz.

Since you're running UniFi with separate VLANs and IoT devices, I'd check:

**UniFi → Settings → WiFi → Your IoT SSID**
- 2.4 GHz enabled ✅
- WPA2 or WPA2/WPA3 Transition ✅
- SSID broadcast enabled ✅
- Not restricted to 5 GHz only ✅

What device are you setting up? (SwitchBot Lock Hub, HomePod, camera, etc.) A screenshot of the previous setup screen or the device model would let me tell you the exact fix.

**You:** I have 5 other kl125 devices on this network

**ChatGPT:** If you already have **5 other TP-Link Kasa KL125 bulbs on the same Wi-Fi**, then the problem is probably **not your Wi-Fi configuration**.

More likely causes:

- This specific bulb didn't properly enter pairing mode.
  - Turn it off/on 3 times quickly.
  - It should start blinking rapidly.
  - If not, factory reset it again.

- The bulb is in the wrong setup mode.
  - Kasa bulbs have a fast-blink setup mode and sometimes a slow-blink AP mode.
  - Try resetting until it is rapidly blinking.

- The bulb's Wi-Fi radio is stuck.
  - Leave it powered off for 30 seconds.
  - Reset and try again.

- The bulb is already associated with another network/account.
  - Factory reset (typically 5 on/off cycles) and confirm the blinking pattern.

A few questions:

1. Is this a **brand new KL125** or one you've used before?
2. During setup, does your iPhone see a temporary Wi-Fi network like **TP-LINK_Smart Bulb_XXXX**?
3. Are you using the **Kasa app** or trying to add it directly through **Home Assistant/HomeKit**?

Since your other KL125s work, I'm leaning toward **the bulb not actually being in pairing mode** or **a defective bulb**, rather than a UniFi or network issue.

**You:** Used before

**ChatGPT:** Since it's a **used KL125 that was previously working**, I'd focus on the bulb itself rather than UniFi.

Try this sequence:

1. Remove power from the bulb for 30 seconds.
2. Factory reset it:
   - Turn it on and off **5 times** (about 1 second each).
   - The bulb should start flashing.
3. In your phone's Wi-Fi settings, look for a network similar to:
   - `TP-LINK_Smart Bulb_XXXX`

If you **don't see the TP-Link setup network at all**, even standing next to the bulb, that's a strong sign the bulb's Wi-Fi module isn't entering pairing mode.

A few things I've seen with KL125s:
- If they were previously configured, sometimes they need **two resets in a row** before they fully forget the old network.
- If the bulb flashes but never creates the TP-Link setup SSID, the internal Wi-Fi radio may have failed.
- If the bulb creates the setup SSID but Kasa can't find your Wi-Fi, then we'd look at the UniFi settings.

Can you tell me:
- Is the bulb currently **blinking rapidly**, **blinking slowly**, or **solid on**?
- Do you see any `TP-LINK_*` Wi-Fi network from your iPhone when standing next to it?

That will narrow it down quickly.

**You:** {"asset_pointer": "sediment://file_000000002f78720ca35e6f74218a1c9f", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 410503, "width": 709}
{"asset_pointer": "sediment://file_00000000e79471f5bb801097dce528c2", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 640866, "width": 709}

**ChatGPT:** This is actually a very useful clue.

Your iPhone can see and join **TP-LINK_Smart Bulb_D9E8**, so:

✅ The bulb's Wi-Fi radio is working  
✅ The bulb is in pairing mode  
✅ The reset succeeded

The problem is happening on the **next step**, when the bulb scans for nearby Wi-Fi networks and reports **"No Wi-Fi Networks Detected."**

Since you have **5 other KL125s already working on the same UniFi network**, I'd check these UniFi-specific settings:

### 1. Is your IoT SSID hidden?
The bulb setup screen shows a **"Join Hidden Network"** button. If your IoT SSID is hidden, the bulb may not find it during scanning.

Try:
- Make the SSID visible temporarily
- Rescan

### 2. Is this SSID 5 GHz only?
KL125 bulbs require **2.4 GHz**.

In UniFi:
- Settings → WiFi → Your IoT SSID
- Verify **2.4 GHz is enabled**

### 3. WPA3 enabled?
Some Kasa firmware versions struggle with WPA3.

Temporarily set:
- WPA2 only
or
- WPA2/WPA3 Transition

### 4. Is AP Isolation enabled?
If you have an IoT VLAN with aggressive isolation settings, the setup process can fail.

### Quick test
Since you already have a working environment:

**Create a temporary Wi-Fi network:**
- SSID: `KasaTest`
- 2.4 GHz only
- WPA2 only
- No VLAN restrictions

Then try adding the bulb.

If it immediately sees `KasaTest`, we know the bulb is fine and something about the main IoT SSID is preventing discovery.

Can you tell me:
- What SSID are the other 5 KL125s connected to?
- Is it a dedicated IoT VLAN SSID?
- Is that SSID hidden or visible?

Since the other KL125s are already working, my bet is on a UniFi setting that changed after those bulbs were originally added, not a bad bulb.

**You:** Not hidden, 2.4 and 5,     WPA2/WPA3 , no IOT VOAN

**ChatGPT:** Given that:

- Other KL125s work on this exact network
- SSID is visible
- 2.4 GHz is enabled
- No IoT VLAN
- The bulb creates its own setup network successfully

I don't think the issue is your UniFi config.

The weird part is that the bulb is saying **"No Wi-Fi Networks Detected"** while your phone can clearly see Wi-Fi networks. That means the bulb's internal scan is failing.

A few things I'd try:

### 1. Temporarily disable WPA3
Even though other bulbs work, they may have joined before a firmware or controller change.

Set the SSID to:
- **WPA2 Only**

Then reset the bulb again and try pairing.

### 2. Disable Band Steering / BSS Transition temporarily
In UniFi, if enabled on that SSID:
- Band Steering = Off
- BSS Transition = Off
- Fast Roaming = Off

Some older IoT devices hate these features.

### 3. Try a phone hotspot test
Create a hotspot on another phone:
- 2.4 GHz
- WPA2

Then see if the bulb can detect that network.

Results:
- If it sees the hotspot → UniFi setting issue.
- If it still sees **zero networks** → bulb hardware/firmware issue.

### 4. Check if it's a stale firmware state
Since it's a used bulb:
- Reset it twice in a row.
- Remove power for a minute.
- Reset again.

I've seen Kasa bulbs get into a state where they broadcast the TP-LINK setup SSID but fail to scan for external networks.

### My current suspicion
About **70–80% bulb issue, 20–30% UniFi feature incompatibility**.

The fastest way to prove it is the hotspot test. If the bulb can't see a phone hotspot sitting 3 feet away, I'd consider that KL125 defective and replace it. The fact that five identical bulbs already work on your network is a strong indicator that the network itself is not the root cause.

**You:** How to really reset it, if it’s broke it’s just broke?

**ChatGPT:** For a KL125, the "real" factory reset is:

1. Turn the bulb **on for ~1 second**
2. Turn it **off for ~1 second**
3. Repeat **5 times**
4. Leave it **on** after the fifth cycle

The bulb should start blinking.

There are actually two reset modes on many Kasa bulbs:

- **Soft reset**: keeps some settings and enters setup mode.
- **Factory reset**: wipes Wi-Fi/account information completely.

If you're unsure, do the 5-cycle reset, wait for blinking, then do it **again**. Many people have to do it twice on older bulbs.

A few tests before declaring it dead:

### Test 1: Scan test
The bulb is currently broadcasting `TP-LINK_Smart Bulb_D9E8`.

That means:
- Power supply is working.
- Wi-Fi chip is at least partially working.
- Firmware is running.

A completely dead bulb wouldn't create that network.

### Test 2: Hotspot test
Use a second phone and create a simple hotspot called:
- SSID: Test
- WPA2

If the bulb still says **"No Wi-Fi Networks Detected"**, even with the hotspot a few feet away, that's a very strong sign the bulb's Wi-Fi scanning function is corrupted or failing.

### Test 3: Kasa app permissions
On your iPhone:
- Settings → Kasa
- Make sure **Local Network** is ON
- Make sure **Location** is allowed while using the app

I've seen iOS permission issues cause strange setup failures that look like bulb problems.

### Is it broken?
Not necessarily, but if:
- It broadcasts its own TP-LINK network,
- Has been factory reset multiple times,
- Cannot see **any** Wi-Fi networks (including a phone hotspot),

then the bulb is very likely defective. The radio can transmit its setup SSID but still fail to scan nearby networks. That's uncommon, but it does happen.

Since you already have five working KL125s on your UniFi network, I'd spend no more than 10–15 minutes on hotspot and WPA2-only testing before calling this bulb bad. The evidence is already pointing more toward the bulb than the network.
