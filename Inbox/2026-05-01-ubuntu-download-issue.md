---
date: 2026-05-01
source: chatgpt
title: "Ubuntu download issue"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Why is Ubuntu server website going to site can’t be reached when I hit download button on 2 devices

**ChatGPT:** This usually isn’t *your devices*—it’s either a broken redirect, DNS issue, or Canonical’s mirror acting up. Let’s narrow it down fast.

---

## 🔥 Most common cause (what this smells like)
When you click download on the entity["software","Ubuntu Server","operating system"] site, it redirects you to a mirror (like `releases.ubuntu.com` or a country mirror). If that redirect fails, you’ll get **“site can’t be reached”**.

If it’s happening on **2 devices**, it’s likely:
- ❌ DNS issue (very common with Pi-hole / UniFi setups)
- ❌ Network blocking (Pi-hole, firewall, or UniFi config)
- ❌ Temporary Ubuntu mirror outage

---

## ⚡ Quick test (do this right now)
Try opening this **direct link** (bypasses the main site):

👉 https://releases.ubuntu.com/22.04/ubuntu-22.04.4-live-server-amd64.iso

### What happens?
- ✅ Works → your issue = redirect/DNS problem  
- ❌ Doesn’t work → network/DNS blocking or outage  

---

## 🧠 Given your setup… I’m 90% sure it’s THIS:
You’re running:
- Pi-hole  
- UniFi  
- Custom DNS  

That combo = very easy to accidentally block Ubuntu mirrors.

---

## 🔍 Check Pi-hole (high probability fix)
1. Go to Pi-hole dashboard  
2. Look at **Query Log**  
3. Search for:
   - `ubuntu.com`
   - `releases.ubuntu.com`
   - `canonical.com`

If you see **blocked (gravity/adlist)** → that’s your problem

### Fix:
- Whitelist:
  - `ubuntu.com`
  - `releases.ubuntu.com`
  - `security.ubuntu.com`

---

## 🌐 Quick bypass test (to confirm)
On one device:
- Turn off WiFi → use cellular  
OR  
- Change DNS to:
  - `8.8.8.8` (Google)
  - `1.1.1.1` (Cloudflare)

If it suddenly works → 💥 confirmed DNS/Pi-hole issue

---

## 🛠️ Other possible causes (less likely)
- Browser extensions blocking redirects  
- UniFi content filtering  
- Ubuntu mirror temporarily down (rare, but happens)

---

## 🧪 If you want a clean homelab-friendly fix
Since you’re doing Plex + mounts + servers (I see your setup in your notes fileciteturn0file2), you should:

- Keep Pi-hole  
- But **relax blocking for dev/sysadmin domains**
- Or create a group like:
  - “Infra whitelist”

---

## 👍 My blunt take
This is almost certainly your **Pi-hole or DNS setup blocking Ubuntu mirrors**, not Ubuntu itself.

---

If you want, I can:
- Check your Pi-hole config step-by-step  
- Or give you a clean DNS setup that won’t break downloads again  

Just tell me what you see when you hit that direct link.
