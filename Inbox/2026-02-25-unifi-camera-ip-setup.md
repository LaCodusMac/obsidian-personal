---
date: 2026-02-25
source: chatgpt
title: "UniFi Camera IP Setup"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Should I put my g5 ultra dome connected to UniFi protect on a fixed ip or is dynamic fine

**ChatGPT:** For your **entity["product","UniFi G5 Ultra Dome","unifi protect camera"]** running on **entity["software","UniFi Protect","video surveillance platform"]**, here’s the straight answer:

### ✅ Leave it on DHCP (dynamic) — but use a DHCP reservation.

That’s the best practice in UniFi environments.

---

## Why NOT set a manual static IP on the camera?

If you hard-code a static IP on the camera itself:

- You can lose access if you change subnets/VLANs
- It won’t follow controller-side IP management
- Future network changes become annoying
- You can accidentally create IP conflicts

UniFi gear is designed to be centrally managed.

---

## Why DHCP Reservation is Better

Instead:

1. Leave the camera set to DHCP.
2. Go into your **UniFi Network** controller.
3. Find the device.
4. Set a **Fixed IP / DHCP reservation** there.

This gives you:
- A consistent IP
- Centralized management
- Easier migrations
- Zero risk of duplicate IP conflicts

---

## When Would You Ever Use Static on the Device?

Almost never in a UniFi setup.

The only real cases:
- You’re using a third-party router
- You’re isolating it on a weird standalone subnet
- You have no DHCP server

But in your setup (UniFi gateway + switch + Protect), dynamic with reservation is the clean way.

---

## Your Current Environment

Since you:
- Run UniFi gear
- Care about clean network organization
- Have cameras + Protect

👉 Use DHCP reservation for all cameras.

Keep it simple and centralized.

---

If you want, I can also tell you whether your cameras should live on a separate VLAN for better security in your rack setup.

**You:** Should cameras be part of iot vlan? I only have one for testing

**ChatGPT:** Short answer: **Yes — cameras should be on their own VLAN**, and that VLAN is often treated like an IoT VLAN.

But since you only have one IoT VLAN right now (for testing), here’s the better way to think about it 👇

---

## 🔐 Best Practice Layout (for UniFi setups like yours)

You ideally want:

- **LAN** → Your main devices (PC, laptop, NUC, admin access)
- **IoT VLAN** → Smart home devices (Kasa, Google devices, etc.)
- **Camera VLAN** → UniFi Protect cameras only

Even though cameras are technically IoT, they behave differently:
- They constantly stream data
- They need reliable access to your Protect NVR
- You usually don’t need them talking to the internet
- You don’t want other IoT devices talking to them

---

## Why Separate Cameras from Other IoT?

If you dump everything into one IoT VLAN:

- Smart plugs can technically see cameras (bad)
- Broadcast traffic increases
- Harder to firewall properly
- Less clean segmentation

Cameras are **high-bandwidth + security-sensitive**.

---

## 🧠 What I’d Do in Your Setup

Given you:
- Run UniFi
- Care about a clean rack + network
- Are already thinking about VLAN structure

I’d recommend:

### Option 1 (Cleanest)
Create:
- VLAN 10 → LAN
- VLAN 20 → IoT
- VLAN 30 → Cameras

### Option 2 (If you want simple for now)
Put cameras on IoT VLAN
BUT:
- Block IoT → LAN
- Allow IoT → Protect/NVR only
- Block IoT → IoT device-to-device if possible

---

## Important Question for You

Where is Protect running?
- Cloud Key Gen2 Plus?
- On a UniFi NVR?
- On your NUC?

Because firewall rules depend on that.

---

## 🔥 My Opinion for Your Rack

You’re building this like a homelab already.  
Just make the camera VLAN now.

It’ll:
- Look cleaner in UniFi
- Be more secure
- Make future projects easier (Home Assistant, remote access, etc.)

If you want, tell me:
- What gateway you're running (UXG? UDM? USG?)
- Where Protect lives

I’ll give you exact rule examples.

**You:** I have one camera for testing. And an established iot and default vlab

**ChatGPT:** Perfect — that makes this simple.

You currently have:

- **Default VLAN (LAN)**
- **IoT VLAN**
- 1 × **entity["product","UniFi G5 Ultra Dome","unifi protect camera"]**
- Running **entity["software","UniFi Protect","video surveillance platform"]**

---

## 🎯 What You Should Do (Right Now)

Since this is just **one test camera**, put it on the **IoT VLAN**.

You do **NOT** need a dedicated camera VLAN yet.

That’s something you do when:
- You have multiple cameras
- You’re running 24/7 recording
- You want tighter segmentation
- You’re pushing heavier traffic

For one test camera? Keep it simple.

---

## 🔐 Just Make Sure of This

Your firewall rules should:

### ✅ Allow:
IoT VLAN → Protect device IP

### 🚫 Block:
IoT VLAN → Default VLAN (except Protect)

### Optional:
Block IoT → Internet if you want cameras fully local-only.

---

## Why This Is Fine for Now

- UniFi cameras don’t need internet to work
- Protect handles adoption internally
- Bandwidth from one G5 Ultra is negligible
- You avoid overcomplicating your network early

---

## When to Create a Camera VLAN

Do it when:
- You add 2–3+ cameras
- You install a Cloud Key / UNVR permanently
- You want ultra-clean segmentation
- You’re building toward a more advanced homelab

---

## My Advice for You

You’re already running VLANs and thinking properly about segmentation — that’s good.

For now:
> Keep camera in IoT VLAN.  
> Don’t over-engineer a one-camera test.

When you expand, we’ll architect it clean.

---

If you tell me where Protect is running (Cloud Key? UDM? NUC?) I’ll sanity-check your firewall logic.

**You:** My cloud key is established

**ChatGPT:** Perfect 👍 — since your **entity["product","UniFi Cloud Key Gen2 Plus","unifi controller nvr device"]** is established and running **entity["software","UniFi Protect","video surveillance platform"]**, here’s exactly what I’d do in *your* setup:

---

# ✅ Recommended Setup (With 1 Test Camera)

**Camera → IoT VLAN**  
**Cloud Key → Default VLAN (LAN)**

That’s totally fine.

You do **NOT** need a dedicated Camera VLAN yet.

---

# 🔐 The Important Part: Firewall Rules

Your goal is simple:

### Allow:
IoT VLAN → Cloud Key IP (Protect)

### Block:
IoT VLAN → Default VLAN (everything else)

---

## How It Should Function

- Camera boots on IoT VLAN
- DHCP reservation gives it a fixed IP
- It talks only to the Cloud Key
- Protect handles everything
- No internet required for camera

Clean. Controlled. Secure.

---

# 🔥 When Should You Make a Camera VLAN?

Create one later if:

- You add 3+ cameras
- You want tighter segmentation
- You’re optimizing broadcast domains
- You start building out more homelab services

Right now? Not necessary.

---

# ⚠️ One Thing to Double Check

Make sure:
- mDNS is enabled between VLANs (if needed)
- Or you adopt the camera manually via IP

Usually Protect handles this fine.

---

# My Opinion for Your Rack Build

Since you:
- Care about structure
- Run UniFi properly
- Already segment IoT

You’re doing it right.

For one camera:
> IoT VLAN + proper firewall rules = perfect.

If you want, tell me your gateway model (UXG? UDM? USG?) and I’ll give you the exact rule layout structure.

**You:** Uxg max

**ChatGPT:** Nice — **entity["product","UniFi UXG-Max","unifi gateway"]** is a solid choice 👌

Since you’re running:

- **UXG-Max**
- **entity["product","UniFi Cloud Key Gen2 Plus","unifi controller nvr device"]** (running **entity["software","UniFi Protect","video surveillance platform"]**)
- 1 test **entity["product","UniFi G5 Ultra Dome","unifi protect camera"]**
- Default VLAN + IoT VLAN

Here’s exactly how I’d configure it.

---

# ✅ Recommended Layout

**Default VLAN (LAN)**
- Cloud Key
- Your PC
- Admin devices

**IoT VLAN**
- Camera
- Smart home devices

No need for a camera-only VLAN yet.

---

# 🔐 Firewall Rules for UXG-Max

In UniFi Network → Firewall → LAN IN

### 1️⃣ Allow Camera → Cloud Key
Rule:
- Source: IoT VLAN
- Destination: Cloud Key IP
- Action: Allow
- Place near top

This ensures Protect works cleanly.

---

### 2️⃣ Block IoT → Default VLAN
Rule:
- Source: IoT VLAN
- Destination: Default VLAN
- Action: Drop
- Place below the allow rule

This prevents IoT devices from touching your main network.

---

### 3️⃣ (Optional but Recommended) Block IoT → Internet (For Cameras Only)

If you want your camera fully local:

Create a group:
- Camera IP(s)

Rule:
- Source: Camera IP group
- Destination: Internet
- Action: Drop

UniFi cameras do NOT need internet to function.

---

# ⚙️ DHCP Recommendation

Leave the camera on DHCP  
Create a **DHCP reservation in UniFi**.

Do NOT set a static IP directly on the camera.

---

# 🧠 Important UXG Detail

Make sure:

- Inter-VLAN routing is enabled (default is yes)
- mDNS reflector is on (if needed)

Usually Protect adoption works fine without extra tuning.

---

# 🔥 What I’d Do If This Were My Rack

For 1 camera:
> IoT VLAN + proper firewall rules = perfect.

When you expand to 3–5 cameras:
> Then create VLAN 30 → Cameras

Right now? Keep it clean and simple.

---

If you want, I can also give you a “future-proof” VLAN numbering layout that’ll make your homelab look enterprise-level.

**You:** Yes. Also let me know if home assistant will let me take the whole IoT VLAN off Internet access

**ChatGPT:** Good — now we’re building this the right way 😎  

You’ve got a **entity["product","UniFi UXG-Max","unifi gateway"]** and **entity["product","UniFi Cloud Key Gen2 Plus","unifi controller nvr device"]**, so you can structure this cleanly from the start.

---

# 🔮 Future-Proof VLAN Layout (Clean + Scalable)

Here’s what I’d run in your rack:

| VLAN | Purpose | Notes |
|------|---------|-------|
| 10 | Default / Admin LAN | PC, laptop, NUC, Cloud Key |
| 20 | IoT | Smart plugs, Google devices, TVs |
| 30 | Cameras | UniFi Protect cameras only |
| 40 | Homelab | Docker, NUC services, future HA |
| 50 | Guest | Optional |

You don’t have to build all of these today — but plan the numbering now so you don’t renumber later.

---

# 🔐 Now — Your Real Question

> Can Home Assistant let me take the entire IoT VLAN off Internet access?

Short answer:

### ✅ Yes — but not blindly.

It depends how your devices function.

---

# 🧠 How Home Assistant Actually Works

**entity["software","Home Assistant","home automation platform"]** runs locally.  
It talks to devices using:

- Local APIs (best case)
- mDNS
- MQTT
- Webhooks
- Or cloud relays (worst case)

If your devices support **local control**, you can absolutely:

> Block IoT VLAN → Internet  
> Allow IoT VLAN → Home Assistant only

And everything stays internal.

---

# 🚨 The Catch

Some IoT devices REQUIRE cloud access:

Examples:
- Some Google integrations
- Certain Kasa firmware versions
- Cheap WiFi plugs
- Cloud-only cameras

If you block internet entirely:
- Some devices stop responding
- Google voice control may break
- Firmware updates won’t work

---

# 🏆 The Ideal Secure Setup

Best practice long term:

### IoT VLAN:
- ❌ Block to LAN
- ❌ Block to Internet (default deny)
- ✅ Allow to Home Assistant IP
- ✅ Allow to DNS
- ✅ Allow to NTP

Then:
- HA lives on VLAN 40 (Homelab)
- HA has internet
- IoT does not

This creates a “broker model”:
Devices talk only to HA  
HA talks to the internet

That’s enterprise-grade segmentation.

---

# 🔥 For Your Setup Right Now

Since you:
- Run Google devices
- Run Kasa lights
- Have UniFi cameras
- Are still building things out

I would:

### Phase 1:
Allow IoT internet access  
Block IoT → LAN  
Allow IoT → Cloud Key  
Allow IoT → HA (if installed)

### Phase 2 (once stable):
Start selectively blocking internet per-device group

---

# 💡 Big Important Question

Where would you run Home Assistant?

- On your NUC in Docker?
- On a Raspberry Pi?
- On the Cloud Key? (not ideal)

Given your hardware, your NUC is perfect.

---

# 🧠 My Honest Opinion

Yes — you *can* take IoT off the internet.

But you should:
1. Move HA to a dedicated VLAN
2. Confirm local control for each device
3. Then restrict internet gradually

Don’t flip the switch all at once.

---

If you want, I can map out:
- Exact firewall rules for UXG
- Ideal HA network placement
- Whether your specific Kasa + Google setup supports full local control

You’re very close to having a seriously clean homelab network.

**You:** Is what you suggested full local control or different ? Also I have chrome cast, Google home speakers, kasa light bulbs and strips.

**ChatGPT:** Good — this is where things get real.

You listed:

- **entity["product","Google Chromecast","google streaming device"]**
- **entity["product","Google Nest Mini","google smart speaker"]** (Google Home speakers)
- **entity["company","TP-Link","networking hardware company"]** Kasa bulbs & strips
- UniFi camera on Protect

Let’s break this down clearly.

---

# 🧠 Is What I Suggested “Full Local Control”?

Not completely.

What I suggested was:

> Block IoT → LAN  
> Allow IoT → Home Assistant  
> Gradually reduce Internet access  

That becomes full local control **only if your devices support it**.

---

# 🔎 Your Devices — Reality Check

## 🎥 Chromecast

❌ Requires internet  
❌ Requires Google cloud  
❌ Won’t function properly fully offline  

You cannot remove internet from Chromecast.

---

## 🔊 Google Home / Nest Speakers

❌ Require internet  
❌ Google Assistant is cloud-based  

If you block internet:
- Voice commands stop working
- Routines break
- Casting may break

---

## 💡 Kasa Bulbs / Strips

This is the interesting one.

Older firmware:
✅ Supports local LAN control  

Newer firmware:
⚠️ Sometimes cloud-dependent  
⚠️ May break if fully offline  

Home Assistant can control Kasa locally **if local API is enabled and firmware supports it.**

---

# 🏆 What “True Full Local” Would Mean

For your setup, full local control would require:

- No Google Assistant
- No Chromecast
- Local-only smart switches (like Zigbee/Z-Wave)
- No cloud reliance

That is NOT your current ecosystem.

---

# 🔐 What You Should Actually Do

Instead of cutting IoT internet entirely:

### 🔹 Better Plan (For You)

Keep IoT internet access  
BUT:

- Block IoT → Default VLAN
- Allow IoT → Cloud Key
- Allow IoT → Home Assistant
- Block IoT device-to-device if possible
- Enable mDNS reflector for casting

That keeps:
- Google working
- Chromecast working
- Kasa working
- Cameras secure

---

# 🧠 If You Want Maximum Security

Later, you could split:

| VLAN | Purpose |
|------|----------|
| 20 | “Cloud IoT” (Google, Chromecast) |
| 30 | Cameras |
| 40 | Local IoT (if you migrate to Zigbee) |

But right now that’s overkill.

---

# ⚡ Important UXG Note

With Chromecast + Google Home across VLANs:

You MUST:
- Enable mDNS reflector
- Possibly allow UDP 1900 / 5353 between VLANs

Otherwise casting breaks.

---

# 🎯 My Recommendation For You Today

Do NOT remove internet from IoT VLAN.  
You are using cloud-dependent devices.

Instead:
> Segment properly, don’t air-gap.

---

If you want, tell me:
- Do you plan to move toward more “homelab / local control” long term?
- Or do you just want clean + secure while keeping Google ecosystem?

That answer changes the architecture.
