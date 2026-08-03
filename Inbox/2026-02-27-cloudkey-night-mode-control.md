---
date: 2026-02-27
source: chatgpt
title: "Cloudkey Night Mode Control"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Cloudkey goes into night mode

**ChatGPT:** If your **entity["product","UniFi Cloud Key Gen2 Plus","ubiquiti network controller"]** is going into **Night Mode**, here’s what’s happening and how to control it.

---

## 🌙 What “Night Mode” Actually Is

On the Gen2 Plus, Night Mode:
- Dims or turns off the **front LCD screen**
- Leaves the device fully running (Protect, Controller, etc. are unaffected)
- Is purely cosmetic / power-saving

Your network and cameras are still operating normally.

---

## 🔧 How to Disable or Adjust Night Mode

### Option 1 – From the Cloud Key Screen
1. Tap the **front touchscreen**
2. Go to **Settings**
3. Find **Display**
4. Adjust:
   - Brightness
   - Night Mode schedule (or disable it)

---

### Option 2 – From UniFi OS Web UI
1. Go to your Cloud Key IP (example: `https://192.168.1.x`)
2. Log into **UniFi OS**
3. Click **Console Settings**
4. Look for **Display / Screen Settings**
5. Adjust Night Mode or brightness

---

## ⚙️ Why It Might Be Turning On Automatically

Common reasons:
- Default schedule enabled (usually evening hours)
- Ambient light detection (if enabled)
- Firmware update reset settings

---

## 🧠 Since You’re Running Protect + Controller

Given your setup:
- UXG Max
- UniFi switch
- Cloud Key handling Protect

Night Mode will **not** impact:
- Camera recording
- VLANs
- Plex on your NUC
- Network performance

It’s strictly screen behavior.

---

If it’s turning off completely (not just dimming), tell me:
- Is the LED ring still on?
- Can you access it via web?
- Is it rebooting or just dark?

We’ll diagnose it properly.
