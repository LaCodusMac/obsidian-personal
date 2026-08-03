---
date: 2026-07-14
source: chatgpt
title: "Intune enrollment error"
category: "Tech Support (General)"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_00000000644c71f59050576c79b4c7e9", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 586670, "width": 1152}
{"asset_pointer": "sediment://file_000000003bd0720c871e25efcf801453", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 666080, "width": 1152}
What’s this issue

**ChatGPT:** This is a **Microsoft Intune/MDM enrollment error**.

The key part of the message is:

> **"This device is already enrolled."**
> **Error code: 8018000a**

### What 8018000a means
Windows is trying to enroll the device into Intune (or another MDM), but Microsoft already believes this device is enrolled. This usually happens when there's a mismatch between:

- The device's local enrollment information
- The Intune device record
- Microsoft Entra ID (Azure AD)

This is a common issue after:
- Reinstalling Windows without removing the old Intune object
- Using Autopilot Reset/Fresh Start
- Imaging a computer
- Leaving and rejoining Entra ID
- An enrollment that failed partway through

---

## As the Intune admin, I'd check these in order:

### 1. Verify the device already exists in Intune
Search by:
- Serial number
- Device name

If it already exists:
- Retire/Delete the old object (if appropriate)
- Wait a few minutes
- Retry enrollment

---

### 2. Check Entra ID
Look for duplicate device objects.

Sometimes you'll have:
- One Entra device
- Two Intune devices

or vice versa.

---

### 3. Check Autopilot
If this is an Autopilot device:
- Verify the hardware hash isn't assigned incorrectly.
- Make sure there aren't duplicate Autopilot records.

---

### 4. Check local enrollment
If you're at OOBE or after setup, boot into Windows and run:

```cmd
dsregcmd /status
```

Look for:

- AzureAdJoined
- DeviceId
- MdmUrl

If it already shows an MDM URL, Windows thinks it's enrolled.

---

### 5. Remove old enrollment (if reusing the device)

Sometimes you need to:

- Disconnect Work or School account
- Delete the Intune object
- Delete the Entra device (if appropriate)
- Reboot
- Re-enroll

---

## If this is during Autopilot OOBE

The fastest fix is usually:

1. Delete the Intune device.
2. Delete the Entra device.
3. (Leave the Autopilot device unless you're rebuilding Autopilot.)
4. Wait 5–15 minutes.
5. Restart OOBE and try again.

---

## A few questions
1. **Is this happening during Windows Autopilot (Out-of-Box Experience), or after Windows is already set up?**
2. **Is this a brand-new device or one that was previously assigned to another user?**
3. **Is it Microsoft Entra Joined only, or Hybrid Entra Joined?**

Once I know that, I can walk you through the exact fix.

**You:** OOBE, Just wiped , it may have been hybrid joined or I may have cut it over

**ChatGPT:** That context makes this much more likely.

Since it's **during OOBE after a wipe**, and the machine **may have previously been Hybrid Entra joined before you converted it**, my suspicion is **stale Intune/Entra enrollment metadata**, not a problem with the local PC.

### Most likely causes (in order)

1. **The device still has an active Intune enrollment object** from before the wipe.
2. **There are duplicate Entra ID device objects** (one Hybrid, one Entra Joined).
3. **The Autopilot device is associated with the wrong Intune/Entra object.**
4. **The MDM certificate/enrollment wasn't fully removed before the wipe** (less common after a true reset).

### What I'd check first

#### 1. Intune → Devices → All Devices
Search by:
- Serial Number (preferred)
- Device Name

If you see multiple entries:
- One Managed
- One Retired
- One Hybrid
- One Entra Joined

that's probably your issue.

---

#### 2. Microsoft Entra Admin Center → Devices

Look for:
- Same serial/device represented twice
- One "Microsoft Entra joined"
- One "Microsoft Entra hybrid joined"

If you've intentionally migrated away from Hybrid, remove the stale Hybrid object (assuming it isn't still in use).

---

#### 3. Windows Autopilot Devices

Verify:
- The hardware hash exists only once.
- The Autopilot profile is still assigned correctly.

Normally you **do not delete the Autopilot object** unless you're intentionally removing it from Autopilot.

---

### If you just cut this device over from Hybrid to Entra Join

I've seen this exact error when:
- Hybrid device still exists
- Intune still thinks the previous MDM enrollment is active
- OOBE attempts a brand-new enrollment
- Intune responds with **8018000a ("already enrolled")**

Deleting the stale Intune device and stale Entra device (not the Autopilot record) usually resolves it after waiting 5–15 minutes for replication.

### One question

**How did you wipe it?**
- **Autopilot Reset**
- **Windows Reset ("Reset this PC")**
- **USB install media**
- **Fresh Start**
- **Wipe command from Intune**

That answer changes the next troubleshooting step.

**You:** It had an active profile but we deleted it last night and waited to see if it would work but same issue

**ChatGPT:** Given that, I'd stop focusing on the local machine and start looking at the service side.

Since:
- ✅ Device was wiped
- ✅ Intune device was deleted yesterday
- ✅ You waited overnight
- ✅ OOBE still fails with **8018000a**

there's likely another object that's still telling Intune the device is enrolled.

### Here's what I'd check next:

#### 1. Is there an Entra device that wasn't deleted?
Sometimes deleting the Intune object leaves the Microsoft Entra device behind.

Check:
- Microsoft Entra Admin Center → Devices → All devices
- Search by:
  - Serial number
  - Device name
  - Hardware ID (if known)

If you see an old Hybrid or Entra device, delete it if it's no longer in use.

---

#### 2. Check for duplicate Intune objects
In Intune, search by:
- Serial Number
- Device Name
- User

Sometimes one object is hidden by filters or there are multiple records with different names.

---

#### 3. Check Windows Autopilot Devices
Is the device still present there?

If yes:
- Is it assigned the correct profile?
- Is there only one hardware hash?

Normally you **leave the Autopilot object**, but if there are duplicate Autopilot registrations, enrollment can fail.

---

#### 4. Check Enrollment Restrictions
I've seen 8018000a appear when the device is matching an existing enrollment because of an old record.

Also verify:
- Device enrollment limit for the user hasn't been reached.
- The user isn't blocked by an enrollment restriction.

---

#### 5. Was the device ever converted from Hybrid to Entra using the same Windows install?
This is the one detail that catches my attention.

If the device:
- Started as Hybrid
- Was converted to Entra Join
- Was later wiped

I've occasionally seen stale registration survive in Microsoft's backend. In those cases, removing **both** the Intune and Entra objects (and confirming only one Autopilot record exists) resolved it.

---

### One thing I'd have you check immediately

Open the device in **Windows Autopilot Devices** and tell me:

- Does it show **Assigned**?
- What is the **Profile Status**?
- Is there an **Associated Intune Device** listed? If so, does it point to a device that no longer exists?

That association is often the clue with this exact error.

Also, **how was the wipe performed?** Was it:
- An **Intune Wipe** command,
- **Reset this PC**,
- Or a **USB installation of Windows**?

That can narrow down whether this is an Autopilot registration issue or an Intune enrollment issue.
