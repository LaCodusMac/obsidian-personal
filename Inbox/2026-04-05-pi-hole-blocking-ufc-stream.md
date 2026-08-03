---
date: 2026-04-05
source: chatgpt
title: "Pi-hole Blocking UFC Stream"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_00000000d7b0722fb8124c1f0932845d", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 380489, "width": 709}
Watching ufc live on my WiFi after adding pihole

**ChatGPT:** Yeah this is almost **definitely your Pi-hole blocking something UFC/ESPN needs** — not actually your internet being down.

That “Fatal Error / Station unavailable” is classic when:
- video CDN domains get blocked  
- auth/tracking endpoints get blocked (ESPN/UFC uses a LOT of them)

---

## 🔥 What’s happening (simple)
Your Pi-hole is probably blocking:
- streaming video servers  
- DRM/auth servers  
- analytics domains ESPN uses to verify playback  

So the app thinks:
> “No internet / can’t play video”

---

## ✅ Quick way to confirm (takes 10 seconds)

**Turn OFF Pi-hole temporarily:**
- Go to Pi-hole admin → Disable (5 minutes)

👉 Then try the stream again

If it works instantly → 100% Pi-hole issue

---

## 🛠️ Fix it properly (best method)

### 1. Open Pi-hole query log
- Admin panel → **Query Log**
- Try to play UFC again
- Watch for **blocked domains (red)**

---

### 2. Look for these common culprits
Whitelist anything like:

```
espn.com
espncdn.com
bamgrid.com
disneyplus.com
akamaihd.net
cloudfront.net
fastly.net
conviva.com
```

👉 Especially:
- `*.bamgrid.com` (BIG one for ESPN/UFC)
- `*.akamaihd.net` (video delivery)
- `*.cloudfront.net`

---

### 3. Add to whitelist
Go to:
- **Whitelist → Add domain**

Example:
```
*.bamgrid.com
*.espn.com
*.akamaihd.net
```

---

## ⚠️ Important (your setup specifically)
You’re running:
- Pi-hole + Unbound
- Custom network stack

So also check:
- No DNS resolution errors (you had NTP issues earlier 👀)
- Router isn’t double-filtering DNS

---

## 🧠 Pro move (what I’d do in your setup)

Since you’re running a homelab:

👉 **Create a “Streaming Bypass” group in Pi-hole**
- Assign your Apple TV / phone to it
- Loosen blocking just for those devices

This avoids breaking apps constantly

---

## 🚨 If you want fastest fix (no debugging)

Just whitelist these now:

```
*.bamgrid.com
*.espn.com
*.espncdn.com
*.akamaihd.net
*.cloudfront.net
```

---

## 💬 Real talk

Pi-hole is amazing, but:
- Streaming apps are **fragile as hell**
- UFC/ESPN is one of the worst offenders

You will hit this again unless you:
- whitelist aggressively OR
- isolate streaming devices

---

If you want, I can:
👉 Build you a **clean Pi-hole whitelist tailored for streaming + your setup**
👉 Or help you split your network (best long-term move for your lab)

**You:** Paramount plus not espn

**ChatGPT:** Got it — **Paramount+ changes the game a bit**, but the root issue is the same:

👉 **Pi-hole is blocking something Paramount+ needs to stream video**

That “Station unavailable / Fatal error” combo is *very* common with Paramount+ + ad blocking.

---

## 🔥 What Paramount+ actually uses (important)

Paramount+ relies heavily on:
- CBS domains  
- Viacom/Paramount tracking + auth  
- Video CDNs (Akamai, Fastly, etc.)

So Pi-hole blocks something → playback fails

---

## ✅ Quick confirm (same test)

Disable Pi-hole for 5 min → try again

- ✅ Works → we fix whitelist  
- ❌ Still broken → different issue (but I’d bet it works)

---

## 🛠️ What to whitelist (Paramount+ specific)

Start with these:

``` id="paramount"
paramountplus.com
cbs.com
cbsivideo.com
cbsi.com
viacomcbs.com
```

### VERY important CDNs:
``` id="cdn"
akamaihd.net
cloudfront.net
fastly.net
```

### Streaming/auth stuff:
``` id="auth"
conviva.com
omtrdc.net
scorecardresearch.com
```

---

## 🧠 Why this happens (so you understand it)

Paramount+ is dumb about blocking:

- It uses **tracking domains for video playback validation**
- If those fail → it kills the stream entirely

So Pi-hole blocks ads → app thinks:
> “Something’s wrong, shut it down”

---

## 🛠️ Best way to fix (clean method)

### Option 1 (recommended for you):
**Put your streaming devices in a relaxed Pi-hole group**

- Apple TV / phone → minimal blocking  
- Everything else → normal blocking  

👉 This fits your homelab setup perfectly

---

### Option 2 (manual grind):
- Open Query Log  
- Try to play stream  
- Whitelist anything blocked right before the crash  

---

## 🚨 One more thing (your earlier NTP/DNS issues)

You had:
> “Cannot resolve NTP server”

That tells me:
👉 Your DNS isn’t 100% clean yet

Paramount+ is VERY sensitive to:
- DNS delays
- resolution failures

So also make sure:
- Unbound is resolving properly  
- No upstream DNS failures  

---

## 💬 Real talk

Paramount+ is honestly:
- one of the **most fragile streaming apps**
- breaks easily with Pi-hole

So don’t fight it too hard — isolate it instead

---

## 👍 If you want next level

I can:
- Build you a **perfect Pi-hole config for streaming + homelab**
- Or set up **device-based bypass (cleanest solution)**

Just tell me what device you’re watching on (Apple TV? phone? browser?)
