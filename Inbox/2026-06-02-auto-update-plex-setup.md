---
date: 2026-06-02
source: chatgpt
title: "Auto-update Plex Setup"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** how to setup auto update

**ChatGPT:** If you're talking about your Plex Docker container on Ubuntu, the easiest way is to use **Watchtower**. Your current Plex container is already configured to restart automatically after reboots with `--restart unless-stopped`. fileciteturn1file0

### Install Watchtower

```bash
docker run -d \
  --name watchtower \
  --restart unless-stopped \
  -v /var/run/docker.sock:/var/run/docker.sock \
  containrrr/watchtower \
  --cleanup \
  --interval 86400
```

This will:

- Check for container updates every 24 hours
- Pull new Plex images automatically
- Stop and recreate Plex with the new image
- Remove old images to save space

### Verify It's Running

```bash
docker ps
docker logs watchtower
```

### Force a Check Right Now

```bash
docker exec watchtower /watchtower --run-once
```

### Alternative: Plex Auto-Updates Only

If you only want Plex updated and not other containers:

```bash
docker run -d \
  --name watchtower \
  --restart unless-stopped \
  -v /var/run/docker.sock:/var/run/docker.sock \
  containrrr/watchtower plex \
  --cleanup \
  --interval 86400
```

Since you're running a homelab with Plex, Home Assistant, and other services, I usually recommend:
- **Auto-update Plex** ✅
- **Do NOT auto-update Home Assistant or infrastructure containers** ❌
- Review and update those manually

Want me to show you how to set up **automatic Ubuntu security updates** too? That's another good thing to enable on your Plex NUC.

**You:** No for my pc with ubuntu desk top

**ChatGPT:** For **Ubuntu Desktop**, you can enable automatic security updates with Ubuntu's built-in unattended-upgrades package.

### Install it

```bash
sudo apt update
sudo apt install unattended-upgrades
```

### Enable automatic updates

```bash
sudo dpkg-reconfigure --priority=low unattended-upgrades
```

Select **Yes** when prompted.

### Verify it's enabled

```bash
sudo systemctl status unattended-upgrades
```

### Check the configuration

```bash
sudo nano /etc/apt/apt.conf.d/50unattended-upgrades
```

Most people leave the defaults, which install security updates automatically.

### Enable automatic package list updates

```bash
sudo nano /etc/apt/apt.conf.d/20auto-upgrades
```

Make sure it contains:

```text
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "1";
```

### Reboot automatically after updates (optional)

If this machine is your AI workstation or homelab box, I would **not** automatically reboot it.

If you want automatic reboots:

```bash
sudo nano /etc/apt/apt.conf.d/50unattended-upgrades
```

Uncomment:

```text
Unattended-Upgrade::Automatic-Reboot "true";
```

### Test it

```bash
sudo unattended-upgrade --dry-run --debug
```

For your Ubuntu Desktop machine running Ollama/Open WebUI/OpenClaw, I'd recommend:

- Automatic **security** updates: ✅
- Automatic **application** updates: ✅
- Automatic **reboots**: ❌
- Manual reboot once every week or two: ✅

That gives you the security benefits without unexpectedly interrupting AI workloads.

**You:** can I set manual reboots for Sunday 2 AM

**ChatGPT:** Yes. On Ubuntu, a simple and reliable way is a weekly cron job.

### Open root's crontab

```bash
sudo crontab -e
```

Add this line:

```bash
0 2 * * 0 /sbin/shutdown -r now
```

This means:

- Minute: `0`
- Hour: `2`
- Day of month: `*`
- Month: `*`
- Day of week: `0` (Sunday)

→ Reboot every Sunday at **2:00 AM**.

### Verify

```bash
sudo crontab -l
```

You should see:

```bash
0 2 * * 0 /sbin/shutdown -r now
```

### Alternative (systemd timer)

More modern Ubuntu approach:

```bash
sudo systemctl edit --force --full sunday-reboot.timer
```

But honestly, for a simple weekly reboot, cron is perfectly fine.

### For your homelab

On the Ubuntu Desktop box running Ollama/Open WebUI/OpenClaw, I'd do:

- Automatic security updates ✅
- Weekly reboot Sunday 2 AM ✅
- Keep the machine powered on 24/7 ✅

Before relying on the reboot, make sure your AI services start automatically after boot:

```bash
systemctl status ollama
docker ps
```

If Open WebUI is running in Docker and Ollama is a systemd service, they'll come back up automatically after the Sunday reboot.

**You:** 0 2 * * 0 /sbin/shutdown -r now
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command
carlthellama@llamaswithhats:~$

**ChatGPT:** You're currently **inside the editor**. The cron entry looks correct.

If you're using **nano**:

1. Press **Ctrl + O** (write out/save)
2. Press **Enter** to confirm the filename
3. Press **Ctrl + X** to exit

Then verify it saved:

```bash
sudo crontab -l
```

You should see:

```text
0 2 * * 0 /sbin/shutdown -r now
```

You can also check that cron is running:

```bash
sudo systemctl status cron
```

You should see **active (running)**.

Since this is your Ubuntu Desktop AI box, I'd also test that everything comes back after a reboot:

```bash
sudo reboot
```

After it comes back up, check:

```bash
systemctl status ollama
docker ps
```

to make sure Ollama, Open WebUI, Plex, or any other services you care about start automatically.
