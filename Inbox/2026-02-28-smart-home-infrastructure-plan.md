---
date: 2026-02-28
source: chatgpt
title: "Smart Home Infrastructure Plan"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** You’ve got:
	•	🖥 NUC10i5FNH (32GB RAM)
	•	🖥 NUC8i7BEH (32GB RAM)
	•	🖥 Potential OptiPlex 3070
	•	📦 Synology NAS (SHR)
	•	🌐 UniFi stack (UXG, switch, VLANs)
	•	🐳 Docker already in play

You’re officially in “why not build something cool” territory.

Let’s break this down practically.

⸻

🏆 Best Use of Each Device (Smart Layout)

🥇 NUC8i7BEH (Strongest iGPU – Iris Plus)

Primary Media + Performance Node

Why:
	•	Best hardware transcoding of the group
	•	Strong i7 CPU
	•	32GB RAM

Use it for:
	•	🎬 Plex (primary server)
	•	📡 Reverse proxy (Nginx / Traefik)
	•	🔄 Sonarr / Radarr / Qbit
	•	🔐 Tailscale / WireGuard
	•	📊 Uptime Kuma monitoring

This stays your “production” box.

⸻

🥈 NUC10i5FNH (Efficient & Modern)

Services / Automation Node

Use it for:
	•	🏠 Home Assistant (full supervised install)
	•	📦 Docker lab environment
	•	🧪 Test containers before production
	•	📈 Grafana + Prometheus
	•	🔐 Pi-hole / AdGuard Home (DNS filtering)
	•	🧠 Immich (self-hosted Google Photos alternative)

This becomes your core automation brain.

⸻

🥉 OptiPlex 3070

This depends on what you want to build:

Option A — Backup Plex Node
	•	Secondary Plex server
	•	Sync libraries
	•	Failover test box
	•	Remote friend Plex box

Option B — Virtualization Playground

Install:
	•	Proxmox
	•	ESXi
	•	Or full KVM

Run:
	•	Windows test VM
	•	Kali Linux
	•	AD lab (domain controller)
	•	Blue Team/SOC lab
	•	Malware sandbox

With your IT background, this actually builds resume-level skills.

⸻

🔥 Cool Projects You Could Run

🧠 1. Full Local Smart Home (Privacy-Focused)

You asked about smart home privacy before.

Use:
	•	Home Assistant on one NUC
	•	IoT VLAN isolated
	•	No cloud dependency

You can:
	•	Block IoT internet access
	•	Still control everything locally
	•	Build automations for lights, cameras, Plex presence

⸻

🎥 2. Private Media Empire
	•	Main Plex on NUC8
	•	Backup Plex on OptiPlex
	•	Sync metadata
	•	Load balance with reverse proxy
	•	Add Overseerr for requests

You’d have better uptime than many small businesses.

⸻

🔐 3. Security Lab (Given Your Network Setup)

Run:
	•	Wazuh SIEM
	•	Suricata IDS
	•	Graylog
	•	CrowdSec

You can monitor your own network traffic from your UniFi environment.

That’s legit cybersecurity experience.

⸻

☁️ 4. Build Your Own “Mini Cloud”
	•	Nextcloud
	•	Immich
	•	Vaultwarden
	•	File browser
	•	Internal Git server

Basically:

JakeCloud™ – fully self-hosted.

⸻

🧪 5. Resume Builder Lab

Since you’re Level 2 IT:

You could practice:
	•	Active Directory
	•	Group Policy
	•	Hybrid Azure
	•	Linux clustering
	•	HAProxy
	•	Kubernetes (k3s cluster across NUCs 👀)

Three small machines = perfect cluster lab.

⸻

⚡ The Real Move (If It Were Me)

If I had your hardware:
	•	🧠 NUC10 → Infrastructure (DNS, HA, monitoring)
	•	🎬 NUC8 → Media & external services
	•	🧪 OptiPlex → Virtualization lab + security testing

That gives:
	•	Separation of workloads
	•	Redundancy
	•	Learning platform
	•	Production stability

⸻

🛑 What NOT To Do
	•	Don’t stack everything on one box.
	•	Don’t waste the i7 Iris GPU on just Pi-hole.
	•	Don’t leave 32GB RAM idle.

You have legit small enterprise hardware at this point.

⸻

💬 Let Me Ask You

What’s the goal:
	1.	More stable Plex?
	2.	Resume building?
	3.	Privacy-focused smart home?
	4.	Security lab?
	5.	Just fun projects?

Pick one and I’ll design you a clean architecture for it. Let’s start a conversation based on this chat from you

**ChatGPT:** Bet — let’s turn that into a *real* plan you can actually run, not just a cool idea list.

You already have the pieces for a “small enterprise at home” layout. The biggest win is **separating roles** so Plex stays stable while you experiment without breaking movie night.

## Baseline architecture (works no matter what your main goal is)

### Roles
- **NUC8 i7 (32GB)** = **Production / Media Edge**
  - Plex + the stuff that touches the outside world (proxy, remote access)
- **NUC10 i5 (32GB)** = **Core Services / Home Infrastructure**
  - DNS, monitoring, Home Assistant, auth, dashboards
- **OptiPlex 3070 (if you grab it)** = **Lab / Virtualization**
  - Proxmox + VMs for AD/SOC/testing

### Network/VLAN layout (clean + safe)
- **LAN (Trusted)**: your PC/laptop, admin access
- **SERVERS**: NUCs, Synology (only you/admin can reach this freely)
- **IOT**: Kasa/Chromecast/Google speakers/cameras
- **GUEST**: guests only
- **MGMT (optional)**: UniFi management interfaces

**Rules of thumb**
- IOT → Internet: allowed (or selectively allowed), **IOT → SERVERS: blocked by default**
- LAN → SERVERS: allowed
- SERVERS → IOT: allowed only if needed (Home Assistant talking to devices)
- Remote access: **VPN in (Tailscale/WireGuard)** > exposing ports

This keeps “smart home stuff” from being able to poke at your NAS/servers.

---

## What I’d build first (the “make it stable + expandable” starter pack)

### On NUC10 (Core Services)
Run these as your “foundation” Docker stack:
- **AdGuard Home** (or Pi-hole) = network-wide DNS filtering
- **Uptime Kuma** = simple monitoring
- **Grafana + Prometheus** = stats for everything (optional but awesome)
- **Home Assistant** = your automation brain
- **Scrypted or Frigate** (later) if you want local camera smarts

### On NUC8 (Production / Media)
Run:
- **Plex**
- **Arr stack** (Sonarr/Radarr/Prowlarr/qBittorrent) — if you use it
- **Overseerr** (requests)
- **Reverse proxy** (Nginx Proxy Manager or Traefik) only if you *really* need external web access

And keep your **Synology as the source of truth** for media (like you’re already doing with `/mnt/media`).

---

## The “Jake-proof” rules so you don’t nuke your own setup while learning
1. **Production (NUC8) doesn’t change unless something is broken.**
2. New stuff gets deployed on **NUC10 first**.
3. If you add the OptiPlex: all “break it / learn it / hack it” goes there.

That’s how you get stability *and* freedom to experiment.

---

## If you pick one goal, here’s how the design shifts

### 1) “More stable Plex”
- Plex + proxy/VPN stays on NUC8
- NUC10 runs monitoring + DNS + alerts
- Add: **automated backups of Plex config** + basic health checks (mount available, container up, NAS reachable)

### 2) “Resume building”
- OptiPlex with **Proxmox**
- Build:
  - AD Domain Controller + Windows client VM
  - Linux server VM
  - “Ticket simulation” VM (like a fake corp environment)
  - Optional: Azure/hybrid practice later
- Your UniFi VLANs become the “enterprise segmentation story”

### 3) “Privacy smart home”
- Home Assistant on NUC10
- IoT VLAN mostly blocked from LAN/SERVERS
- Gradually migrate cloud-dependent devices to local control where possible
- You can still keep Google speakers, but treat them as “less trusted”

### 4) “Security lab”
- OptiPlex: Wazuh/Graylog/ELK + a Kali VM
- Mirror/monitor traffic (carefully) and log:
  - DNS queries (AdGuard)
  - UniFi events
  - Server logs
- Add: CrowdSec on your proxy/VPN entry points

### 5) “Just fun projects”
- Immich, Vaultwarden, Nextcloud, a dashboard homepage, game servers, etc.
- But still keep the separation so Plex never suffers.

---

## Your next move (quick, practical)
If we start this like a real build-out, step 1 is:

**Decide what is “production” today.**  
Right now your Plex is on an Ubuntu NUC in Docker, with Synology mounted at `/mnt/media`. Perfect.

So we do either:
- **Option A (least disruption):** Keep Plex where it is, and move “core services” to the *other* NUC.
- **Option B (best long-term):** Make NUC8 the dedicated production Plex box and migrate cleanly.

I can design either one as a “do this, then this” sequence.

### Pick one number so I lock the architecture:
1) Stable Plex first  
2) Resume builder lab first  
3) Privacy smart home first  
4) Security lab first  
5) Fun/self-hosted cloud first  

Once you pick, I’ll give you:
- exact VLAN/firewall rule set (what talks to what)
- which services go on which box
- a clean docker-compose stack layout
- backup plan (Synology + configs) so you can break stuff safely

**You:** Get me ready to setup home lab. Which device should I use to best utilize everything and keep learning. And number 1 & 2 of 3

**ChatGPT:** Since you want **(1) stable Plex** and **(2) a resume-building lab**, the best move is to design the homelab so:

- **Plex and media never break**
- **You can freely experiment and learn**
- **Your hardware is actually utilized**

Right now you already have a good base: **NUC + Synology + UniFi + Docker**. The trick is **separating production from lab**.

---

# 🧠 The Best Device Layout for Your Lab

## 🥇 NUC8i7BEH — Production Server
This becomes the **stable box that always works**.

Use it for:

- 🎬 Plex  
- 📡 Reverse proxy (Nginx Proxy Manager / Traefik)  
- 📥 Sonarr / Radarr / Prowlarr  
- 🌐 Tailscale or WireGuard  
- 📊 Uptime Kuma monitoring  

Why this machine:
- **Iris Plus iGPU → best hardware transcoding**
- **Strong i7 CPU**
- **32GB RAM**

This should **almost never change once configured**.

Your current setup (Docker + NFS mount from Synology) already fits perfectly.

---

## 🥈 NUC10i5FNH — Core Infrastructure Server
This becomes your **homelab infrastructure brain**.

Run things that support the network and teach you real skills.

Recommended services:

- 🏠 **Home Assistant**
- 🧠 **Immich** (self-hosted photos)
- 🌐 **AdGuard Home / Pi-hole**
- 📊 **Grafana + Prometheus**
- 🔐 **Vaultwarden**
- 📈 **Uptime Kuma**

This teaches you:

- Docker stack management
- DNS infrastructure
- monitoring & metrics
- smart home automation
- reverse proxy concepts

---

## 🥉 OptiPlex 3070 — Virtualization Lab
This becomes your **learning playground**.

Install:

**Proxmox**

Then run VMs like:

| VM | Purpose |
|---|---|
| Windows Server | Active Directory |
| Windows 11 | domain client |
| Ubuntu Server | Linux admin |
| Kali Linux | security testing |
| Wazuh | SIEM/security monitoring |

This teaches **real enterprise IT skills**.

Perfect for someone with **Level 2 IT experience** who wants to grow.

---

# 🧱 Your Full Homelab Architecture

```
Internet
   │
Arris Modem
   │
UXG Max
   │
UniFi Switch
   │
 ├── Synology NAS (media storage)
 ├── NUC8 i7 (Plex + media services)
 ├── NUC10 i5 (Home Assistant + infra services)
 ├── OptiPlex 3070 (Proxmox lab)
 ├── UniFi AP
 └── Gaming PC
```

Your **Synology remains the storage backbone**.

---

# 🌐 Recommended VLAN Layout

Since you're already experimenting with VLANs in UniFi, build it properly now.

| VLAN | Purpose |
|---|---|
| **LAN** | PCs / laptops |
| **SERVERS** | NUCs + NAS |
| **IOT** | cameras, Kasa, Google devices |
| **GUEST** | guest WiFi |
| **LAB** | Proxmox VMs |

Basic rules:

- IOT → LAN ❌ blocked
- IOT → Internet ✅ allowed
- LAN → SERVERS ✅ allowed
- LAB → SERVERS ⚠️ limited

This mimics **enterprise segmentation**.

---

# 🧰 Software You Should Learn (Resume Value)

These will actually help your career.

### Infrastructure
- Docker
- Proxmox
- Linux administration
- NFS / SMB storage
- reverse proxy

### Networking
- VLANs
- firewall rules
- DNS servers

### Monitoring
- Grafana
- Prometheus
- Uptime Kuma

### Security
- Wazuh
- CrowdSec
- Suricata

### Automation
- Home Assistant
- scripts & automations

---

# 🔐 Backup Strategy (Important)

Your setup should follow **3-2-1 backup**:

- Primary media → Synology
- Snapshots → Synology
- Config backups → second location (cloud or external)

Back up:

- Docker configs
- Plex database
- Home Assistant
- Proxmox VMs

---

# ⚡ What I Recommend You Do First

### Step 1
Dedicate machines:

| Machine | Role |
|---|---|
NUC8 | Plex production |
NUC10 | Infrastructure |
OptiPlex | Proxmox lab |

---

### Step 2
Move all infrastructure services to **NUC10**.

---

### Step 3
Install **Proxmox on OptiPlex**.

This becomes your **IT learning environment**.

---

# 🚀 The Next Level (Very Cool Project)

Once everything runs:

Build a **3-node Kubernetes cluster** across:

- NUC8
- NUC10
- OptiPlex

This teaches **modern DevOps infrastructure**.

---

# 💡 The Biggest Mistake People Make

They put **everything on one server**.

Your hardware allows you to run a **mini datacenter**.

Separating roles makes everything:

- faster
- safer
- easier to learn from

---

# 👍 Quick Question For You

One thing will determine the **best homelab design**:

Do you want your **NUCs running:**

**Option A**
Ubuntu + Docker (what you're already doing)

**Option B**
Proxmox virtualization

**Option C**
Hybrid (Proxmox + Docker VMs)

If you tell me that, I can also show you **a homelab architecture that most engineers use** and it would fit your exact hardware perfectly.
