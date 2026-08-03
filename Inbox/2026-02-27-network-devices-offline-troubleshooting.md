---
date: 2026-02-27
source: chatgpt
title: "Network Devices Offline Troubleshooting"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_00000000296c71f78bc5f4d24cf24300", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 270047, "width": 709}
What is going on

**ChatGPT:** Alright — based on your screenshot:

### What’s Happening

Your UniFi console (**UOS Server – UCK G2 Plus**) is online ✅  
Your **G5 Dome Ultra camera** is online ✅  

But these devices are **offline** ❌:
- AC Pro (Access Point)
- UXG Max (Gateway)
- USW 24 PoE (Switch)

---

### What This Means

Your **Cloud Key is powered and reachable**, but it cannot communicate with your core network devices.

This usually happens in one of these scenarios:

#### 1️⃣ Devices lost power
Power outage, tripped breaker, unplugged PoE, etc.

#### 2️⃣ They’re on a different network/site
If you were restoring backups or moving controllers (you were earlier), they might be:
- Adopted to another site
- Stuck to a different controller
- On a different VLAN

#### 3️⃣ The UXG is down
If the **gateway is offline**, that’s the most important one.
If UXG is off:
- Switch goes offline
- AP goes offline
- Only devices directly connected to Cloud Key might stay up

Your camera is online, which suggests:
- It’s powered
- It’s reachable through the Cloud Key
- Possibly connected differently than the rest

---

### Most Likely Cause (Based on Your Setup)

Since:
- You’ve been migrating controllers
- You have two sites previously
- You were restoring backups

This smells like a **controller/site mismatch**.

Your UCK is up — but the gateway/switch/AP are either:
- Still adopted to the old site
- Factory reset
- On a different management IP

---

### Quick Checks (In Order)

#### ✅ 1. Are the lights on?
Physically check:
- UXG Max
- USW 24 PoE
- AC Pro

No lights = power issue.

---

#### ✅ 2. Can you still access the internet?
If yes:
- Your UXG might actually be working but just not adopted to this controller.

If no:
- Gateway is likely actually down.

---

#### ✅ 3. SSH Test
From a laptop on the network:

```
ping 192.168.1.1
```

(or whatever your gateway IP is)

If no response → UXG is truly offline.

---

### Important Question

Did you recently:
- Factory reset anything?
- Restore the Cloud Key from backup?
- Delete one of the sites?

That context changes the fix completely.

---

### Big Picture

Right now your network hierarchy looks like this:

ISP  
→ UXG (Offline?)  
→ Switch (Offline?)  
→ AP (Offline?)  
→ Cloud Key (Online)  
→ Camera (Online)

That’s not normal.

---

Answer me this:

1. Do you currently have internet working?
2. Did you just restore or migrate the controller?
3. Are the physical devices powered on?

We’ll fix it step-by-step.

**You:** I was playing around with vlans

**ChatGPT:** Ahhh.  

You were playing with VLANs.  

That explains almost everything. 🔥

Right now what likely happened is:

Your **management VLAN changed**, and your:

- UXG Max  
- USW 24 PoE  
- AC Pro  

are now sitting on a VLAN your Cloud Key **cannot reach**.

But your **G5 Dome Ultra is still online**, which means:
- It’s either on the default VLAN
- Or Protect is still reachable locally

---

## What Probably Happened

You likely:
- Created a new VLAN
- Assigned it to a port profile
- Or changed the “Management Network” setting

And one of these occurred:

### 1️⃣ You changed the switch uplink port profile  
If you tagged or removed the native VLAN on the port connecting:
- UXG ↔ Switch  
- Switch ↔ Cloud Key  

You effectively isolated your core devices.

---

### 2️⃣ You changed the Default network VLAN ID  
If you modified VLAN 1 or the management network, devices might now be:

- Still expecting old VLAN
- Sitting untagged
- Or tagged incorrectly

---

### 3️⃣ You moved devices to a VLAN without proper routing  
If your Cloud Key is on VLAN 1 but your devices are now on VLAN 20 (for example) —  
and inter-VLAN routing isn’t configured correctly — they’ll show offline.

---

# Why the Camera Is Still Online

This is important.

Your G5 Dome Ultra is online because:

- It’s powered via PoE
- Protect runs directly on the Cloud Key
- It may be on the same VLAN as the Cloud Key

So Protect is happy.
Network devices are not.

---

# Immediate Fix Strategy (Clean & Controlled)

We’re going to do this safely.

### Step 1 — Do you still have internet?
If yes → UXG is actually working.
If no → you VLAN’d the gateway interface.

---

### Step 2 — Plug laptop directly into the switch
Bypass WiFi.

Check your IP:

```
ipconfig
```

Are you still getting:
```
192.168.1.x
```
Or something else?

---

### Step 3 — Most Common Fix

If you changed VLANs on the switch uplink port:

Go to:
Settings → Ports → Uplink port → Set profile to “All” or “Default”

If you can’t access the switch because it’s offline:

You may need to:

- Factory reset the switch
- Or factory reset the UXG (last resort)

---

# Before We Nuke Anything

Answer these:

1. Do you still have internet?
2. Did you change the VLAN on the LAN interface of the UXG?
3. Did you change port profiles on the switch uplink?

We’ll surgically fix this without wiping everything.

You were just leveling up your network skills a little too aggressively 😅
