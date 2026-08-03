---
date: 2026-03-12
source: chatgpt
title: "UniFi VPN Setup Guide"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** How to do my UniFi vpn

**ChatGPT:** Since you already run a **entity["software","UniFi Network","Ubiquiti network controller software"]** controller in your homelab, the **best VPN option is WireGuard**. It’s fast, simple, and works great for securely accessing your **Synology, Plex server, and NUCs** from anywhere. 🔐

Below is the **recommended setup for a home lab like yours**.

---

## 1️⃣ Create a VPN Server in UniFi (WireGuard)

1. Open your **UniFi Network Controller**.
2. Go to **Settings → VPN**.
3. Click **Create New**.
4. Select **WireGuard Server**.
5. Configure:

**Basic Settings**
- **Name:** `Home VPN`
- **VPN subnet:** `192.168.50.0/24`  
- **Port:** `51820` (default)

**Gateway / Router**
- Choose your **UniFi gateway** (Dream Machine / USG / etc.).

6. Click **Apply / Save**.

Your router now runs the VPN server.

---

## 2️⃣ Create a User (Client)

1. Go to **Settings → VPN → WireGuard → Clients**
2. Click **Add Client**

Fill in:

- **Name:** `Jake iPhone`
- Leave everything else default.

UniFi will generate:

- **Private key**
- **Public key**
- **QR code**

---

## 3️⃣ Connect Your Phone

Install the app:

- **entity["mobile_app","WireGuard","VPN client app"]**

Then:

1. Open WireGuard
2. Tap **Add Tunnel**
3. Scan the **QR code from UniFi**
4. Toggle the VPN **ON**

You are now connected to your home network.

---

## 4️⃣ Test Access

While on **cellular or outside your network**, try opening:

- **Synology DSM**
  ```
  https://192.168.1.x:5001
  ```

- **Plex**
  ```
  http://192.168.1.x:32400
  ```

- **UniFi Controller**
  ```
  https://192.168.1.x
  ```

If it loads → your VPN works.

---

## 5️⃣ What This Lets You Do (Perfect for Your Setup)

With your **NUC + Synology homelab**, VPN gives you secure access to:

- 🎬 **Plex** without opening ports
- 📂 **Synology files**
- 🐳 **Docker containers on your NUC**
- 🌐 **Pi-hole / DNS**
- 🖥 **SSH into servers**

Basically **your whole home network remotely**.

---

## 6️⃣ Important Security Setting

In the WireGuard client config:

Enable:

**Allowed IPs**
```
0.0.0.0/0
```

This routes **all traffic through your home network**, protecting you on public Wi-Fi.

---

✅ **Your homelab with VPN should look like this**

```
Internet
   │
UniFi Gateway
   │
───────────────
│              │
NUC (Docker)   Synology NAS
Plex           Backups
Containers
```

Phone → **WireGuard VPN → Home network**

---

💡 Since you're building a **serious homelab with NUCs and a NAS**, the **next level UniFi setup I’d recommend** is:

- VPN
- VLANs
- Remote management
- Ad blocking network-wide

If you want, I can also show you **the clean “pro” UniFi homelab layout** most people miss (it makes your setup way better).
