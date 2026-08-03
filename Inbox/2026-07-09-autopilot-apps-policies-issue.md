---
date: 2026-07-09
source: chatgpt
title: "Autopilot Apps Policies Issue"
category: "Tech Support (General)"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_000000003990720cb64489f69b352abe", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 496023, "width": 1152}

**ChatGPT:** From your screenshot, Autopilot itself appears to have progressed, but the **Apps and policies** phase is stuck on the **Sidecar** policy provider.

The important part is:

- ✅ **Provider Tracking List Retrieval** – Success
- ✅ **Provider Installation** – Success
- ⚠️ **Installation** – **Current status of this resource event is unknown**
- **Finish Time:** Not available

This usually means one of a few things:

1. **An Intune policy or app is hanging**
   - An app install never reported success or failure.
   - A Win32 app detection rule isn't completing.
   - A PowerShell script is stuck.

2. **The Intune Management Extension (IME) isn't processing correctly**
   - The Sidecar provider is the Intune Management Extension used for Win32 apps and scripts.

3. **Network/connectivity issue**
   - Device can't reach Intune or download content.
   - Proxy/firewall issue.

## As the Intune admin, I'd check:

- **Intune → Devices → Windows → Enrollment Status Page**
  - Which app is required during ESP?
- **Device → Managed Apps**
  - Is a Win32 app stuck "Installing"?
- **Device → Scripts**
  - Any PowerShell scripts pending?
- **IntuneManagementExtension.log**
  - Usually the fastest way to identify the culprit.

## On the device

Press **Shift + F10** and run:

```cmd
dsregcmd /status
```

Verify the device is:

```
AzureAdJoined : YES
DeviceAuthStatus : SUCCESS
```

Then check the IME service:

```cmd
sc query IntuneManagementExtension
```

It should be:

```
STATE : RUNNING
```

You can also open:

```
C:\ProgramData\Microsoft\IntuneManagementExtension\Logs\
```

and inspect:

```
IntuneManagementExtension.log
```

That log almost always identifies the app or script that's hanging.

## Based on the screenshot

I don't think this is an Autopilot registration issue. It's much more likely:
- a required Win32 application,
- a PowerShell script,
- or a policy assigned during Enrollment Status Page that isn't completing.

If you're the Intune admin, could you tell me:
- Is this **user-driven Autopilot** or **pre-provisioning (white glove)**?
- Is it hanging indefinitely at **"Apps and policies"**, or does it eventually fail with an error code?
- Are you using the **new Intune sidecar/Win32 apps**, or mostly Microsoft Store apps?

Those details will narrow it down quickly.

**You:** {"asset_pointer": "sediment://file_000000003628722f999a8ca9a3488eee", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 500774, "width": 1152}

**ChatGPT:** This screenshot is actually more helpful.

The **Win32 app itself shows as installed successfully** (green check):

```
./Device/Vendor/MSFT/EnrollmentStatusTracking/Setup/Apps/Tracking/Sidecar/Win32App...
✓ Installation
```

So the application isn't what's holding up ESP.

The failure is higher up:

```
./Vendor/MSFT/DMClient/Provider/MS MDM Server
⚠ Installation
```

That points to the **MDM policy provider**, not the Win32 app.

### This usually means one of these:

1. **A configuration profile is hanging**
   - Settings Catalog
   - Administrative Templates
   - Device Restrictions
   - Security Baselines

2. **A PowerShell script or remediation is waiting**
   - Scripts assigned during enrollment
   - Endpoint Analytics remediation

3. **A policy CSP is waiting for completion**
   - Sometimes Windows never reports completion even though the policy applied.

---

## I'd check these first in Intune

### 1. Enrollment Status Page
- Devices → Windows → Enrollment
- Enrollment Status Page
- Is **Block device use until required apps and profiles are installed** enabled?

If yes, ESP is waiting on one of those required policies.

### 2. Configuration Profiles
Look at every profile assigned to this device/user.

See if one is showing:

- Pending
- Not Applicable
- Error

---

### 3. Scripts

Go to:

**Devices → Scripts and Remediations**

See if anything is:

- Running
- Pending
- Failed

---

### 4. Event Viewer (best local clue)

Open:

```
Event Viewer
Applications and Services Logs
Microsoft
Windows
DeviceManagement-Enterprise-Diagnostics-Provider
Admin
```

Look for recent events around the time enrollment started. Errors such as **404, 4042, 409, 4046, or 4047** can identify the specific CSP or policy causing the delay.

---

## If this is happening to every new Autopilot device

Then I'd suspect:

- A broken configuration profile
- A security baseline
- A recently added Settings Catalog policy
- An ESP configuration waiting for a policy that never reports completion

---

## If it's only this one laptop

I'd try:

1. Export the logs (the button shown in your screenshot).
2. Review `MDMDiagReport.html` and the IME logs.
3. If nothing obvious appears, wipe the device and retry Autopilot—occasionally the DMClient provider gets stuck during enrollment.

### One question:
**Does the device eventually fail after a timeout (for example after 60 minutes), or has it been sitting on this screen indefinitely?** That answer changes the next troubleshooting step.
