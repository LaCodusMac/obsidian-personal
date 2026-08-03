---
date: 2025-11-24
source: chatgpt
title: "Fix UniFi AP connection"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** i can not access my old unigi controller that ym ap keeps connecting to my

**ChatGPT:** Got you — this usually happens when an AP keeps trying to re-join an old UniFi controller it was previously adopted by. That controller still has its “inform URL” stored on the AP, so even if you can’t access that controller anymore, the AP keeps phoning home to it.

Here’s how to fix it depending on what you **can** still access.

---

# ✅ **Fix: Point AP Away From Old Controller + Adopt to Your NUC**

### **Step 1 — SSH Into the AP**
You need the AP’s IP address (check your router/DHCP leases).

Then SSH into it:

```
ssh ubnt@<AP-IP>
```

**Default password** (if never changed):  
`ubnt`  
If it was adopted before, it will be whatever password the old controller set — but you can still reset it (explained below).

---

# ❗ If You CANNOT SSH Into the AP
That means the old controller set a custom device password and you don’t know it.

**Solution → Factory Reset the AP**

1. Hold the reset button **10 seconds** until the light flashes.  
2. Wait ~1 minute.  
3. It will reboot into factory state with defaults.

**Then you CAN SSH using:**
```
username: ubnt
password: ubnt
```

---

# ✅ **Step 2 — Point the AP to Your New Controller**
Your NUC running Ubuntu + Docker will have a new IP (ex: `192.168.1.X`).

Once connected to the AP via SSH:

```
set-inform http://<NUC-IP>:8080/inform
```

**Run it TWICE** — UniFi always expects the second confirmation.

Example:

```
set-inform http://192.168.1.50:8080/inform
set-inform http://192.168.1.50:8080/inform
```

Your AP should now appear as **Pending Adoption** in your new UniFi controller.

---

# ❗ If your controller is running UniFi Network Application 9.x
Your AP may show up but adoption may fail unless firmware matches.  
If this happens, tell me the AP model and controller version — I’ll give exact firmware steps.

---

# ❗ If Your AP STILL Keeps Connecting to Old Controller
That means the old controller is still online somewhere on your network — often:

- Old Windows service still running  
- Old Docker container auto-starting  
- Old UniFi installed on a laptop  
- Something using port **8080** is running

Tell me **what devices you’ve ever run UniFi on**, and I’ll help you kill the old controller completely.

---

# If you want, I can also:
✅ Show you the clean install steps for UniFi Controller on your NUC Docker  
✅ Make sure ports and volumes are correct  
✅ Help you adopt your switch/APs cleanly  
Just tell me your NUC’s IP and your AP model.
