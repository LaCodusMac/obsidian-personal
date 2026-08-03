---
date: 2026-03-09
source: chatgpt
title: "Backup Laptop Setup"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_0000000080c471f5983c24ce9d699864", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 434743, "width": 1152}
My back up laptop. What should I set it up with

**ChatGPT:** That’s actually a **great backup server candidate** for your homelab.

From the picture I can see:  
- **Dell Latitude 5420**
- **Intel i5-10310U (10th gen, 4 cores / 8 threads)**
- **16 GB RAM**
- **~512 GB SSD**

For what you told me earlier — **backing up your Synology + having a safe fallback machine** — here’s the best setup.

---

# Best Setup for This Backup Laptop

## 1️⃣ Install **Ubuntu Server**
Skip Windows for this role.

**Why Ubuntu Server:**
- Stable and lightweight
- Easy automation
- Runs backup tools + Docker
- Good for learning Linux (helpful for your IT career)

Use **Ubuntu Server 22.04 LTS**.

---

# 2️⃣ Primary Job: Synology Backup Target
This laptop should act as a **secondary backup destination** for your NAS.

Flow would be:

```
Synology NAS
     ↓
Laptop Backup Server
     ↓
External drive (optional later)
```

### Software Options

Best options:

**Option A (simplest)**  
Use **Synology Hyper Backup → Rsync**

**Option B (my favorite)**  
Use **Restic + cron**

**Option C (GUI)**  
Use **Duplicati**

You asked about Duplicati before — it's actually perfect for this.

---

# 3️⃣ Enable Remote Access (VPN)
Since you have **UniFi**, the safest setup is:

**WireGuard VPN on your UniFi router/controller**

Then when you're away:

```
Laptop / Phone
     ↓
VPN
     ↓
Home Network
     ↓
Access Synology + Backup Laptop
```

No ports exposed.

---

# 4️⃣ Optional Containers (Very Useful)
Since the laptop has **16GB RAM**, you can run some helpful Docker containers.

Examples:

**Core homelab tools**

| Container | Purpose |
|---|---|
| Portainer | Docker management GUI |
| Tailscale or WireGuard | backup VPN |
| Uptime Kuma | monitor your servers |
| Duplicati | backup software |
| Syncthing | device file sync |

---

# 5️⃣ Disk Layout
Keep it simple.

```
500GB SSD

200GB → OS + Docker
300GB → Backup storage
```

Later you can add:

- **External 4TB USB drive**
- Use it as **offline backup**

---

# 6️⃣ Automatic Backups
Set a schedule like:

**Daily**
```
Synology → Laptop backup
```

**Weekly**
```
Laptop → external drive
```

That gives you **3-2-1 backup strategy**.

---

# 7️⃣ Secondary Role (Nice Bonus)
This laptop could also act as:

- **Emergency Plex server** if your NUC fails
- **Docker learning box**
- **Network monitoring machine**

But **backup should remain its main job**.

---

# The Final Setup (Simple Version)

```
Dell Laptop
│
├─ Ubuntu Server
├─ Docker
│   ├─ Portainer
│   ├─ Duplicati
│   └─ Uptime Kuma
│
└─ Backup storage for Synology
```

---

💡 **Important tip:**  
Plug the laptop into **Ethernet and leave it always on**. Laptops actually make great low-power servers.

---

If you want, I can also show you the **PERFECT homelab layout using:**

- Your **NUC10**
- Your **NUC8**
- This **laptop**
- Your **Synology**

and turn it into a **very clean mini datacenter setup** (it’ll actually be a really solid lab for someone in IT).

**You:** Ubuntu server is ready

**ChatGPT:** Perfect. Since **Ubuntu Server is already installed**, let’s turn this into your **Synology backup server + homelab utility box** in a few clean steps. I’ll keep this **simple and in the right order** so nothing breaks. 🧠

---

# Step 1 — Update the Server
First thing on any new install.

```bash
sudo apt update && sudo apt upgrade -y
```

Then install some basics:

```bash
sudo apt install curl git htop net-tools -y
```

These help with troubleshooting.

---

# Step 2 — Give the Server a Static IP
Your backup server **must not change IP**.

Find your interface:

```bash
ip a
```

You’ll see something like:

```
eth0
or
enp0s31f6
```

Edit the netplan config:

```bash
sudo nano /etc/netplan/00-installer-config.yaml
```

Example:

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s31f6:
      dhcp4: no
      addresses: [192.168.1.50/24]
      gateway4: 192.168.1.1
      nameservers:
        addresses: [1.1.1.1,8.8.8.8]
```

Apply it:

```bash
sudo netplan apply
```

---

# Step 3 — Install Docker
We’ll use Docker for your backup tools.

```bash
curl -fsSL https://get.docker.com | sudo sh
```

Add your user to Docker:

```bash
sudo usermod -aG docker $USER
```

Then reboot:

```bash
sudo reboot
```

---

# Step 4 — Install Portainer (Docker GUI)
This gives you a **web dashboard to manage containers**.

```bash
docker volume create portainer_data
```

Then:

```bash
docker run -d -p 9000:9000 \
--name portainer \
--restart=always \
-v /var/run/docker.sock:/var/run/docker.sock \
-v portainer_data:/data \
portainer/portainer-ce
```

Open in browser:

```
http://SERVER-IP:9000
```

Example:

```
http://192.168.1.50:9000
```

---

# Step 5 — Create Backup Storage Folder

```bash
mkdir ~/backups
```

or better:

```bash
sudo mkdir /backup
sudo chmod 777 /backup
```

---

# Step 6 — Install Duplicati (Backup Software)

```bash
docker run -d \
--name duplicati \
-p 8200:8200 \
-v /backup:/backups \
-v /home:/source \
--restart unless-stopped \
lscr.io/linuxserver/duplicati
```

Open:

```
http://SERVER-IP:8200
```

This is where your **Synology will send backups**.

---

# Step 7 — Set Up Synology Backup
On your Synology:

Open **Hyper Backup**

Choose:

```
Rsync Server
```

Destination:

```
Laptop IP
```

Example:

```
192.168.1.50
```

Now your NAS backs up **to this laptop automatically**.

---

# Step 8 — Install Uptime Kuma (Optional but Awesome)

This monitors your servers.

```bash
docker run -d \
--name uptime-kuma \
-p 3001:3001 \
-v uptime-kuma:/app/data \
--restart=always \
louislam/uptime-kuma
```

Open:

```
http://SERVER-IP:3001
```

---

# What This Laptop Now Does
Your **backup server now runs:**

```
Ubuntu Server
│
├─ Docker
│   ├─ Portainer (docker management)
│   ├─ Duplicati (backup system)
│   └─ Uptime Kuma (monitoring)
│
└─ Backup storage for Synology
```

---

# Next Level (Optional but VERY Cool)
Later we could add:

• **Pi-hole** → network ad blocking  
• **WireGuard** → remote access VPN  
• **Syncthing** → device sync  
• **Immich** → Google Photos replacement  
• **Nextcloud** → private cloud

This would make your homelab **extremely legit**.

---

✅ If you want, I can also show you **one trick that makes your homelab 10x cleaner**:

A **single Docker stack that manages all your containers automatically**. It makes managing servers way easier.
