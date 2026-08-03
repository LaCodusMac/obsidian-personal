---
date: 2026-02-23
source: chatgpt
title: "UniFi Cloud Key Restore"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Upload the .unifi-file you want to use to restore to your UCK G2 Plus. When i try this my .unf files do not show up or let me add

**ChatGPT:** Alright Jake — this is almost always one of these 4 issues when restoring a **UniFi backup** to a **Cloud Key Gen2 Plus**.

We’ll go step-by-step.

---

## 1️⃣ First — Make Sure It’s the Right File Type

The **entity["product","UniFi Cloud Key Gen2 Plus","ubiquiti device"]** only accepts:

```
.unifi
```

NOT:

```
.unf
```

If your backup ends in **.unf**, that’s from:
- Older UniFi Controller versions
- Or a local export from Windows

The Cloud Key restore page will literally not show `.unf` files.

---

## 2️⃣ If You Only Have .unf Files

You have two options:

### ✅ Option A (Cleanest Way)
Temporarily install UniFi Network on your laptop:

- Install **entity["software","UniFi Network Application","ubiquiti controller software"]**
- Restore the `.unf` file there
- Then create a NEW backup from that controller
- That new backup will be `.unifi`
- Upload that to your Cloud Key

This works 100% of the time.

---

### ✅ Option B (Sometimes Works)
Rename:

```
backup.unf
```

to

```
backup.unifi
```

⚠️ This only works if it was made from a newer controller version.  
If it fails — use Option A.

---

## 3️⃣ Also Check These (Very Common)

### 🔹 Same or Newer Version Required

The Cloud Key firmware must be:
- Same version
- Or NEWER than the backup version

If your Cloud Key is on a very old version, update it first.

Check under:
```
Settings → System → Updates
```

---

### 🔹 Browser Issue

Sometimes the file picker won’t show files if:

- File filter is set to specific type
- You're using Edge weirdly
- It’s inside a zip

Make sure:
- File is NOT zipped
- Try Chrome
- Drag and drop instead of browse

---

## 4️⃣ Where Exactly Are You Restoring?

There are two restore spots:

### 🔹 During initial setup (best way)
or  
### 🔹 Settings → System → Backup → Restore

If you're restoring from the old Windows controller, the initial setup screen is safer.

---

## 5️⃣ Important Question

Where did this `.unf` file come from?

- From your Windows laptop?
- From another Cloud Key?
- From a UniFi OS console?

That determines the cleanest fix.

---

Reply with:
- The file extension you have
- What version your Cloud Key is running
- Where the backup was created

We’ll get this restored properly. 💪

**You:** how to get .unifi file

**ChatGPT:** Alright Jake — here’s exactly how you get a **`.unifi` backup file** (the only type your **entity["product","UniFi Cloud Key Gen2 Plus","ubiquiti device"]** accepts for restore).

---

# ✅ How To Create a `.unifi` Backup File

You must create it from a **UniFi OS console** (Cloud Key, Dream Machine, etc.).

You CANNOT generate `.unifi` directly from old Windows-only `.unf` exports.

---

## 🔹 If You Still Have Your Old Controller Running (Best Case)

If your controller is still running on:

- Your Windows laptop  
- Another Cloud Key  
- A UniFi OS device  

Do this:

### Step 1  
Open your controller.

### Step 2  
Go to:

```
Settings → System → Backup
```

### Step 3  
Click:

```
Download Backup
```

⚠️ If it's a UniFi OS console, it will download as:

```
backup.unifi  ✅
```

If it downloads as `.unf`, you are on a legacy controller and need the conversion method below.

---

# 🔄 If You ONLY Have a `.unf` File

No problem. Here’s how to convert it properly.

---

## 🛠 Method: Convert `.unf` → `.unifi`

### Step 1 – Install UniFi Network on Your Laptop

Install:

**entity["software","UniFi Network Application","ubiquiti controller software"]**

(Just run it locally.)

---

### Step 2 – Restore the `.unf` File

Inside UniFi Network:

```
Settings → System → Restore
```

Upload your `.unf`.

---

### Step 3 – Generate a NEW Backup

After restore finishes:

Go back to:

```
Settings → System → Backup
```

Click:

```
Download Backup
```

Now it will download as:

```
backup.unifi  ✅
```

That’s the file you upload to your Cloud Key.

---

# 🔥 Why This Is Required

`.unf` = Legacy standalone controller format  
`.unifi` = UniFi OS console format  

Cloud Key Gen2 Plus runs UniFi OS — so it only accepts `.unifi`.

---

# 🧠 Pro Tip (Version Match Matters)

Your Cloud Key firmware must be:

- Same version
- Or NEWER than the backup version

If restore fails, update your Cloud Key first.

---

If you want, tell me:
- What version your backup came from
- What version your Cloud Key is on

And I’ll make sure you don’t hit a version mismatch error next.
