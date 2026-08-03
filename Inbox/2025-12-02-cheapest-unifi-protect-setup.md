---
date: 2025-12-02
source: chatgpt
title: "Cheapest UniFi Protect setup"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Cheapest way to do UniFi protect with current setup

**ChatGPT:** Good question. Because you already have extra hardware (you mentioned extra SSDs and potential NAS-repurposing machines), the cheapest way to get entity["software","UniFi Protect",0] working *practically* — without buying expensive new gear — is limited by how UniFi Protect is designed. Here’s the deal + what your cheapest realistic setups are:

## ✅ Important: UniFi Protect ecosystem limitation

- UniFi Protect is a closed ecosystem: you **cannot** officially run it on arbitrary hardware (like your own PC/NAS) — it requires one of their designated “UniFi OS Consoles” (e.g. Cloud Key Gen2+, UNVR, UDM-Pro/SE, etc.). citeturn0search5turn0search4turn0search8  
- Self-hosting for just the “network controller” (for APs, routing, etc.) can be done on third-party hardware, but that doesn’t include Protect. citeturn0search3turn0search5  
- In short: even if you have spare SSDs or a spare PC/NAS box, you can’t officially “install Protect” on them.  

Because of that, the “cheapest way” requires buying a supported piece of hardware — you’re basically paying once for the right console.  

---

## 💡 Cheapest Official Entry Options

Here are the lowest-cost new (or sometimes used) ways to get into Protect — ranked by price / simplicity.  

products{"selections":[["turn0product1","Ubiquiti UniFi Dream Machine SE (UDM-SE)"],["turn0product13","Ubiquiti UniFi Dream Machine Pro (UDM-Pro)"],["turn0product19","Ubiquiti UniFi Dream Machine (UDM)"],["turn0product17","Ubiquiti Dream Router 7"],["turn0product0","WD Purple 4TB Surveillance Internal Hard Drive"],["turn0product2","Seagate 2TB Surveillance SATA III 3.5\" HDD"],["turn0product12","Seagate SkyHawk 4TB Surveillance Hard Drive"],["turn0product14","1TB SMARTSF DVR/NVR Compatible Internal Hard Drive"]],"tags":["All-in-one (best value)","All-in-one (Pro)","Entry-level router (no Protect)","Budget router option","Surveillance HDD 4TB","Surveillance HDD 2TB","Surveillance HDD 4TB","Budget HDD 1TB"]}

### Quick takes

- **product_entity["turn0product1","Ubiquiti UniFi Dream Machine SE (UDM-SE)"]** — Easiest all-in-one: router + PoE + built-in UniFi OS + NVR support. If you don’t yet own a router/firewall and want the simplest path, this tends to be the most straightforward, albeit a bit pricey.  
- **product_entity["turn0product13","Ubiquiti UniFi Dream Machine Pro (UDM-Pro)"]** — Similar to the SE, works well if you prefer a more “pro / rack-style” setup and want to support multiple cameras with expandability.  
- **product_entity["turn0product19","Ubiquiti UniFi Dream Machine (UDM)"]** — Lower-cost UniFi router/gateway… but it’s important: the base UDM does *not* support UniFi Protect. citeturn0reddit39turn0search5 So not useful by itself for cameras.  
- **product_entity["turn0product17","Ubiquiti Dream Router 7"]** — Could be considered if you just want a budget router and very light camera usage — but camera support and storage will be extremely limited. citeturn0search8turn0search7  

If you go with one of the “NVR-capable” options (UDM-SE or UDM-Pro), you’ll also want a decent surveillance-grade HDD for reliable recording/storage rather than relying on consumer SSDs. Drives like **product_entity["turn0product0","WD Purple 4TB Surveillance Internal Hard Drive"]** or **product_entity["turn0product2","Seagate 2TB Surveillance SATA III 3.5\" HDD"]** give a good balance of price vs storage — and they’re designed for 24/7 video recording.  

---

## 🎯 What about using your own NUC / PC / NAS with spare SSDs?

You **could not** officially run UniFi Protect on your own NUCs (or repurposed NAS/PC) because Protect expects to run on approved UniFi OS consoles. citeturn0search5turn0search0  

Some people in community forums express frustration at this (“I already have 50+ TB of storage, why buy new hardware just to license Protect”), noting that the software “will only run on Ubiquiti hardware.” citeturn0reddit26turn0reddit33  

In short: while technically there are some unofficial hacks, they're not supported, likely unstable, and not recommended if you want reliability.  

---

## ✅ My Recommendation Given Your Background (You Have Spare Hardware/NAS, but Want Cheap & Reliable)

Because you already have spare storage and hardware experience — but given the limitations — **the most sensible, cost-effective way** is:

- Get a used or new UDM-SE or UDM-Pro (depending on how many cameras you plan), **plus** a surveillance-class HDD (e.g. WD Purple or Seagate Surveillance) for storage.  
- Use your existing networking gear and NAS/storage for other purposes — let UniFi Protect use the dedicated console/storage.  

That gives you a clean, officially-supported UniFi Protect setup without overpaying or tying up your other hardware.  

---

If you want — I can **sketch 3 full budget scenarios** (low / medium / maximum leveraging your existing gear) *with approximate cost total* for you. That way you can pick the one closest to your budget.  
Do you want me to build that cost-scenario sheet for you now?

**You:** I have uxg max, 24 port UniFi switch and ap pro

**ChatGPT:** Got it — **you already have:**

- **UXG-Max** (router/gateway)  
- **24-port UniFi Switch**  
- **UniFi AP Pro**

So you already have network + PoE gear handled **perfectly**.

### ✅ That means the *only* thing you need for UniFi Protect is an **NVR-capable UniFi OS Console.**  
Everything else works with what you have.

---

# ⭐ Cheapest Possible UniFi Protect Options (given your setup)

## **1️⃣ Cheapest Overall: Cloud Key Gen2+ (CKG2+)**  
**Usually $150–$200 used**, $199 new  
- Has **1TB drive included**  
- Runs **UniFi OS** → Protect, Network, etc.  
- Good for **1–6 cameras** (depending on bitrate)  
- VERY low power usage  
- Easiest drop-in option  
- Works perfectly with UXG-Max + Switch + AP

👉 If you only plan on **a few cameras**, this is the **absolute cheapest**.

---

## **2️⃣ Best Value for More Cameras: UNVR (the original, not the Pro)**  
**$299 new**, often **$180–$230 used**  
- 4-bay NVR (HDDs not included)  
- Rock-solid for **5–20+ cameras**  
- Dedicated box = no performance issues  
- Works perfectly with UXG-Max  
- No router functions (you don’t need them anyway)

👉 If you want more than **3–5 cameras**, THIS is the best “cheap but scalable” option.

---

## **3️⃣ UDM-Pro / UDM-SE — NOT needed**  
You already have a UXG-Max, so don’t buy a UDM-Pro/SE unless you want to replace your gateway.  

These would **duplicate** what your UXG already does.

---

# 🥇 Best Choice For You
Depending on your plans:

### ✔ **Just want 1–4 cameras?**  
→ **Cloud Key Gen2+** (cheapest, cleanest)

### ✔ **Want 5+ cameras?**  
→ **UNVR** (still cheap, way more storage/options)

---

# 📦 How it plugs into your current setup

```
Internet → UXG-Max → 24-port UniFi Switch → Cameras
                               ↓
                     CKG2+ or UNVR (NVR)
```

- UXG still handles routing  
- Switch still handles PoE  
- NVR handles UniFi Protect only  
- AP Pro keeps working as normal  

Super clean.

---

# 💬 Want me to build you a recommended setup?
I can list:

- Total cost
- Exact model
- Where to buy cheap (used/refurb vs new)
- How many cameras it supports
- Best camera choices for budget/night vision

Just tell me:
**How many cameras are you planning to run?**
