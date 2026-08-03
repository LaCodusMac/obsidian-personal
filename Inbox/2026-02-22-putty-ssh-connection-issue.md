---
date: 2026-02-22
source: chatgpt
title: "PuTTY SSH Connection Issue"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Why can’t my windows laptop putty into the Linux server

**ChatGPT:** Alright Jake — since you’ve got NUCs and a Synology in your setup, let’s troubleshoot this the way you would on a ticket. 👇  

When **PuTTY can’t SSH into a Linux server**, it’s almost always one of these:

---

## 1️⃣ SSH Service Not Running on the Linux Box

On the Linux server, check:

```bash
sudo systemctl status ssh
```

or

```bash
sudo systemctl status sshd
```

If it’s not active:

```bash
sudo systemctl start ssh
sudo systemctl enable ssh
```

If SSH isn’t installed:

```bash
sudo apt install openssh-server
```

---

## 2️⃣ Wrong IP Address

From your Windows laptop:

```powershell
ping <linux-ip>
```

On the Linux machine:

```bash
ip a
```

Make sure:
- You’re using the correct IP
- It hasn’t changed (DHCP issue?)
- You’re not accidentally trying the public IP internally

If this is one of your Intel NUCs, double-check it didn’t grab a new DHCP lease.

---

## 3️⃣ Firewall Blocking Port 22

On Linux:

### If using UFW:
```bash
sudo ufw status
```

Allow SSH:
```bash
sudo ufw allow ssh
```

### If using firewalld:
```bash
sudo firewall-cmd --list-all
```

---

## 4️⃣ Network / VLAN Issue (Since You’re Into Home Lab Stuff)

If:
- Windows is on one VLAN
- Linux server is on another
- Inter-VLAN routing isn’t configured

You won’t connect.

Test:

```powershell
Test-NetConnection <linux-ip> -Port 22
```

If ping works but port 22 fails → firewall or SSH service issue  
If ping fails → routing or wrong subnet

---

## 5️⃣ Wrong Username

PuTTY won’t tell you clearly sometimes.

Common mistake:
- Trying to log in as `root` when root login is disabled.

Check on Linux:

```bash
sudo nano /etc/ssh/sshd_config
```

Look for:

```
PermitRootLogin no
```

If it says no → use your regular user.

---

## 6️⃣ SSH Config Blocking You

In `/etc/ssh/sshd_config`, check:

```
AllowUsers
```

If your user isn’t listed, you won’t get in.

---

## 7️⃣ Port Changed

Maybe SSH isn’t on port 22.

Check:

```bash
sudo grep Port /etc/ssh/sshd_config
```

If it says something like:

```
Port 2222
```

You need to specify that in PuTTY.

---

## 8️⃣ Windows Firewall (Rare but Happens)

Make sure outbound 22 isn’t blocked:

```powershell
Test-NetConnection <linux-ip> -Port 22
```

---

# Quick Triage Flow

Tell me what error PuTTY shows:

- 🔴 “Connection refused” → SSH not running  
- 🔴 “Network error: Connection timed out” → Firewall / routing  
- 🔴 “Access denied” → Username/password issue  
- 🔴 “No route to host” → Wrong subnet  

---

Since you’re running a homelab with NUCs and a rack setup — is this:
- A fresh Linux install?
- A server you moved to a different VLAN?
- Something behind your Synology or a different gateway?

Give me the exact PuTTY error and we’ll zero in fast.
