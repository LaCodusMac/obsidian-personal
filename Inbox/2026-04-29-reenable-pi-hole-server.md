---
date: 2026-04-29
source: chatgpt
title: "Reenable Pi-hole Server"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** how to reenbale my pihole server

**ChatGPT:** Alright—let’s get your Pi-hole back online. I’ll keep this practical based on your setup style (Docker + Ubuntu NUC).

---

## 🔍 First: figure out what’s actually “down”

Most Pi-hole issues fall into one of these:
- Container stopped
- DNS service not responding
- Network/IP changed
- Port conflict (53 is common)

---

## 🧠 Step 1 — Check if Pi-hole container is running

```bash
docker ps | grep pihole
```

### If you **see it running**
👉 Skip to Step 3

### If you **don’t see it**
Check stopped containers:

```bash
docker ps -a | grep pihole
```

Then start it:

```bash
docker start pihole
```

---

## 🔄 Step 2 — If container exists but won’t start

Run:

```bash
docker logs pihole
```

Common issues:
- Port 53 already in use (usually by systemd-resolved)
- Bad volume mount
- Config corruption

---

## 🌐 Step 3 — Test if DNS is actually working

From your NUC:

```bash
nslookup google.com 127.0.0.1
```

Or from another device using your Pi-hole IP:

```bash
nslookup google.com <PIHOLE-IP>
```

### If this fails:
👉 Pi-hole DNS isn’t running correctly

---

## ⚠️ Step 4 — Check for port 53 conflict (VERY common)

```bash
sudo lsof -i :53
```

If you see something like:
```
systemd-resolved
```

Fix it:

```bash
sudo systemctl disable systemd-resolved
sudo systemctl stop systemd-resolved
```

Then update resolv.conf:

```bash
sudo rm /etc/resolv.conf
echo "nameserver 1.1.1.1" | sudo tee /etc/resolv.conf
```

Restart Pi-hole:

```bash
docker restart pihole
```

---

## 📦 Step 5 — If everything is broken, just recreate it

Sometimes faster than debugging:

```bash
docker stop pihole
docker rm pihole
```

Then run (basic working config):

```bash
docker run -d \
  --name pihole \
  -p 53:53/tcp -p 53:53/udp \
  -p 80:80 \
  -e TZ="America/New_York" \
  -e WEBPASSWORD="yourpassword" \
  -v /home/ubuntu/pihole/etc-pihole:/etc/pihole \
  -v /home/ubuntu/pihole/etc-dnsmasq.d:/etc/dnsmasq.d \
  --restart unless-stopped \
  pihole/pihole:latest
```

---

## 🔗 Step 6 — Access UI

Open:

```
http://<NUC-IP>/admin
```

---

## 🧠 Quick reality check (based on your setup)

Since you:
- Run Plex in Docker
- Use Synology mount
- Likely using UniFi network

👉 Most likely causes:
- Pi-hole container stopped after reboot
- Port 53 conflict
- IP changed after moving devices (you *just moved your Synology earlier*)

---

## 🚀 If you want, I can go deeper

Tell me:
- Are you running Pi-hole in Docker or bare metal?
- What happens when you run `docker ps`?
- Any error messages?

I can basically “remote troubleshoot” this with you step-by-step and get it fixed fast.

**You:** pihole is hosted via my raspberry pi 5.

**ChatGPT:** Got it—Pi-hole on a **Raspberry Pi 5 (not Docker)**. Let’s bring it back step-by-step without overcomplicating it.

---

## 🔍 1. Check if Pi-hole service is running

On the Pi:

```bash
pihole status
```

### You want to see:
```
DNS service is running
```

### If it says NOT running:
```bash
pihole restartdns
```

---

## 🔧 2. Check core services (this is usually the issue)

Pi-hole depends on:
- `pihole-FTL` (main DNS engine)
- `lighttpd` (web UI)

Run:

```bash
sudo systemctl status pihole-FTL
sudo systemctl status lighttpd
```

### If either is inactive:
```bash
sudo systemctl restart pihole-FTL
sudo systemctl restart lighttpd
```

---

## 🌐 3. Test DNS directly on the Pi

```bash
nslookup google.com 127.0.0.1
```

### If this fails:
👉 Pi-hole DNS is broken internally (we fix next)

---

## ⚠️ 4. Check for port 53 conflict (MOST COMMON)

```bash
sudo lsof -i :53
```

### If you see:
```
systemd-resolved
```

That’s your problem.

Fix it:

```bash
sudo systemctl disable systemd-resolved
sudo systemctl stop systemd-resolved
```

Then:

```bash
sudo rm /etc/resolv.conf
echo "nameserver 1.1.1.1" | sudo tee /etc/resolv.conf
```

Restart Pi-hole:

```bash
pihole restartdns
```

---

## 🌍 5. Make sure your network is actually using Pi-hole

Since you’re on UniFi:

Check:
- **DHCP DNS Server** → should be your Pi’s IP (e.g. `192.168.1.x`)
- Or manually set your device DNS to Pi IP

Test from your laptop:

```bash
nslookup google.com <PI-IP>
```

---

## 🔁 6. If it still doesn’t work → repair install (safe)

This won’t wipe your config:

```bash
pihole -r
```

Then choose:
```
Repair
```

---

## 🧠 Based on your situation (recent move + network changes)

Most likely causes for you:
- Pi got a **new IP**
- UniFi DHCP not pointing to Pi anymore
- DNS service stopped after reboot

---

## 🚀 Quick fastest fix (try this first)

Run this combo:

```bash
pihole restartdns
sudo systemctl restart pihole-FTL
sudo systemctl restart lighttpd
```

Then test:

```bash
nslookup google.com 127.0.0.1
```

---

## If you want fast pinpoint help

Send me:
- Output of `pihole status`
- Output of `sudo systemctl status pihole-FTL`
- Your Pi IP

I’ll tell you exactly what’s broken in one pass.

**You:** Pihole is running but I moved off of it because of issues during move

**ChatGPT:** Ahh—that actually helps a lot. Your Pi-hole itself is fine, your **network just isn’t using it anymore** after the move.

Let’s flip everything back cleanly.

---

## 🧠 What likely happened
When you moved:
- Your Pi got a **new IP**
- Your **UniFi DHCP/DNS stopped pointing to Pi-hole**
- Your devices switched to automatic DNS (or ISP DNS)

So Pi-hole is running… just not being used.

---

## 🔍 Step 1 — Find your Pi-hole IP

On the Raspberry Pi:

```bash
hostname -I
```

You’ll get something like:
```
192.168.1.50
```

👉 That’s your Pi-hole IP now

---

## 🌐 Step 2 — Point your network back to Pi-hole (UniFi)

In your UniFi controller:

Go to:
```
Settings → Networks → LAN → DHCP
```

Set:
```
DHCP Name Server → Manual
```

Enter:
```
<PIHOLE-IP>
```

Example:
```
192.168.1.50
```

Save it.

---

## 🔄 Step 3 — Force devices to pick it up

EITHER:
- Restart devices  
OR
- On your laptop:

```bash
ipconfig /flushdns   # Windows
```

or

```bash
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder  # Mac
```

---

## 🧪 Step 4 — Test it

From your laptop:

```bash
nslookup google.com
```

You should see:
```
Server: 192.168.1.50
```

---

## 📊 Step 5 — Confirm in Pi-hole UI

Open:
```
http://<PIHOLE-IP>/admin
```

👉 You should start seeing queries instantly

---

## ⚠️ Optional but IMPORTANT (recommended)

### 🔒 Give Pi-hole a static IP

If you don’t do this, it’ll break again later.

In UniFi:
```
Clients → Raspberry Pi → Settings → Fixed IP
```

---

## 🚀 If you want a better setup (your level)

Since you’re running:
- UniFi
- Plex + NAS
- Multiple services

👉 Best practice:

- Keep Pi-hole as DNS
- Add fallback DNS (optional):
  ```
  192.168.1.50, 1.1.1.1
  ```
- OR run **secondary Pi-hole later** (high availability)

---

## 🧠 Reality check (your exact issue)

You didn’t “break” Pi-hole.

You just:
> moved networks → DHCP reset → Pi-hole got bypassed

Super common.

---

## If it still doesn’t work

Tell me:
- Your Pi IP
- Screenshot of UniFi DNS settings  
- Output of `nslookup google.com`

I’ll pinpoint it instantly.

**You:** whwere in unifi do i eneter the pihole ip

**ChatGPT:** You’re in the right place to ask this—UniFi hides it a bit depending on the UI version. I’ll walk you exactly where to click.

---

## 🎯 Where to enter Pi-hole IP in UniFi

### ✅ Go here:

```text
Settings → Networks → (Your LAN network)
```

Usually called:
- “LAN”
- or your custom network name

---

## 🔧 Inside that network, find:

Scroll until you see:

```text
DHCP Service Management
```

Then look for:

```text
DHCP Name Server
```

---

## ✏️ Change it to:

```text
Manual
```

Then enter your Pi-hole IP:

```text
192.168.1.xxx   ← your Pi
```

---

## 📌 Example:

| Setting | Value |
|--------|------|
| DHCP Name Server | Manual |
| DNS Server | 192.168.1.50 |

---

## 💾 Save it

Hit **Apply Changes**

---

## 🔄 VERY IMPORTANT (people miss this)

Devices won’t switch immediately.

Do one of these:
- Toggle WiFi off/on on your phone/laptop  
- Reboot devices  
- Or wait for DHCP lease renewal

---

## 🧪 Verify it worked

On your computer:

```bash
nslookup google.com
```

You should see:

```text
Server: 192.168.1.50
```

---

## 🧠 If you don’t see “DHCP Name Server”

You might be in a different UniFi UI version.

Try this path instead:

```text
Settings → Internet → WAN → DNS Server
```

⚠️ But note:
- That sets DNS for **the router itself**, not clients
- You WANT the DHCP/LAN setting

---

## 🚀 Bonus (recommended for your setup)

Once it’s working:

👉 Set a **fixed IP** for your Pi

```text
Clients → Raspberry Pi → Settings → Fixed IP
```

So it never breaks again after reboot/move.

---

If you want, send me a screenshot of your UniFi screen—I’ll point exactly where to click based on your version.

**You:** acobmcnamara@Jacobs-MacBook-Air ~ % nslookup google.com
Server:		192.168.1.1
Address:	192.168.1.1#53

Non-authoritative answer:
Name:	google.com
Address: 142.250.188.14

**ChatGPT:** Perfect—that output tells us exactly what’s wrong:

👉 Your device is still using **your router (192.168.1.1)** for DNS  
👉 NOT your Pi-hole

So UniFi hasn’t been updated (or your device hasn’t picked it up yet)

---

## 🔧 Let’s fix it cleanly

### ✅ Step 1 — Go to the correct UniFi setting

Open your UniFi Controller and go to:

```text
Settings → Networks → LAN
```

(Click your main LAN network)

---

### 🔍 Step 2 — Find this section

Look for:

```text
DHCP Service Management
```

Then:

```text
DHCP Name Server
```

---

### ✏️ Step 3 — Change it

Set:

```text
DHCP Name Server → Manual
```

Enter your Pi-hole IP:

```text
192.168.1.X   ← your Raspberry Pi
```

Save changes.

---

## 🔄 Step 4 — FORCE your Mac to update (this is why it still shows 192.168.1.1)

On your Mac:

### Option 1 (fastest)
Turn WiFi OFF → ON

### Option 2 (terminal)
```bash
sudo killall -HUP mDNSResponder
```

---

## 🧪 Step 5 — Test again

Run:

```bash
nslookup google.com
```

### You WANT to see:
```text
Server: 192.168.1.X   ← Pi-hole
```

---

## 🚨 If it STILL shows 192.168.1.1

Then one of these is happening:

### 1. DHCP setting didn’t apply
- Double-check UniFi saved correctly

### 2. You edited the wrong network
- Make sure it's your **active LAN**, not guest/VLAN

### 3. Mac has manual DNS set

Check:

```text
System Settings → Network → WiFi → Details → DNS
```

If you see anything manually set:
👉 Remove it or replace with Pi IP

---

## 🧠 Quick sanity check (important)

Try this:

```bash
nslookup google.com 192.168.1.X
```

(Replace with Pi IP)

### If this works:
👉 Pi-hole is fine  
👉 Problem is 100% UniFi/DHCP

---

## 💡 Your exact situation

You:
- Moved setup
- UniFi reset DHCP behavior
- Devices fell back to router DNS

Super normal—nothing is broken.

---

If you want, send a screenshot of your UniFi “Networks” page and I’ll literally point to the exact toggle you need 👍

**You:** the pihole ip came up

**ChatGPT:** Nice—that’s exactly what you want 👍

If your `nslookup` now shows your Pi-hole IP as the server, that means:

✅ UniFi DHCP is correctly pointing to Pi-hole  
✅ Your device is using Pi-hole for DNS  
✅ Pi-hole is effectively “back online”

---

## 🔍 Quick final checks (worth doing)

### 1. Open Pi-hole dashboard

Go to:
```
http://<PIHOLE-IP>/admin
```

👉 You should see **queries coming in live**

---

### 2. Test ad blocking

Try visiting:
```
http://doubleclick.net
```

👉 It should fail to load or be blocked

---

### 3. Confirm from another device

On your phone (on WiFi):
- Open a browser → go to Pi-hole dashboard  
- Or just browse normally and check if ads are reduced

---

## ⚠️ One thing most people forget

### 🔒 Make sure your Pi-hole IP is STATIC

If not, this will break again later.

In UniFi:
```
Clients → Raspberry Pi → Settings → Fixed IP
```

---

## 🧠 Optional upgrade (based on your setup)

Since you’re running:
- UniFi
- Plex server
- Synology

👉 You could level this up with:
- **Backup DNS (secondary Pi-hole later)**
- Or temporary fallback:
  ```
  192.168.1.X, 1.1.1.1
  ```

---

## 🚀 You’re back

At this point:
> Your network is routing DNS through Pi-hole again

If you notice anything weird (slow DNS, apps not loading, etc.), I can help you tune it—but you’re fully functional now.
