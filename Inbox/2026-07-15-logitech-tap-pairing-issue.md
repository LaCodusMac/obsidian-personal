---
date: 2026-07-15
source: chatgpt
title: "Logitech Tap Pairing Issue"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Logitech tap with confrence room system will keeps asking to pair but will not pair with rally bar

**ChatGPT:** If the **Logitech Tap IP** continuously prompts to pair but never completes pairing with a **Rally Bar**, these are the most common causes and fixes, in order of likelihood:

### 1. Confirm what mode the Rally Bar is in (most common)
- **Microsoft Teams Rooms on Android**
- **Zoom Rooms on Android**
- **USB/BYOD mode**

The pairing process is different depending on the mode.

### 2. If it's Microsoft Teams Rooms
If both devices are already signed into Microsoft Teams Rooms, Microsoft—not Logitech—manages the pairing. In many cases, they should pair automatically if they're assigned to the same room account. Manual Bluetooth pairing may not work as expected. citeturn0search9turn0search1

### 3. Verify Bluetooth is enabled
On the Rally Bar:
- **Settings → Device Settings → Connectivity → Bluetooth**
- Ensure Bluetooth is **ON**.

Then:
- Press and hold the **Bluetooth button** on the back of the Rally Bar for **5 seconds**.
- You should see the pairing screen with a **4-character code**. citeturn0search1

### 4. Keep the devices close together
Bluetooth pairing is only intended for initial setup.
- Keep the Tap IP within **30 ft (10 m)** of the Rally Bar during pairing. citeturn0search1

### 5. Forget the previous pairing
On the Tap IP:
- Settings
- System
- Forget Device (or Unpair)
- Restart the Tap
- Start pairing again. citeturn0search5

### 6. Restart both devices
A full reboot often clears a stuck Bluetooth state:
- Reboot Rally Bar
- Reboot Tap IP
- Attempt pairing again.

### 7. Check firmware
Make sure:
- Rally Bar
- Tap IP
- CollabOS

are all running current firmware.

### 8. Factory reset (last resort)
If this is a new install or you're rebuilding the room:
- Factory reset the Rally Bar.
- Factory reset the Tap IP.
- Set up the Rally Bar first.
- Then pair the Tap IP. Logitech specifically recommends this if pairing repeatedly fails. citeturn0search1

---

### A few questions that will narrow it down quickly:

1. **Is this a Tap IP (network cable only) or a USB Tap?**
2. **Is the Rally Bar running Teams Rooms on Android, Zoom Rooms, or USB mode?**
3. **During pairing, do you actually see the Rally Bar name and 4-character code on the TV, or does it just keep spinning?**
4. **Was this room working before, or is it a brand-new deployment?**

Those answers usually pinpoint the issue within a couple of steps.

**You:** We can’t get into settings because we don’t have admin

**ChatGPT:** If you **can't access Settings because you don't have the admin PIN/password**, your options are fairly limited.

Here are the things you *can* try:

1. **Reboot both the Rally Bar and Tap IP** by unplugging power for about 30 seconds, then powering them back on. Sometimes they'll automatically reconnect if they were previously paired.

2. **Check that both devices are on the same network** (for a Tap IP deployment). If one device is on a different VLAN or subnet and they were factory reset, pairing may not complete.

3. **Wait a few minutes after boot.** If the Rally Bar is still provisioning or signing into Teams/Zoom, the Tap may continue to show the pairing screen until the Rally Bar is ready.

If the Tap keeps asking to pair and never completes, and you **can't enter the device settings**, then you'll need someone with one of the following:
- The **Logitech admin PIN** for the device.
- Access to **Logitech Sync**, if the organization manages the room through Sync.
- The **Microsoft Teams Rooms** or **Zoom Rooms** admin managing the room.

If none of those are available, the only remaining option is typically a **factory reset**, but that also requires setting the room back up afterward.

### A couple of questions:
- Is this a **Teams Room** or a **Zoom Room**?
- Is this a **brand-new install**, or did it stop working after a reset or update?

**You:** We tried factory reset but it didn’t work

**ChatGPT:** If you've already **factory reset both the Rally Bar and the Tap IP**, and the Tap still loops on **"Pair"** without ever connecting, it's likely no longer a simple Bluetooth issue.

Here are the most likely causes:

1. **Firmware mismatch** – One device may be running a much newer or older version of CollabOS than the other. This can prevent pairing. Without admin access, you can't verify or update it.

2. **Network issue** – If this is a **Tap IP**, after the initial Bluetooth handshake it communicates over the network. If the Tap and Rally Bar are on different VLANs, have client isolation enabled, or required ports are blocked, pairing can fail.

3. **Hardware issue** – It's uncommon, but either the Bluetooth radio or another component in the Tap or Rally Bar may have failed.

### I'd check these next:
- Is the **Rally Bar displaying a pairing code** on the TV, or does it never get that far?
- Does the **Tap actually find the Rally Bar**, or does it just keep searching?
- Is this **Teams Rooms on Android** or **Zoom Rooms**?
- After the factory reset, did both devices go through their full setup and receive IP addresses?

If the Tap **sees the Rally Bar, you enter the code, and it just spins before failing**, that strongly suggests a **CollabOS version mismatch** or a **network communication problem**, not Bluetooth itself.

Can you describe exactly where it gets stuck?
- **A.** "Searching for devices"
- **B.** It finds the Rally Bar, you enter the code, then it never completes.
- **C.** It pairs briefly, then immediately asks to pair again.

That distinction will narrow it down quickly.

**You:** How to reset

**ChatGPT:** If you need to **factory reset a Logitech Rally Bar or Tap IP**, here are the standard methods:

### Rally Bar
1. Leave the Rally Bar powered on.
2. Locate the **small reset pinhole** on the back of the Rally Bar.
3. Press and hold the reset button with a paperclip for **10–15 seconds**.
4. Release it when the LED changes or the device begins rebooting.
5. Wait several minutes for the factory reset to complete.

### Tap IP
1. Keep the Tap IP powered via PoE.
2. Locate the **reset pinhole** on the back or underside of the Tap IP.
3. Press and hold the reset button for **10–15 seconds**.
4. The Tap IP will reboot and return to its out-of-box setup.

### If you've already done this
Since you mentioned you've already factory reset it and it still won't pair, another factory reset is unlikely to solve the problem. At that point I'd suspect:
- A **CollabOS firmware mismatch** between the Rally Bar and Tap IP.
- A **network configuration issue** (especially with Tap IP).
- A hardware issue with one of the devices.

One question: **Is your Tap a Tap IP (single Ethernet cable/PoE only) or the USB Tap (USB cable to the Rally Bar)?** The troubleshooting path is different depending on the model.

**You:** We did 7-10 seconds on the pinhole

**ChatGPT:** 7–10 seconds is **sometimes not long enough**. On many Logitech CollabOS devices, you should:

1. Keep the device powered on.
2. Insert a paperclip into the reset pinhole.
3. **Hold it for 15–20 seconds** (some technicians hold it until the LED changes or the reboot clearly begins).
4. Release it only after you see the device start restarting.

If it simply rebooted without returning to the initial setup wizard, it likely **didn't complete a factory reset**.

A couple of questions:
- Is this a **Rally Bar**, **Rally Bar Mini**, or **Rally Bar Huddle**?
- Is the **Tap** a **Tap IP** (Ethernet/PoE only) or a **USB Tap**?

Also, when the Tap says **"Pair"**, what exactly happens after you tap it? Does it:
- Find the Rally Bar and show a code?
- Say "Pairing..." forever?
- Fail with an error?
- Go back to the pairing screen?
