---
date: 2026-05-05
source: chatgpt
title: "Prusa Mini Setup Guide"
category: "Design & Creative"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_0000000090c471fd92287bb66d2e9e1f", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 537558, "width": 1152}
{"asset_pointer": "sediment://file_00000000a0f471fda9d72797a27df10c", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 405577, "width": 1152}
{"asset_pointer": "sediment://file_00000000d99071fdbfa165a1701f546a", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 598919, "width": 1152}
Used prusa mini. Plugged in and on. Give me my steps to get printing

**ChatGPT:** Nice—you’ve got a **Prusa Mini+** and it’s already assembled and powered on 👍 You’re like 10–15 minutes away from your first print if everything checks out.

I’ll walk you through the exact flow—no fluff.

---

# ✅ 1. Quick physical check (from your photos)
Before touching the screen:

- Filament tube (white PTFE) is connected ✔️  
- Print head wiring looks clean ✔️  
- Bed is installed ✔️  
- Nothing loose or dangling ✔️  

👉 Only thing: make sure the **print sheet is clean** (wipe with isopropyl alcohol if you have it)

---

# ⚡ 2. First-time setup on the screen
On the orange controller:

Go to:
```
Settings → Configuration / Wizard
```

Run:
### 👉 “Selftest”
This checks:
- Motors
- Fans
- Heater

Let it complete fully.

---

# 🎯 3. Calibration (CRITICAL)
This is the step people skip and then prints fail.

Run:

### 👉 “First Layer Calibration”

The printer will:
- Heat up
- Draw a line on the bed

Use the knob to adjust:

- If filament is NOT sticking → lower nozzle (more negative)
- If it’s squished too hard → raise it (less negative)

You want:
✔ Smooth line  
✔ Slightly squished  
✔ Not peeling up  

---

# 🧵 4. Load filament
Go to:
```
Filament → Load Filament
```

Steps:
1. Heat nozzle (it will auto do this)
2. Insert filament into top
3. Push until gears grab it
4. Wait until plastic comes out of nozzle clean

👉 If it curls or blobs at first = normal

---

# 📦 5. Get something to print (easiest way)

### Option A (FASTEST – do this first):
Your printer likely came with an SD card.

- Insert SD card
- Go to:
```
Print → select file
```

Pick something like:
- Benchy
- Prusa logo
- Sample print

---

### Option B (from your computer)
Use:
- **PrusaSlicer** (free)

Steps:
1. Import model (.STL)
2. Select printer: **Prusa Mini**
3. Slice
4. Export to SD card
5. Print

---

# 🔥 6. Start first print
When printing:

Watch first 2 minutes closely:
- Is filament sticking?
- Is it dragging or lifting?

If bad:
👉 Stop print → redo first layer calibration

---

# ⚠️ Common beginner mistakes (avoid these)
- Not calibrating first layer ❌
- Dirty print bed ❌
- Wrong filament type (start with PLA) ❌
- Walking away too early ❌

---

# 🚀 7. After first successful print
Then you can:
- Tune quality
- Try different models
- Adjust temps
- Add OctoPrint later (fits your homelab setup nicely)

---

# 🧠 Pro tip (based on your setup)
Since you’re into homelab/Plex:

Later you can:
- Run **OctoPrint in Docker** on your NUC
- Control printer over network
- Upload prints remotely

---

# If you want next:
I can:
- Walk you through your **first calibration LIVE step-by-step**
- Help diagnose if first layer looks bad (send pic)
- Set up **remote printing with your server**

Just tell me where you're at 👍

**You:** There’s a small one of fillament in there

**ChatGPT:** Yep—that’s totally normal 👍  
What you’re seeing is just **leftover filament in the hotend from the previous owner**.

Here’s what to do (takes 2–3 minutes):

---

# 🔥 1. Heat the nozzle
On your screen:
```text
Filament → Load Filament
```

Let it heat up (usually ~215°C for PLA).

---

# 🧵 2. Push new filament in
- Insert your filament into the top
- Push it in firmly until the gears grab it

The printer will start feeding it through.

---

# 🟡 3. Watch what comes out
At first you’ll see:
- Old color (from previous filament)
- Maybe a weird mix

👉 **Keep it going until the color is 100% your new filament**

---

# ✂️ 4. Clean the nozzle tip
Once it’s flowing clean:
- Use tweezers or fingers (careful, hot)  
- Pull off the little blob hanging

---

# ⚠️ If filament won’t go in:
Try this:
- Increase temp slightly (220°C)
- Push a bit harder while loading

---

# 🚫 Don’t worry about:
- Small leftover filament inside → completely fine  
- Mixing colors at first → expected  

---

# ✅ When you’re ready:
After clean extrusion:
👉 Go run **First Layer Calibration** before printing

---

If you want, send me a pic of what’s coming out of the nozzle and I’ll tell you if it looks perfect or not.

**You:** I don’t see self test

**ChatGPT:** Yeah that menu can be a little hidden on the **Prusa Mini**—you’re not crazy.

From your screen in the pic, you’re on the main menu. Do this exactly:

---

# 🔍 How to find Selftest

On the knob:

### 1. Click the knob → go to:
```text
Settings
```

### 2. Scroll down to:
```text
Calibration
```

### 3. Inside there you should see:
```text
Selftest
```

---

# 🤔 If you STILL don’t see it
There are 2 common reasons:

### 1. Firmware layout difference
Some versions show it as:
```text
Settings → Selftest
```

### 2. It may already be completed
If previous owner ran it, it might not show prominently.

👉 In that case, **you can safely skip selftest** and go straight to:

```text
Calibration → First Layer Calibration
```

---

# 🎯 What matters more than selftest
Honestly, the **first layer calibration is the important one**.

Do this next:
```text
Calibration → First Layer Calibration
```

That’s what determines whether your prints succeed.

---

# Quick sanity check (before printing)
Since you bought it used:

- Does the nozzle heat? ✔️  
- Do fans spin? ✔️  
- Does the head move when you press “Home”? ✔️  

If yes → you’re good to go.

---

# If you want to be safe
We can still verify everything manually in 30 seconds.

Tell me:
👉 Does it move when you hit **Auto Home**?

If yes, I’ll guide you straight into your first print.

**You:** No calibration

**ChatGPT:** Alright—if you’re not seeing **Selftest OR Calibration**, something’s off. The Mini always has those unless the UI is limited or firmware is weird.

But don’t get stuck—we can **still get you printing right now** and fix menus after.

---

# 🔧 First—confirm basic control works
On your screen, do you see something like:

- **Move Axis**
- **Preheat**
- **Filament**
- **Settings**

👉 If yes, good—we’ll do manual setup.

---

# 🔥 1. Manually heat the nozzle
Go to:
```text
Preheat → PLA
```

Wait until ~200–215°C.

---

# 🧵 2. Manually load filament
Go to:
```text
Filament → Load
```

Push filament in until:
- It grabs
- Plastic comes out clean

---

# 🏠 3. Home the printer
Go to:
```text
Move Axis → Auto Home
```

Make sure:
- Bed moves forward/back
- Head moves left/right
- Z goes up/down

If that all works → machine is healthy.

---

# 🎯 4. Do a “manual first layer” (since menu missing)
We’ll simulate calibration:

Start ANY print (from SD card if you have one)

### While it starts printing:
Watch the first line:

👉 Adjust live:
```text
Settings → Live Adjust Z
```
(or sometimes just “Tune” during print)

---

### What you want:
- Line sticks to bed ✅  
- Slightly squished ✅  

### Adjust like this:
- Not sticking → turn knob **more negative**  
- Too squished → turn knob **less negative**

---

# 🚨 Why your menu is missing
One of these is happening:

1. **Old firmware**
2. **Factory reset / partial config**
3. **UI mode glitch**

---

# 🧠 Fix (do this AFTER first print works)

Update firmware:

1. Go to:  
👉 https://www.prusa3d.com/drivers/

2. Download:
👉 **Prusa Mini firmware**

3. Put file on USB
4. Plug into printer
5. It will prompt update

---

# 🟢 Reality check
You’re NOT stuck.

Even without those menus:
👉 If it heats + moves + extrudes → you can print

---

# Next step
Tell me what you see on your main screen exactly (list the options)

or send a pic of the menu

I’ll pinpoint exactly what’s missing and fix it clean 👍

**You:** {"asset_pointer": "sediment://file_0000000055c471fd80e6f42ba70697d4", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 414799, "width": 1152}

**ChatGPT:** Perfect — that IS the first layer calibration test 👍

And honestly?  
That top-left square already looks pretty decent.

Here’s what I see:

- Filament is sticking well ✅
- Lines are connected ✅
- Not wildly squished ✅
- Maybe *slightly* high still, but very close

---

# What to do NOW

While it’s still printing:

Adjust the Z offset a tiny bit more negative.

Something like:
```text id="n9tq90"
-0.020 to -0.050
```

more negative than current.

You want the lines in that square to:
- Blend together slightly
- Have almost no visible gaps

---

# What “too high” looks like
Your long lines show a tiny bit of:
- Rounded filament
- Slight spacing

That means nozzle is just a hair high.

---

# IMPORTANT
Do NOT overdo it.

If you go too low:
- Surface gets rough
- Nozzle scrapes
- Elephant foot / blobs

---

# Ideal first layer
You want:
- Smooth satin look
- Slight squish
- No gaps
- No ridges

---

# After this finishes
If the square:
- Feels smooth with fingernail
- Doesn’t peel easily

👉 You’re ready to print real models.

---

# Next step after calibration
Go to:
```text id="b0g1oi"
Print → sample model
```

Print:
- Benchy
- Prusa logo
- Anything small

---

# One more thing
Your sheet looks pretty clean, but before serious printing:

Use:
- 90%+ isopropyl alcohol

Avoid touching the print area with fingers afterward.

---

You’re actually in good shape here for a used printer.

**You:** How to take print off

**ChatGPT:** # ✅ Best way to remove prints on the Prusa Mini

The nice thing about the Prusa spring steel sheet:
👉 You usually do NOT pry prints off.

---

# Method 1 (best): Let it cool
Wait until:
- Bed temp drops near room temp

Most PLA prints will:
- Pop loose themselves
OR
- Come off very easily

---

# Method 2: Flex the sheet (recommended)

1. Lift the steel sheet off the magnetic bed
2. Slightly bend/flex it

The print should:
👉 Pop right off

This is the normal Prusa method.

---

# ⚠️ Avoid this
Don’t:
- Dig aggressively with metal scraper
- Pry hard at corners
- Gouge the sheet

You can damage the PEI surface.

---

# For the calibration lines in your pic
Those thin lines may stick a little more.

You can:
- Flex sheet
- Rub with fingernail/plastic scraper
- Peel gently from one corner

---

# If something is REALLY stuck
Put sheet back on printer and:
```text id="qsgsl8"
Preheat bed to ~60°C
```

Then try removing again.

---

# After removing
Wipe bed with:
- Isopropyl alcohol

This keeps adhesion consistent.

---

# Bonus tip
If prints EVER stop sticking well:
Wash the sheet with:
- Warm water
- Tiny bit of dish soap

Dry fully, then alcohol wipe.

That restores adhesion surprisingly well.

**You:** {"asset_pointer": "sediment://file_00000000a2b071fd92b92373eced4471", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 431700, "width": 1152}
What happened

**ChatGPT:** That’s classic **“spaghetti” failure** 🍝 — totally normal for a first used-printer test.

What happened:
- The print lost adhesion or detached from the bed
- Then the printer kept printing in midair
- Filament piled into a noodle mess

Good news:
👉 Your printer is probably fine.

---

# Most likely causes

## 1. Bed wasn’t clean enough
Finger oils = prints stop sticking.

Do this:
- Remove sheet
- Wash with dish soap + warm water
- Dry fully
- Then wipe with isopropyl alcohol

---

## 2. Z height slightly too high
Your calibration earlier was close, but maybe still a tiny bit high.

The first layer needs a bit more squish.

---

## 3. Old/cheap filament
If that filament came with the printer:
👉 It may be old and brittle/moisture-soaked.

That causes weak prints and poor adhesion.

---

# What to do RIGHT NOW

## Step 1 — Stop print
Press:
```text id="i2dsh3"
Stop
```

---

## Step 2 — Clean nozzle blob
Careful — nozzle is HOT.

Pull off:
- Loose spaghetti
- Any blob hanging on nozzle

Tweezers help.

---

## Step 3 — Clean print bed
Wash it properly.

This matters WAY more than beginners think.

---

## Step 4 — Run first layer test AGAIN
This time:
- Lower Z slightly more
- Maybe another `-0.030`

You want:
- More squish
- Smooth connected lines

---

# BEFORE next real print
Print something tiny/simple:

Best first prints:
- 20mm calibration cube
- Benchy
- Small Prusa logo

Avoid tall weird models at first.

---

# Also important
That object in the photo almost looks like:
- Failed old filament
OR
- Someone intentionally started a junk print

So don’t assume the printer itself caused it.

---

# Honestly?
For a used Mini:
- Motion looks good
- Extrusion works
- Bed heating works

You’re actually starting from a pretty solid place.

**You:** It was not a junk print but filament is older

**ChatGPT:** Yeah, old filament alone can absolutely cause this.

PLA that’s been sitting:
- Absorbs moisture from air
- Gets brittle
- Prints inconsistently
- Strings like crazy
- Loses bed adhesion easier

And your failed print actually looks VERY consistent with old wet PLA.

---

# Signs your filament is old/wet
You may notice:
- Lots of stringing
- Brittle snapping
- Rough surface
- Popping/crackling sounds
- Weak layer adhesion
- Random blobs

---

# Easiest test
When cold:
- Bend the filament slightly

If it:
- Snaps easily = old/wet
- Feels flexible = probably okay

---

# What I’d do in your position

## Best option
Get a fresh spool of:
entity["product","Polymaker PolyLite PLA"]  
or  
entity["product","Overture PLA"]

Those are beginner-friendly and reliable.

---

# For NOW though
You can probably still print with this filament.

Just:
- Clean bed well
- Lower Z slightly
- Print smaller/simple objects
- Slow first layer down

---

# Important thing:
Your printer itself actually looks healthy.

The fact that it:
- Extruded consistently
- Moved correctly
- Heated properly

…means you likely avoided the expensive problems already.

---

# One thing to check next
Look at the nozzle.

If there’s burnt plastic buildup around it:
- Heat nozzle
- Carefully wipe with paper towel/tweezers

A dirty nozzle plus old PLA can worsen adhesion and stringing.

---

# Your next print attempt
I’d recommend:
- Small calibration cube
- Freshly cleaned bed
- Slightly lower Z offset
- Watch first layer carefully

You’re very close to having this dialed in.

**You:** Step by step before next print

**ChatGPT:** Do this exactly before the next print:

## 1. Stop/cool
Stop the print. Let the bed/nozzle cool enough to touch safely.

## 2. Remove the mess
Take off the flexible steel sheet. Flex it to pop off the failed print. Remove any loose strings from the nozzle area.

## 3. Clean the nozzle
Heat nozzle to PLA temp:

```text
Preheat → PLA
```

When hot, carefully pull off any plastic stuck to the nozzle with tweezers. Don’t touch the brass nozzle with fingers.

## 4. Clean the bed properly
Remove the steel sheet and wash it at the sink:

```text
Warm water + dish soap
```

Scrub with clean fingers or a clean sponge. Dry fully with paper towel. Try not to touch the print surface after.

## 5. Put sheet back on
Put the steel sheet back on the magnetic bed. Make sure it is seated flat and aligned.

## 6. Load/purge filament
Go to:

```text
Filament → Load Filament
```

Let it push filament through until the color/flow looks clean and steady. Trim the blob/string off the nozzle.

## 7. Run first layer calibration again
Start the first layer calibration.

While it prints, lower Z a little more than before:

```text
More negative = nozzle closer
```

Go in small steps:

```text
-0.020 at a time
```

Stop when the line is slightly squished, smooth, and stuck down. No round loose string.

## 8. Print something small
Do not try a big/tall print yet.

Pick one:
```text
Prusa logo
20mm cube
Benchy
```

## 9. Watch the first 5 minutes
Do not walk away. If the first layer lifts, curls, or turns into strings, stop immediately.

For old filament, set first print slower if you can:

```text
PLA
Nozzle: 210–215°C
Bed: 60°C
```

Your failure was most likely old filament + first layer/bed adhesion, not a broken printer.

**You:** {"asset_pointer": "sediment://file_000000001d7871fd9854f12cb99744d5", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 338133, "width": 1152}
{"asset_pointer": "sediment://file_00000000dac471fd9640c59fa04f5d37", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 456234, "width": 1152}

**ChatGPT:** This is MUCH better. You’re basically there now 👍

What I see:

- Lines are sticking consistently ✅
- No lifting/curling ✅
- Square is clean and uniform ✅
- Long paths are stable ✅

The nozzle is maybe still:
```text id="u57ml0"
slightly high
```

…but only by a tiny amount.

---

# Final tiny adjustment
Lower Z just a little more:

```text id="mr1ccz"
~ -0.010 to -0.020
```

more negative.

You want the individual lines in the square to blend together just a touch more.

Right now they’re:
- Good
- But still slightly distinct

---

# Then STOP calibrating
Seriously — don’t chase perfection forever.

You are now:
```text id="7zkf8v"
well within usable range
```

for normal PLA printing.

---

# Next step: real print

Print something simple:
- Benchy
- 20mm cube
- Prusa logo

Watch:
- First layer only
- First 3–5 minutes

If it sticks through that:
👉 you’re good.

---

# One important note
That steel sheet has visible wear/scratches, which is completely normal for used Prusas.

But because of that:
- Cleanliness matters more
- Avoid touching center area

---

# My honest assessment of the printer
From all your pics:
- Motion system looks healthy
- Bed adhesion now looks good
- Extrusion looks consistent
- No obvious clog
- No obvious warped bed

This actually looks like a pretty solid used Mini.

**You:** I’m at 0.000 now

**ChatGPT:** Ah — then your Z offset logic is inverted from what we were discussing earlier.

If you’re at:

```text id="4kof93"
0.000
```

and the print still looks just slightly high, then you actually want to go:

```text id="im9w4h"
positive
```

a tiny amount on this setup.

Try:

```text id="y9st7r"
+0.010 to +0.020
```

ONLY if:
- lines still look a little round/separate
- square doesn’t fully blend together

---

But honestly?

Your latest calibration already looks good enough to print real objects.

At this point:
👉 Stop tuning
👉 Start printing

Because over-tweaking is how beginners end up making it worse.

---

# What to print next
Do one of these:
- Benchy
- 20mm cube
- Prusa logo

And watch:
- first layer
- first few minutes

If it stays attached:
✅ calibration is good enough

---

# Important expectation
With:
- older filament
- used sheet
- used nozzle

…you are NOT going to get perfect Instagram-quality first layers immediately.

But you are already in:
```text id="1x8jrp"
functional / good
```

territory now.

**You:** Well is was .01 before and I made it 0

**ChatGPT:** Got it — then you moved the nozzle slightly farther away from the bed when you changed:

```text id="um5dbq"
0.01 → 0.00
```

So your earlier setting was probably actually better.

Based on your photos, I’d go back to around:

```text id="8oyx4t"
+0.010
```

or maybe:

```text id="m2kj1q"
+0.015
```

That should give just a little more squish.

---

# Then stop adjusting
Seriously, you’re already extremely close.

Your latest calibration is:
- Good enough for normal prints
- Not showing major adhesion issues
- Not scraping

---

# Next move
Print:
```text id="gtu6fy"
20mm calibration cube
```

or:
```text id="jgx7za"
Benchy
```

Watch the first layer.

If it:
- stays flat
- doesn’t peel
- doesn’t spaghetti

👉 you’re dialed in enough to start using the printer normally.

---

# One more thing
Since the filament is older:
- some stringing is expected
- slightly uglier prints are expected

Don’t spend hours chasing tiny imperfections with this spool.

**You:** {"asset_pointer": "sediment://file_00000000d5b471fdb1f5fe1f40686ea5", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 357321, "width": 1152}
.05

**ChatGPT:** Yep — that looks better than before. The square is getting more properly squished now 👍

At:

```text id="svj8ae"
0.05
```

you’re in a good range.

The lines in the square are:
- Connecting better ✅
- Smoother ✅
- Still not over-squished ✅

You could maybe go:
```text id="7q1f5y"
0.055–0.060
```

for absolute perfection, but honestly:

👉 I would stop here and print something real.

---

# What to do next

Print:
```text id="twn1t9"
20mm cube
```

or:
```text id="n0v0qb"
Benchy
```

Watch:
- first layer only
- first few minutes

If it stays attached:
✅ you’re calibrated enough

---

# One thing I DO notice
That little defect/blob in the square is probably:
- old filament inconsistency
OR
- tiny nozzle contamination

Not a calibration disaster.

---

# Before every print now
Do this habitually:

```text id="8quv9f"
Alcohol wipe on bed
```

That alone prevents a huge amount of failures.

---

# Your printer status right now
Honestly:
```text id="byu4jv"
Ready for normal PLA printing
```

You’ve already solved the hard beginner part.

**You:** There’s a big hole in the middle of the square

**ChatGPT:** Yep, I see it now — but the good news is:

That is NOT a bad Z-height problem.

That single hole is much more likely:
- old/wet filament
- tiny nozzle contamination
- inconsistent extrusion for a moment

Because the REST of the square looks good.

If Z was wrong, you’d see:
- gaps everywhere
- poor adhesion everywhere
- uneven lines across whole square

Instead, yours is:
```text id="aeh2dr"
mostly uniform with one defect
```

which points to extrusion inconsistency, not calibration.

---

# What I would do

## Option 1 (recommended)
Leave Z where it is:
```text id="3s6r71"
0.05
```

and print a small real object.

You’re close enough now.

---

## Option 2 (if you want cleaner results)
Do a quick nozzle purge:

### Heat nozzle:
```text id="kg1v5t"
Preheat PLA
```

### Then extrude more filament:
```text id="95n16r"
Filament → Load
```

Push through:
- 20–30 cm of filament

Sometimes old material clears out and fixes random gaps instantly.

---

# Also:
That filament may simply be inconsistent.

Old PLA commonly causes:
- random missing spots
- weak extrusion
- blobs
- stringing

---

# Important beginner advice
Don’t spend 2 hours trying to make the calibration square flawless using questionable old filament.

Your printer is already:
```text id="8kqpmg"
good enough to start printing
```

Fresh filament later will probably make a massive difference immediately.

**You:** How to clean nozzle

**ChatGPT:** # Easy/safe way to clean the nozzle on your Prusa Mini

You do NOT need to disassemble anything right now.

---

# ✅ Method 1 — Basic hot wipe (do this first)

## 1. Heat nozzle
On printer:

```text id="7z3o88"
Preheat → PLA
```

Wait until nozzle is around:
```text id="6vg2zc"
210–220°C
```

---

## 2. Remove dangling plastic
Use:
- tweezers
- paper towel folded thick
- brass brush if you have one

Carefully wipe:
- bottom of nozzle
- sides of nozzle

⚠️ VERY HOT.

Do not touch heater wires.

---

## 3. Extrude fresh filament
Go to:

```text id="p4l8r1"
Filament → Load Filament
```

Let filament flow through for:
```text id="yqjlwm"
20–30 seconds
```

You want:
- smooth consistent strand
- no popping
- no burnt chunks

---

# ✅ Method 2 — “Cold pull” (ONLY if clogging continues)
Do this later if:
- missing lines
- clicking extruder
- inconsistent extrusion

Not necessary yet probably.

---

# What NOT to do
Avoid:
- steel wire into nozzle
- random needles
- scraping hard with metal tools

You can damage nozzle.

---

# What your nozzle probably has
Based on your pics:
```text id="p4ll31"
minor residue / old filament contamination
```

Not a severe clog.

---

# After cleaning
Run:
- one more purge
- then print a small cube/benchy

If missing spots disappear:
✅ issue solved

---

# Strong recommendation
Get fresh PLA soon.

Even a cheap new spool will make troubleshooting WAY easier because you remove the “is the filament bad?” variable.

**You:** {"asset_pointer": "sediment://file_00000000da9871fdbe1a25cc4a243c9c", "content_type": "image_asset_pointer", "fovea": null, "height": 1152, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 319910, "width": 1536}

**ChatGPT:** That actually looks like OpenClaw is working now with:

```text id="i8j40h"
ollama/qwen2.5:7b
```

The important line is:

```text id="mclscz"
local ready | idle
```

and it responded to “hello,” which means:
- Ollama is connected ✅
- Qwen is loaded ✅
- OpenClaw session is running ✅

---

# About this error:
```text id="zj39l5"
[assistant turn failed before producing content]
```

That usually happens:
- during startup
- when model initializes
- first prompt timeout
- context setup hiccup

If it responds afterward (which yours did):
👉 ignore it for now.

---

# What to test next

Try these:

```text id="rf4cs1"
what model are you using
```

```text id="xhffvw"
write a short python script
```

```text id="v73kbq"
summarize what OpenClaw is
```

If responses are:
- reasonably fast
- consistent
- no crashes

then your setup is healthy.

---

# Your performance expectations
On your Lenovo P3 without a strong GPU:

```text id="zkqvb0"
Qwen2.5 7B
```

is a MUCH better fit than:
- Llama 3.1 8B
- larger models

That’s why it feels way snappier.

---

# Next improvement (important)
Right now you’re running:
```text id="qys98h"
terminal UI only
```

The next nice upgrade is:

## Open WebUI
Browser-based interface:
- chat history
- model switching
- cleaner UX
- easier management

Since Ollama already works, Open WebUI setup should be straightforward now.

---

# One thing I’d still recommend
Update OpenClaw config so Qwen is the default model permanently instead of Llama.

Because right now it looks like you manually changed the session model.

**You:** {"asset_pointer": "sediment://file_0000000020f471fd9aacda85eaecd711", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 246733, "width": 709}

**ChatGPT:** Nice — this means your Telegram bot is working correctly.  
You just need to approve your Telegram account from the OpenClaw terminal.

On the machine running OpenClaw, type exactly:

```bash
openclaw pairing approve telegram 3YD3LYKE
```

Then press Enter.

After that:
1. Go back to Telegram
2. Send:
```text id="0zwdfh"
/start
```

again or just say:
```text id="1jqmyq"
hello
```

and the bot should respond normally.

---

# What’s happening here
OpenClaw uses pairing approval so random Telegram users can’t access your local AI agent.

Your screenshot shows:
- Telegram bot configured correctly ✅
- Pairing code generated correctly ✅
- OpenClaw running correctly ✅

So this is actually a good sign.

---

# After pairing works
You’ll be able to:
- Chat with your local Qwen model from phone
- Access your homelab AI remotely
- Keep sessions between desktop + mobile

Pretty cool setup honestly.

**You:** {"asset_pointer": "sediment://file_0000000091a871f899e596c5955f0aca", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 3152399, "width": 1152}
{"asset_pointer": "sediment://file_000000008f3871fd8078deeac66aeece", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 3365947, "width": 1152}

**ChatGPT:** That’s actually a pretty solid Benchy for:
- old mystery filament
- a used printer
- first setup/calibration

You’re in good shape.

What I notice:

## Good
- Hull shape looks clean ✅
- Layers are mostly consistent ✅
- No catastrophic shifting ✅
- Adhesion held ✅
- Overhangs mostly worked ✅

## Minor issues
- Some stringing/blobs
- Slight roughness
- Small imperfections

That is VERY likely from:
```text id="14hnw4"
old PLA filament
```

more than the printer itself.

---

# Translation:
Your printer works.

Seriously.

You’ve already cleared:
- calibration
- adhesion
- extrusion
- motion
- basic tuning

Those are the hard beginner hurdles.

---

# Biggest upgrade now
Fresh PLA.

Get something like:
entity["product","Polymaker PolyLite PLA"]  
or  
entity["product","Overture PLA"]

You’ll probably see an immediate quality jump.

---

# Next things to learn
Now you can start exploring:

## Printables
urlPrintableshttps://www.printables.com

Great for Prusa users.

---

## Useful first homelab prints
Since you’re into self-hosting/networking:

- Raspberry Pi mounts
- Cable clips
- Rack accessories
- NUC mounts
- Headphone stands
- Gridfinity organizers

---

# Strong recommendation
Before changing a million settings:
```text id="fskc78"
print more with default settings first
```

Learn:
- how supports work
- how orientation matters
- what failures look like

THEN tune.

---

# Honestly?
That’s a successful first printer setup session.
