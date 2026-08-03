---
date: 2026-05-11
source: chatgpt
title: "Enable SSH Ubuntu"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** How to enable ssh on Ubuntu desktop

**ChatGPT:** On Ubuntu Desktop, SSH is usually just disabled because the SSH server isn’t installed yet.

Open Terminal and run:

```bash
sudo apt update
sudo apt install openssh-server -y
```

Then enable and start SSH:

```bash
sudo systemctl enable ssh
sudo systemctl start ssh
```

Check that it’s running:

```bash
sudo systemctl status ssh
```

You should see:

```text
active (running)
```

Now find your Ubuntu machine’s IP:

```bash
ip a
```

Look for something like:

```text
192.168.1.xxx
```

Then from another device:

### From Mac/Linux
```bash
ssh yourusername@192.168.1.xxx
```

### From Windows
Use:
- PowerShell:
```powershell
ssh yourusername@192.168.1.xxx
```
- or entity["software","PuTTY","SSH client for Windows"]

If the firewall is enabled on Ubuntu Desktop, allow SSH:

```bash
sudo ufw allow ssh
```

Then verify:

```bash
sudo ufw status
```

For your homelab setup with Plex/Docker on Ubuntu, SSH is the best way to manage the NUC remotely instead of constantly using a monitor/keyboard locally.

**You:** How to get user name from cli

**ChatGPT:** Run:

```bash id="h7r0v8"
whoami
```

That prints your current username.

Example:

```text id="0qj0uo"
ubuntu
```

You can also see all users on the system with:

```bash id="m9d0bz"
cut -d: -f1 /etc/passwd
```

Or see your full logged-in user info:

```bash id="7syg2i"
id
```
