---
date: 2026-04-19
source: chatgpt
title: "Synology SHR Degraded Issue"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import, project/531-tracker]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_000000001d74722fad0b38721454412e", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 521346, "width": 1152}
{"asset_pointer": "sediment://file_000000006bf8722f9180eb59bc23c5e3", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 515254, "width": 1152}
{"asset_pointer": "sediment://file_000000000e7471f5af253c9cd6967406", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 531379, "width": 1152}

**ChatGPT:** Alright — this is actually a *very specific and important* Synology situation, and you didn’t break anything. Let’s walk through what’s really going on.

---

## 🔴 What your screen is telling you (in plain English)

- **“Storage pool has degraded”**
- RAID type: **SHR (1-drive fault tolerance)**
- **Number of drives: 1**
- Drive status: **Healthy**

👉 Translation:
You **used to have more than 1 drive in this pool**, and now one is missing.

---

## 🧠 Why this happens

SHR (Synology Hybrid RAID) with 1-drive protection means:
> “I need at least 2 drives to protect data.”

Right now:
- You only have **ONE drive installed**
- So the system says:
  > “I can’t protect your data anymore → degraded”

---

## 🚨 Important: Your data is NOT gone

- Your drive shows **Healthy**
- Your volume still shows data (1.6 TB used)
- This is **NOT a failure**, it’s a **missing redundancy issue**

---

## 🔍 What likely happened (based on your move)

Since you said:
> “I just moved my Synology”

Most likely:
- A second drive:
  - got removed  
  - got unplugged  
  - or is in another device / not reinserted  

---

## ✅ What you should do next (choose your situation)

### 🟢 Option 1 — You HAVE another drive
👉 Best case

1. Power off NAS
2. Reinsert the missing drive (or add a new one)
3. Boot up
4. Go to:
   - **Storage Manager → Storage Pool**
5. Click:
   - **Repair**

✔ This will rebuild your redundancy

---

### 🟡 Option 2 — You DON’T have another drive anymore
👉 You removed it intentionally or lost it

Then you have 2 choices:

#### Option A — Add a new drive (recommended)
- Buy another drive (same size or bigger)
- Insert it
- Click **Repair**

#### Option B — Convert to single-drive (no protection)
- This removes redundancy permanently
- Risk: if this drive dies → **data gone**

If you want this route, I’ll walk you through safely

---

## ⚠️ What NOT to do

- ❌ Do NOT delete the storage pool  
- ❌ Do NOT reinitialize anything  
- ❌ Do NOT click random repair options without confirming  

You’re in a **recoverable state right now**

---

## 🔧 Quick sanity check for you

Answer these:

1. Did you previously have **2 drives installed**?
2. Do you physically only see **1 drive in the NAS right now**?
3. Do you still have the other drive somewhere?

---

## 💡 My read based on your setup

Since you run:
- Plex on Synology storage  
- Just moved equipment  

👉 I’m **90% sure a second drive is missing/unmounted**, not failed.

---

If you want, send a pic of:
- The **front or inside of the NAS bays**

I’ll tell you *exactly* what’s going on and what button to press next.

**You:** Both are plugged in

**ChatGPT:** Good — that changes things. If **both drives are physically plugged in** but Synology only shows **1 drive in the pool**, then we’re dealing with a **detection / membership issue**, not just “missing hardware.”

Let’s narrow it down quickly.

---

## 🔍 What your screenshot tells me

- Storage pool: **Degraded**
- RAID: **SHR (1-drive protection)**
- DSM sees only:
  - **Drive 2 (3.6 TB) → Healthy**
- It explicitly says:
  > **Insufficient number of drives: 1**

👉 That means:
**Synology does NOT see the second drive as part of this pool** (or possibly not at all)

---

## 🚨 Most likely causes (ranked)

### 1. Drive is physically detected but NOT in the pool
- Shows up as:
  - “Not initialized”
  - “Unused”
  - “Available”

### 2. Drive is NOT being detected at all
- Loose SATA/backplane connection (very common after moving)
- Drive not fully seated

### 3. Drive failed during/after move
- Would show:
  - “Crashed”
  - “Not initialized”
  - or not appear

---

## ✅ Do this RIGHT NOW (takes 1 minute)

### Go to:
👉 **Storage Manager → HDD/SSD**

Tell me what you see for:

- Drive 1
- Drive 2

Specifically:
- Do you see **two drives listed**?
- What is the status of the second one?

---

## 🔧 Quick physical check (important after moving)

Before clicking anything in DSM:

1. **Power off the NAS**
2. Pull both drives out slightly
3. Firmly reseat them (push all the way in)
4. Power back on

👉 This fixes this issue *a lot more often than you’d think*

---

## 🧠 What happens next (based on what we find)

### 🟢 If second drive shows up as “Available”
→ You just need to:
- Go to **Storage Pool**
- Click **Repair**
- Select that drive

---

### 🟡 If second drive shows “Not initialized”
→ Still good:
- Same process → **Repair → select drive**

---

### 🔴 If second drive does NOT show at all
→ Then:
- Hardware issue (connection or drive failure)

We’ll troubleshoot:
- Swap drive bays
- Check if the drive spins up
- Possibly test in another system

---

## ⚠️ Don’t click repair yet

Until we confirm:
- The second drive is the correct one  
- It doesn’t wipe anything  

---

## 👇 Next step

Send a screenshot of:
👉 **Storage Manager → HDD/SSD tab**

That will tell me instantly which path you’re on and exactly what button to press.

**You:** {"asset_pointer": "sediment://file_000000007bcc722fb5c43986ed32105d", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 394529, "width": 1152}

**ChatGPT:** Perfect — this screenshot tells us exactly what’s wrong.

---

## 🧠 What’s actually happening

- ✅ **Drive 1 → Healthy**
- ✅ **Drive 2 → Healthy**
- ❌ But your **storage pool only includes ONE of them**

👉 Translation:
> Your second drive exists, but it is **NOT part of the RAID anymore**

This usually happens when:
- The pool got “broken” during the move  
- Synology lost track of the second disk’s membership  
- Or it was temporarily disconnected and dropped from the array  

---

## ✅ Good news

- Both drives are **healthy**
- Your data is still there
- This is **100% fixable**

---

## ⚠️ Important before we fix it

We need to make sure:
👉 We **add the correct drive back into the pool**  
👉 Without wiping anything accidentally

---

## 🔧 Step-by-step fix (this is what you do)

### 1. Go to:
👉 **Storage Manager → Storage Pool**

---

### 2. Click:
👉 **Repair**

---

### 3. It will ask you to select a drive

You should see:
- The **other 3.6 TB drive available**

👉 Select the drive that is **NOT currently in the pool**

---

### 4. Confirm repair

- Synology will:
  - Add the drive back
  - Rebuild the RAID
- This can take **hours**

---

## ⏳ What happens during repair

- Your data stays accessible
- Performance may be slower
- You’ll see a **rebuilding progress bar**

---

## 🚨 One VERY important check

Before you click repair:

👉 Go to:
**Storage Manager → Storage Pool → Drive Info**

Confirm:
- Only ONE drive is currently assigned to the pool

---

## ❗ If you don’t see a drive available to select

Then the second drive might:
- Have leftover partitions
- Need to be “initialized”

👉 I can walk you through that safely if needed

---

## 🧠 What caused this (so it doesn’t happen again)

Most likely:
- Drive briefly disconnected during move
- SHR dropped it from array
- Didn’t auto-readd

Totally normal in home setups

---

## 👇 Next step

Go hit:
👉 **Repair → select second drive**

If you want to be 100% safe:
Send a pic of the **Repair screen before confirming**, and I’ll double-check it with you.

**You:** {"asset_pointer": "sediment://file_00000000d67871f58cad535881b5eb9d", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 464643, "width": 1152}

**ChatGPT:** Perfect — this is exactly what I wanted to see.

## ✅ You are good to proceed

- **Action:** Repair  
- **Selected drive:** Drive 1  
- **Pool:** Storage Pool 1  
- **Mode:** Fast Repair  

👉 This means Synology is about to **add Drive 1 back into the RAID and rebuild it**.

---

## 🚨 Important confirmation (last sanity check)

This is safe **because:**
- You already confirmed both drives are present
- One drive is currently “missing” from the pool
- Synology is **re-adding it**, not wiping your existing volume

👉 This is the correct operation.

---

## 🟢 Go ahead and click **Apply**

---

## ⏳ What happens next

- RAID will start **rebuilding**
- You’ll see:
  - Progress % in Storage Manager
- Time estimate:
  - Likely **several hours (4–12 depending on load)**

---

## ⚠️ During rebuild

- ✅ You can still use Plex / NAS
- ⚠️ It will be slower
- ❌ Do NOT:
  - Shut down the NAS
  - Remove drives

---

## 🧠 After it finishes

You should see:
- Storage Pool → **Healthy**
- Protection restored (SHR redundancy back)

---

## 💡 One smart move after this

Once it's done:
👉 Run **Data Scrubbing**

This helps catch silent issues after a rebuild

---

## 🔥 Real talk

You handled this well — a lot of people panic and wipe their pool here.  
You caught it early, and this is the *best-case recovery scenario*.

---

If anything looks weird during rebuild (errors, stalls, etc.), send a screenshot — I’ll stay with you through it.
