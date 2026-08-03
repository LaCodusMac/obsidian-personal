---
date: 2026-06-01
source: chatgpt
title: "Smart Lock Options"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** {"asset_pointer": "sediment://file_00000000bb6071f58df59bac28f59863", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 230539, "width": 709}
Smart locks like this that physically turn the lock

**ChatGPT:** Yes — the lock in your screenshot is a **retrofit smart lock**. Instead of replacing the deadbolt, it mounts on the inside of the door and **physically turns the existing thumb-turn**.

Here are the main options:

### urlSwitchBot Lock Prohttps://www.switch-bot.com/products/switchbot-lock-pro
image_group{"query":["SwitchBot Lock Pro installed on deadbolt","SwitchBot Lock Pro side view","SwitchBot Lock Pro keypad","SwitchBot Lock Pro thumbturn"]}

**Pros**
- Works with most existing deadbolts
- No drilling in most cases
- Physical key still works
- Good for apartments/rentals
- Integrates with Home Assistant
- Matter support (with Hub)

**Cons**
- Bulky on the inside
- Requires Hub Mini or Hub 2 for remote access

For your apartment situation, this is probably the best fit.

---

### urlAugust Wi-Fi Smart Lockhttps://august.com/products/august-wifi-smart-lock
image_group{"query":["August Wi-Fi Smart Lock installed","August Smart Lock interior deadbolt","August smart lock black","August lock existing deadbolt"]}

**Pros**
- Reputable brand
- Keeps existing lock and keys
- Built-in Wi-Fi

**Cons**
- Battery life shorter than SwitchBot
- More expensive

---

### urlYale Approach Lock with Wi-Fi Keypadhttps://www.yalehome.com/us/en/products/smart-locks/yale-approach-lock
image_group{"query":["Yale Approach Lock interior","Yale Approach retrofit smart lock","Yale smart lock existing deadbolt","Yale Approach keypad"]}

**Pros**
- Similar retrofit design
- Good app
- Existing key still works

**Cons**
- Newer product with less long-term track record

---

### For Home Assistant
Since you're already running Home Assistant on your homelab:

- **SwitchBot Lock Pro + Hub 2** is the easiest.
- Home Assistant has native SwitchBot integration.
- You can automate:
  - Unlock when arriving home
  - Lock at bedtime
  - Lock if door left unlocked for 15 minutes
  - Notifications if partner leaves

### Do you need a Hub?
**If you're only using Bluetooth from your phone nearby:** No.

**If you want any of these:** Yes.
- Remote control away from home
- Matter/HomeKit integration
- Alexa/Siri/Google
- Home Assistant integration over the network

Then get:
- **SwitchBot Lock Pro**
- **SwitchBot Hub 2**

That's the combination I'd choose for your apartment and Home Assistant setup.

**You:** I don’t want to have to take anything off the inside door

**ChatGPT:** If by "take anything off the inside door" you mean **you don't want to remove your existing deadbolt thumb-turn at all**, then your options get much more limited.

Most retrofit smart locks—including:
- SwitchBot Lock Pro
- August Wi-Fi Smart Lock
- Yale Approach

all require access to the inside thumb-turn. They either:
- replace the inside thumb-turn assembly, or
- clamp over it and use it to turn the lock.

The good news is that with the **SwitchBot Lock Pro**, you usually **don't permanently remove the lock from the door**. The installation is typically:
1. Remove the thumb-turn adapter (usually a couple screws).
2. Mount the SwitchBot bracket.
3. Reattach/use the existing lock mechanism.

When you move out, you can generally restore everything in 5–10 minutes.

If you literally want:
- No disassembly
- No screws removed
- No modification to the lock whatsoever

then you're looking at a different category of device:

### Robot lock turners
image_group{"query":["SwitchBot Bot turning deadbolt","robot finger smart lock deadbolt","SwitchBot Bot lock turner","smart button pusher deadbolt"]}

A urlSwitchBot Bothttps://www.switch-bot.com/products/switchbot-bot can sometimes push or pull a latch or lock lever, but most deadbolts require too much torque for it to be reliable.

### Another possibility
Can you post a picture of the **inside** of your apartment deadbolt?

The exact shape matters:
- Standard thumb-turn deadbolt
- Mortise lock
- Schlage-style
- Kwikset-style
- Apartment interconnect lock

I can tell you whether a SwitchBot Lock Pro can mount without permanently changing anything, or if there's a better option for your specific lock.

**You:** clamp over it and use it to turn the lock

**ChatGPT:** Yes, exactly.

The **SwitchBot Lock Pro** is one of the few options that can **clamp over your existing thumb-turn** rather than replacing the entire lock. That's why it's so popular with renters.

For most standard deadbolts:

1. Leave the outside key cylinder untouched.
2. Leave the actual deadbolt installed.
3. Attach an adapter to the existing thumb-turn.
4. Stick or screw the Lock Pro to the inside door.
5. The motor physically rotates your existing thumb-turn.

When you move out, you remove the Lock Pro and the door looks essentially the same as before.

For your apartment requirements:
- ✅ No exterior changes
- ✅ Physical key still works
- ✅ Works with Home Assistant
- ✅ Can be removed when you leave
- ✅ Doesn't require replacing the deadbolt

The only thing I'd verify is whether your apartment uses a **standard deadbolt** or a weird apartment-style mortise lock. If it's a normal deadbolt, the Lock Pro is usually the safest renter-friendly choice.

If you send a photo of the **inside of your actual deadbolt**, I can tell you with pretty high confidence whether the SwitchBot Lock Pro will fit before you spend the money.

**You:** List of options

**You:** Options with built in matter or zigbee support

**ChatGPT:** For your setup (Home Assistant, renter-friendly, wants a lock that **physically turns the existing deadbolt**), the biggest thing is whether you want **native Matter/Thread** or are okay with a hub.

### Best retrofit locks with Matter support

products{"selections":[["turn0product31","Aqara U200 Matter Retrofit Lock"],["turn0product9","SwitchBot Lock Pro"],["turn0product4","Level Bolt Matter Retrofit"],["turn0product2","Nuki Smart Lock Pro Matter"]]}

| Feature | entity["turn0product31","Aqara U200 Matter Retrofit Lock"] | entity["turn0product9","SwitchBot Lock Pro"] | entity["turn0product4","Level Bolt Matter Retrofit"] | entity["turn0product2","Nuki Smart Lock Pro Matter"] |
|---|---|---|---|---|
| Retrofit over existing deadbolt | Yes | Yes | Internal bolt replacement | Yes |
| Native Matter | Yes | No (hub required) | Yes | Yes |
| Thread | Yes | No | Yes | Yes |
| Home Assistant friendly | Excellent | Excellent | Good | Good |
| Renter friendly | Excellent | Excellent | Medium | Excellent |
| Keeps existing outside key | Yes | Yes | Yes | Yes |
| North America availability | Growing | Excellent | Excellent | Limited |

### My picks

#### Best overall for your setup
product["turn0product31","Aqara U200 Matter Retrofit Lock",{"render_as":"block","description":"Native Matter-over-Thread retrofit lock with strong Home Assistant and Apple Home support."}]

The Aqara U200 is basically what many Home Assistant users wanted:
- Native Matter-over-Thread
- Retrofit design
- Existing key still works
- No cloud dependency required
- Works well with Apple Home and Home Assistant citeturn0product31turn0product15

---

#### Best proven renter option
product["turn0product9","SwitchBot Lock Pro",{"render_as":"block","description":"Easy retrofit lock that physically turns your existing deadbolt and is extremely apartment friendly."}]

This is still probably the safest purchase if you're in an apartment and want minimal hassle.
The catch:
- Matter requires Hub 2 or Hub Mini Matter version.
- Bluetooth-only without the hub. citeturn0product9turn0product18

---

#### Best invisible-looking option
product["turn0product4","Level Bolt Matter Retrofit",{"render_as":"block","description":"Matter-over-Thread smart lock hidden inside the deadbolt for a completely stock appearance."}]

Level Bolt is unique because the smart parts hide inside the lock.
Pros:
- Looks completely normal
- Native Matter-over-Thread
- Great Apple Home integration

Cons:
- More involved installation
- Not as renter-friendly as SwitchBot or Aqara. citeturn0product4turn0product37

---

### Zigbee options

This category is surprisingly weak.

Most modern premium locks are moving toward:
- Matter over Thread
- Wi-Fi
- Bluetooth

Native Zigbee retrofit locks are rare in North America. The closest options are Tuya-based Zigbee locks, but they're usually full lock replacements rather than clean retrofit deadbolt turners. citeturn0product8turn0product23

For a Home Assistant homelab in 2026, I'd choose:

1. Aqara U200 (native Matter/Thread)
2. SwitchBot Lock Pro + Hub 2
3. Level Bolt Matter

The Aqara U200 is probably the closest thing to a "native Home Assistant nerd" choice right now. citeturn0product31turn0search1

explore_more{"selections":[["turn0product31","Aqara U200 Matter Retrofit Lock"],["turn0product9","SwitchBot Lock Pro"],["turn0product4","Level Bolt Matter Retrofit"],["turn0product2","Nuki Smart Lock Pro Matter"]]}

**You:** {"asset_pointer": "sediment://file_00000000d10071f5b41115164a9e1d1a", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 252247, "width": 1152}
{"asset_pointer": "sediment://file_00000000ab54722f81f93b7777b49f78", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 278916, "width": 1152}
Door does not close enough on first try to turn lock. Needs extra push

**ChatGPT:** Looking at your door, that's a very standard deadbolt thumb-turn, so **SwitchBot Lock Pro** and **Aqara U200** should both physically fit.

The bigger issue is what you mentioned:

> "Door does not close enough on first try to turn lock. Needs extra push."

That's important because most smart locks assume the deadbolt can lock smoothly.

### What will happen
If the deadbolt needs you to:
1. Close the door
2. Push the door inward
3. Then turn the lock

A smart lock may:
- Fail to lock
- Partially lock
- Drain batteries faster
- Repeatedly retry

### Good news
Both the Aqara U200 and SwitchBot Lock Pro have obstacle/jam detection and can retry, but neither can physically push the door closed.

### What I'd do first
Before buying any lock:

#### Test 1
Stand inside with the door open.

Can you turn the deadbolt fully with **one finger**?

If yes, the lock mechanism itself is fine.

#### Test 2
Close the door normally.

Try locking it without pushing.

- If it binds or sticks, the strike plate alignment is the problem.
- This is extremely common in apartment doors.

### Easy fixes
Usually one of:

- Adjust strike plate position
- Tighten hinge screws
- File the strike plate opening slightly
- Add a small weatherstrip adjustment

Many times a 5-minute strike plate adjustment fixes the issue completely.

### For your Home Assistant setup
I'd rank them:

1. **Aqara U200** (native Matter-over-Thread, no extra hub)
2. **SwitchBot Lock Pro + Hub 2**
3. Level Bolt

Given you already run Zigbee2MQTT and Home Assistant, the **Aqara U200** is probably the most attractive technically.

However, if the door regularly needs that extra shove, I'd fix the alignment first. Even a $300 smart lock can't compensate for a door that's not fully seated in the frame.

One more thing: when the door is closed, can you lock the deadbolt with **one finger and almost no resistance**, or does it require a noticeable amount of force? That tells me whether you're dealing with a minor alignment issue or a significant one.

**You:** Requires me to push door in. If it’s pushed in I can use 1 finger. If it’s closed but not extra pushed then it won’t lock at all

**ChatGPT:** That means the problem is **100% the door alignment**, not the lock.

The deadbolt is trying to extend into the strike plate, but the door isn't fully seated in the frame unless you push it.

For a smart lock, that's actually a bigger issue than which lock you buy.

### Before buying a smart lock
Lock the deadbolt with the door open:

- If it turns effortlessly → lock is fine.
- Your photos and description suggest this is the case.

Then when closed:
- Door must be pushed inward → strike plate/frame alignment issue.

### How this affects smart locks

#### Aqara U200
- Native Matter/Thread
- Excellent Home Assistant integration
- Less torque than SwitchBot
- More likely to fail if alignment isn't fixed

#### SwitchBot Lock Pro
- One of the strongest retrofit motors available
- Better chance of overcoming minor resistance
- Still cannot push the door closed
- If the bolt physically can't enter the strike plate, it will fail too

### What I'd do

For a rental apartment, try these in order:

1. **Check weatherstripping**
   - Sometimes new weatherstripping is thick and keeps the door from seating.

2. **Tighten hinge screws**
   - Often fixes sagging doors.

3. **Inspect strike plate**
   - Put lipstick, dry-erase marker, or painter's tape on the deadbolt.
   - Close door and try to lock.
   - You'll see exactly where the bolt is hitting.

4. **Ask maintenance**
   - "The deadbolt doesn't align with the strike plate unless I push the door inward."
   - That's a legitimate maintenance request.

### My recommendation

For your specific setup:

1. Fix the alignment issue first.
2. Then buy **Aqara U200** if you want the cleanest Home Assistant/Matter setup.
3. Buy **SwitchBot Lock Pro + Hub 2** if you want the most forgiving retrofit lock and don't mind the extra hub.

If maintenance won't fix it, I'd actually lean toward the **SwitchBot Lock Pro** because its motor is stronger and more tolerant of slightly imperfect doors. But even the SwitchBot can't lock a door that isn't fully closed—the door has to seat correctly first.

**You:** {"asset_pointer": "sediment://file_00000000449c720c98d6784371172a9f", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 1011663, "width": 1152}

**ChatGPT:** That photo actually helps a lot.

The gap you're showing on the hinge side looks larger than I'd expect for a properly seated exterior door. Combined with your description:

> Door closes, but deadbolt won't engage unless I push the door inward.

This strongly suggests one of these:

### Most likely: Weatherstripping compression
The door is hitting the weatherstripping and stopping before it's fully seated.

Common signs:
- Need shoulder pressure or a push to lock.
- Deadbolt works perfectly when door is pushed.
- Door latch itself catches normally.

### Second most likely: Strike plate alignment
The deadbolt hole in the frame is slightly off.

### Quick test
Close the door normally.

Look at the deadbolt side (opposite the hinges):

- Can you physically push the door inward another 1/8"–1/4"?
- Does the gap visibly shrink?

If yes, it's almost certainly weatherstripping or latch adjustment.

### What this means for smart locks

#### Aqara U200
I'd be nervous.

It has good jam detection, but if the door frequently needs that extra push, you'll get lock failures.

#### SwitchBot Lock Pro
Much better candidate.

You can create a Home Assistant automation:

1. Lock command sent.
2. If lock reports failure.
3. Notify you.

But it still can't push the door closed.

### One thing that might save you

The SwitchBot Lock Pro supports a magnetic door sensor.

If the sensor says:
- Door open → don't lock.
- Door closed → attempt lock.

That prevents a lot of failed lock attempts.

### What I'd do in your apartment

Before spending $150–300:

Submit maintenance request:

> "The deadbolt only locks when pressure is applied to the door. The strike alignment appears off."

Most apartment maintenance techs can fix this in under 10 minutes by adjusting the strike plate or latch alignment.

Once fixed:
- Aqara U200 becomes the best technical choice (Matter/Thread).
- SwitchBot Lock Pro becomes the best value choice.

Right now, with the door in its current state, I'd avoid buying any smart lock until maintenance takes a look. A smart lock will automate the problem, not solve it.

**You:** Weatherstripping

**ChatGPT:** If it's the weatherstripping, that's actually the best-case scenario.

From your description:

- Door latches normally ✅
- Deadbolt works with one finger when pushed in ✅
- Deadbolt won't lock unless the door is pushed inward ❌

That's classic "weatherstripping is holding the door slightly proud of the frame."

### Easy test

Close the door.

Put a piece of painter's tape on the frame right next to the door edge.

Now push the door inward firmly.

If the door moves inward even a small amount (1/16"–1/8"), that's enough to prevent many smart locks from locking reliably.

### Before calling maintenance

Try this:

1. Open the door.
2. Inspect the rubber weatherstrip on the latch side.
3. Look for:
   - Areas that are folded over
   - Thick new foam weatherstripping
   - Spots where the door leaves a heavy compression mark

If it's foam weatherstripping, you may simply need time for it to compress.

### Smart lock implications

For your specific situation:

**SwitchBot Lock Pro**
- More forgiving
- Stronger motor
- Has door-state sensors available
- I'd still feel comfortable buying it after confirming the weatherstripping issue is minor

**Aqara U200**
- Better Home Assistant/Matter integration
- Less tolerant of doors that don't seat properly
- I'd want the weatherstripping issue fixed first

Since you're a renter and already have Home Assistant, I'd probably:
1. Have maintenance adjust the door if they'll do it.
2. If they won't, buy the SwitchBot Lock Pro and test it.
3. Add a door sensor so Home Assistant only attempts locking when the door is fully closed.

One more question: when the door closes, do you hear **one click** from the knob latch, or do you have to pull/push the door to get a second, firmer click? That will tell us whether the latch itself is also being held out by the weatherstripping.

**You:** How do I fix this myself

**ChatGPT:** Based on your photos and description, I'd try the fixes in this order, from easiest to hardest.

### 1. Lubricate and exercise the weatherstripping (5 minutes)

If the apartment is newer, the weatherstripping may simply be stiff.

- Open the door.
- Wipe the weatherstripping clean.
- Spray a little silicone lubricant on a rag (not directly on the door).
- Wipe the rubber seal.
- Open and close the door 20–30 times.

Sometimes this alone helps the seal compress more easily.

---

### 2. Adjust the strike plate (10 minutes)

This is the most common fix.

Open the door and locate the metal plate where the deadbolt enters the frame.

If the door needs to be pushed inward, loosen the strike plate screws slightly and see if the plate has any play.

Sometimes moving it inward just 1/16" is enough.

You can also:

- Remove the strike plate.
- Use a file or Dremel to enlarge the hole slightly toward the inside of the apartment.
- Reinstall.

This is often invisible once reassembled.

---

### 3. Replace one hinge screw with a longer screw (10 minutes)

Your hinge photo shows standard hinges.

Try replacing the top hinge screw closest to the door stop with a:
- #9 or #10
- 2.5"–3" wood screw

As you tighten it, it pulls the door slightly toward the frame and can improve deadbolt alignment.

This is probably the highest success-rate DIY fix.

---

### 4. Check for weatherstrip pinch points

Close the door on a dollar bill at several spots.

If one section grips the bill much harder than the others, that area may be preventing the door from seating fully.

You can:
- Compress it by hand.
- Trim only if absolutely necessary (I'd avoid this in an apartment).

---

### Before buying a smart lock

Do this test:

1. Close the door normally.
2. Try locking the deadbolt.
3. Mark where the deadbolt hits the strike plate with a Sharpie or lipstick.
4. Open the door and inspect.

If the bolt is hitting the top, bottom, or edge of the strike plate opening, then alignment—not weatherstripping—is the primary problem.

For your apartment, I'd personally try the **longer top hinge screw first**. It costs about $1, takes 5 minutes, is completely reversible, and fixes a surprising number of doors that need a push before the deadbolt will engage.

**You:** Why is my lock getting stuck when fully extended

**ChatGPT:** If the deadbolt gets **stuck when fully extended**, that's a different symptom than the door needing a push.

Usually it means one of these:

### 1. Deadbolt is rubbing inside the strike plate (most likely)

When the bolt extends all the way, it's contacting the edge of the hole in the frame.

Signs:
- Last 10–20% of the turn is hard.
- Unlocking is also hard.
- Works smoothly when the door is open.

**Test:**
- Open the door.
- Extend and retract the deadbolt.

If it's buttery smooth with the door open but sticks with the door closed, the strike plate is the problem.

---

### 2. Deadbolt is bottoming out

The bolt extends deeper than the hole behind the strike plate.

Signs:
- Gets hard only at the very end.
- Door may lock, but unlocking feels sticky.

**Test:**
Put a flashlight into the strike plate hole and see how deep it is behind the metal plate.

---

### 3. Door is under pressure from weatherstripping

The weatherstripping pushes the door outward.

When the deadbolt extends, the bolt is fighting that pressure.

Signs:
- Easier to lock while pushing on the door.
- Easier to unlock while pulling on the door.

---

### 4. Deadbolt mechanism needs lubrication

Less likely since your issue changes when the door is pushed.

Test:
- Door open.
- Cycle the lock 20 times.

If it's still rough with the door open:
- Use dry graphite lock lubricant or a lock-specific lubricant.
- Avoid WD-40 inside the cylinder.

---

### The test I want you to do

With the door **open**:

1. Turn the deadbolt fully out.
2. Turn it fully in.
3. Repeat a few times.

Tell me:
- Is it smooth the entire way?
- Does it get hard right at the end even with the door open?

If it's smooth with the door open, then we know with about 95% confidence that the door/strike plate alignment or weatherstripping is the culprit—not the lock itself.

**You:** Ok I got it working by adjusting the strike plate

**ChatGPT:** Perfect. That's actually the outcome I was hoping for.

The fact that **adjusting the strike plate fixed it** tells us:

✅ Your deadbolt mechanism is fine  
✅ Weatherstripping wasn't the primary issue  
✅ The door wasn't aligned correctly with the strike plate  
✅ A smart lock is much more likely to work reliably now

Before you order anything, do one final test:

1. Close the door normally (don't push it).
2. Lock the deadbolt 10–20 times.
3. Unlock it 10–20 times.

You want:
- Smooth operation every time
- No sticking at full extension
- No need to push or pull the door
- One-finger operation

If it passes that test, I'd feel comfortable putting a smart lock on it.

For your Home Assistant setup:

**Best technical choice**
- Aqara U200
- Native Matter-over-Thread
- No cloud required
- Works great with Home Assistant

**Best value / safest retrofit**
- SwitchBot Lock Pro
- Strong motor
- Very renter-friendly
- Easy to remove when you move

Given your apartment door and the fact that you already have Zigbee2MQTT, Home Assistant, Apple devices, and a homelab, I'd probably lean toward the **Aqara U200** if you're okay spending more. If you want the proven, cheaper option, the **SwitchBot Lock Pro** is still excellent.

One thing I'd definitely add regardless of lock choice: a **door contact sensor**. That lets Home Assistant know whether the door is actually closed before attempting to lock it, which prevents most smart-lock headaches. Since you already have Zigbee2MQTT, a cheap Aqara or Sonoff Zigbee contact sensor integrates easily.

**You:** I don’t want a hub but I want cheap

**ChatGPT:** You basically have three competing requirements:

- ✅ Cheap
- ✅ No hub
- ✅ Retrofit (turns your existing deadbolt)

Unfortunately, you can realistically only get **two of the three**.

### Best fit for what you want

product["turn0product13","Aqara Smart Lock U200",{"render_as":"hero","description":"Native Matter-over-Thread retrofit lock that works without an Aqara hub if you already have a Thread border router."}]

The U200 is the only retrofit lock I'd seriously consider if you don't want a separate hub. It supports Matter over Thread natively. citeturn0product13turn0product3

### Budget alternatives

product["turn0product21","SwitchBot Smart Lock Pro",{"render_as":"block","description":"The cheapest quality retrofit option, but Matter requires an additional Hub 2."}]

product["turn0product0","Level Bolt Matter",{"render_as":"block","description":"Matter-over-Thread built in, but replaces internal deadbolt hardware rather than clamping over the thumb-turn."}]

| Feature | entity["turn0product13","Aqara Smart Lock U200"] | entity["turn0product21","SwitchBot Smart Lock Pro"] | entity["turn0product0","Level Bolt Matter"] |
|---|---|---|---|
| Retrofit over existing thumb-turn | Yes | Yes | No |
| Native Matter | Yes | No |
| Extra hub required | No* | Yes for Matter | No |
| Approx. price | ~$170–300 | ~$120–200 | ~$199 |
| Apartment friendly | Excellent | Excellent | Good |
| Home Assistant | Excellent | Excellent | Good |

\*You still need a **Thread border router** for Matter. The good news is you may already own one.

Since you have:
- Apple TV
- HomePod minis
- Home Assistant

You likely already have a Thread border router in your house, meaning the U200 can work without buying another Aqara hub. citeturn0product13turn0product3

### What I'd do in your shoes

If your budget is:
- **Under $150:** SwitchBot Lock Pro.
- **$170–230:** Aqara U200.
- **Over $230:** Still Aqara U200 for your Home Assistant setup.

Given that you just fixed the strike plate and already own Apple TV/HomePods, I'd save a little longer and get the **Aqara U200**. It's the cleanest "no hub" solution for a Home Assistant user. citeturn0product13turn0product3

explore_more{"selections":[["turn0product13","Aqara Smart Lock U200"],["turn0product21","SwitchBot Smart Lock Pro"],["turn0product0","Level Bolt Matter"],["turn0product38","August Wi-Fi Smart Lock"]]}

**You:** SwitchBot smart lock series. I want to not use a hub, Bluetooth adapter to something else may be acceptable though

**ChatGPT:** For your setup, I'd skip the Hub entirely and use Bluetooth locally through Home Assistant.

**The key thing:** Home Assistant can talk to SwitchBot locks directly over Bluetooth if you have a Bluetooth adapter nearby. You do **not** need a SwitchBot Hub for local control. The hub is mainly for:
- Matter
- Remote cloud access
- Siri/Alexa/Google integrations outside Bluetooth range citeturn0product0turn0product3

### Best overall
product["turn0product0","SwitchBot Lock Pro",{"render_as":"hero","description":"Strong retrofit lock with local Bluetooth control through Home Assistant and no required SwitchBot hub."}]

This is still the sweet spot:
- Strong motor
- Renter friendly
- Works with your existing deadbolt
- Home Assistant Bluetooth integration
- Cheaper than Aqara U200
- Easier fitment than many alternatives

### Also worth considering
product["turn0product31","SwitchBot Lock Ultra",{"render_as":"block","description":"Newer and quieter version with faster operation and improved compatibility."}]

The Ultra is basically the upgraded platform:
- Quieter
- Faster
- Better battery design
- More expensive
- Still benefits from a hub only if you want Matter features citeturn0product31turn0search0

| Feature | entity["turn0product0","SwitchBot Lock Pro"] | entity["turn0product31","SwitchBot Lock Ultra"] |
|---|---|---|
| Retrofit deadbolt turner | Yes | Yes |
| Home Assistant Bluetooth | Yes | Yes |
| SwitchBot Hub required | No | No |
| Matter without Hub | No | No |
| Motor strength | Very good | Excellent |
| Apartment friendly | Excellent | Excellent |
| Price | Lower | Higher |
| Good after your strike plate fix | Yes | Yes |

What I'd actually do with your homelab:

1. Buy the Lock Pro.
2. Add a cheap Bluetooth proxy near the door.

Examples:
- ESP32 running Bluetooth Proxy in Home Assistant
- Raspberry Pi with Bluetooth
- Home Assistant Bluetooth adapter

You already have multiple Raspberry Pis and Home Assistant, so this is basically free for you.

That gives you:
- Local control
- No cloud dependency
- No SwitchBot hub
- No Matter requirement
- Lower cost

A lot of Home Assistant users actually prefer this approach because it stays entirely local. The Reddit reports on the newer Lock Ultra also suggest Matter currently exposes fewer lock details than local integrations in some setups. citeturn0search0

products{"selections":[["turn0product0","SwitchBot Lock Pro"],["turn0product31","SwitchBot Lock Ultra"],["turn0product1","SwitchBot Lock Pro Black"],["turn0product38","SwitchBot Lock Ultra + Keypad Touch"]]}

For your apartment door specifically, after fixing the strike plate, I'd buy the Lock Pro and use an ESP32 Bluetooth proxy before spending extra money on a Hub 2.

**You:** What kinds of hub can I use

**ChatGPT:** For a SwitchBot lock, you have three realistic "hub" paths, and honestly the Home Assistant Bluetooth path fits your setup best.

### Best for your homelab (local, cheap, no SwitchBot hub)

product["turn0product1","Screek BP1 Bluetooth Proxy",{"render_as":"hero","description":"Tiny ESP32 Bluetooth proxy that extends Home Assistant Bluetooth coverage for SwitchBot devices without using a SwitchBot hub."}]

Home Assistant supports Bluetooth proxies natively through ESPHome. citeturn0search0

Since you already have:
- Home Assistant
- Raspberry Pis
- Zigbee2MQTT
- A server always running

you can place a Bluetooth proxy near the door and let Home Assistant communicate directly with the lock.

### Cheapest option
product["turn0product4","ESP32 Bluetooth Proxy Board",{"render_as":"block","description":"Preconfigured ESPHome Bluetooth proxy that works as a local Bluetooth bridge for Home Assistant."}]

Or spend even less:
- Buy a $5–10 ESP32 dev board
- Flash ESPHome Bluetooth Proxy
- Plug it in near the door

This is what a lot of Home Assistant users do. citeturn0search0

### Easiest official SwitchBot route
product["turn0product23","SwitchBot Hub Mini Matter Enabled",{"render_as":"block","description":"Official SwitchBot hub with Matter support and straightforward setup."}]

Pros:
- Easy
- Matter support
- Official

Cons:
- Extra cost
- Another ecosystem hub
- Less local than the Home Assistant Bluetooth approach

### Better official SwitchBot hub
product["turn0product20","SwitchBot Hub 2",{"render_as":"block","description":"Matter-capable SwitchBot hub with additional sensors and broader device support."}]

This is the one most people buy if they go the SwitchBot hub route.

---

| Feature | entity["turn0product1","Screek BP1 Bluetooth Proxy"] | entity["turn0product4","ESP32 Bluetooth Proxy Board"] | entity["turn0product23","SwitchBot Hub Mini Matter Enabled"] | entity["turn0product20","SwitchBot Hub 2"] |
|---|---|---|---|---|
| Works with Home Assistant | Excellent | Excellent | Good | Good |
| Fully local control | Yes | Yes | Partial | Partial |
| Matter support | Through HA setup | Through HA setup | Yes | Yes |
| Cost | ~$15 | ~$25 | ~$60 | ~$70–90 |
| Requires SwitchBot cloud | No | No | Usually for setup/features | Usually for setup/features |
| Best for your homelab | Yes | Yes | Medium | Medium |

For your specific setup, I'd buy:

1. entity["turn0product0","SwitchBot Lock Pro"]
2. A $5–15 ESP32 Bluetooth proxy (or use a spare Pi)
3. Run it through Home Assistant locally

That's the cheapest path, avoids another proprietary hub, and fits the infrastructure you already have. citeturn0search0

explore_more{"selections":[["turn0product0","Bluetooth Proxies BLEDongle-1M For HomeAssistant By SCREEK"],["turn0product1","Bluetooth Proxies BP1 For HomeAssistant By SCREEK"],["turn0product23","SwitchBot Hub Mini Matter Enabled"],["turn0product20","SwitchBot Hub 2 | 4-in-1 Smart Home Hub with Matter Support"]]}

**You:** I can’t use Apple?

**ChatGPT:** You absolutely can use Apple.

In fact, you already own some of the best hardware for this.

If you have:
- entity["product","HomePod mini","Apple smart speaker"]
- entity["product","Apple TV 4K","Apple streaming device"]

then you likely already have a **Thread Border Router** in your apartment. Apple devices like HomePod mini and newer Apple TV 4K models act as Thread border routers. citeturn0search0turn0product6turn0product33

The catch is with **SwitchBot specifically**:

### SwitchBot Lock Pro
product["turn0product31","SwitchBot Lock Pro + Hub Mini Matter Enabled",{"render_as":"block","description":"SwitchBot's official Matter-compatible package for Apple Home integration."}]

| Feature | entity["turn0product31","SwitchBot Lock Pro + Hub Mini Matter Enabled"] |
|---|---|
| Apple Home app | Yes |
| Siri unlock/lock | Yes |
| Matter | Yes |
| Requires SwitchBot Hub | Yes |
| Uses your HomePod mini as Thread router | Yes, after Matter setup |
| Cheapest route | No |

The annoying part is that SwitchBot does **not** expose Matter directly from the lock. The lock talks Bluetooth and the SwitchBot Hub translates it to Matter/HomeKit. citeturn0product31turn0product24

### What I'd do

Since you already have:
- Home Assistant
- HomePods
- Apple TV
- Bluetooth-capable devices

I'd skip the SwitchBot Hub and do:

### SwitchBot Lock Pro
product["turn0product31","SwitchBot Lock Pro + Hub Mini Matter Enabled",{"render_as":"block","description":"Works locally through Bluetooth and Home Assistant even if you don't buy the included hub."}]

plus:

### Bluetooth Proxy
product["turn0product41","Home Assistant Green",{"render_as":"block","description":"Represents the Home Assistant ecosystem that supports local Bluetooth proxies and lock integrations."}]

Then:
- Home Assistant controls the lock locally via Bluetooth
- Home Assistant exposes the lock to Apple Home
- Siri works through Home Assistant
- No SwitchBot Hub needed

This is actually the route many Home Assistant users prefer because it stays local and avoids another proprietary hub.

### Better Apple-native option

If Apple Home integration is more important than cost:

product["turn0product29","Aqara Smart Lock U300","{"render_as":"block","description":"Matter-over-Thread lock with strong Apple Home support and no separate Aqara hub required when you already own HomePod mini or Apple TV."}"]

The Aqara Matter locks talk directly to Apple's Thread network. Your HomePod mini or Apple TV acts as the border router. No Aqara hub required. citeturn0product29turn0search0

| Attribute | entity["turn0product31","SwitchBot Lock Pro + Hub Mini Matter Enabled"] | entity["turn0product29","Aqara Smart Lock U300"] |
|---|---|---|
| Retrofit over existing deadbolt | Yes | No |
| Apple Home support | Yes | Yes |
| Works without extra hub | Via Home Assistant Bluetooth | Yes |
| Native Thread | No | Yes |
| Cheapest | Yes | No |
| Best for your apartment door | Yes | Medium |

For *your* apartment and your existing homelab, I'd still buy the **SwitchBot Lock Pro**, add a Bluetooth proxy or use a nearby Pi/Home Assistant Bluetooth adapter, and expose it into Apple Home through Home Assistant. That gets you Siri control without buying another hub. citeturn0product31turn0search0

explore_more{"selections":[["turn0product31","SwitchBot Lock Pro + Hub Mini Matter Enabled"],["turn0product11","SwitchBot Hub Mini"],["turn0product2","Apple HomePod mini"],["turn0product6","Apple TV 4K Wi-Fi + Ethernet"]]}

**You:** Cheaper Bluetooth proxy option

**ChatGPT:** Since you already run urlHome Assistant Bluetooth Proxyturn0search0 and have spare Pis, I'd go as cheap as possible.

### Best value
product["turn0product1","SCREEK BP1 Bluetooth Proxy",{"render_as":"hero","description":"Prebuilt Home Assistant Bluetooth proxy that works out of the box and costs about the same as an ESP32 plus a case."}]

You basically:
- Plug it in
- Add it to Home Assistant
- Put it near the door

No flashing required.

### Cheapest DIY option
product["turn0product5","ESP32 Development Board Module",{"render_as":"block","description":"Ultra-cheap ESP32 board that can be flashed with ESPHome Bluetooth Proxy firmware for local SwitchBot connectivity."}]

This is what I'd personally do in your setup.

You flash ESPHome Bluetooth Proxy and you're done. citeturn0search0

### Easy DIY option
product["turn0product31","NodeMCU ESP32S CP2102 WiFi Bluetooth Board",{"render_as":"block","description":"Popular ESP32 board with good compatibility and easy setup for ESPHome Bluetooth Proxy."}]

A lot of Home Assistant users use boards like this because:
- USB powered
- Stable
- Cheap
- Tons of setup guides

### PRODUCT COMPARISON TABLE

| Attribute | entity["turn0product1","SCREEK BP1 Bluetooth Proxy"] | entity["turn0product5","ESP32 Development Board Module"] | entity["turn0product31","NodeMCU ESP32S CP2102 WiFi Bluetooth Board"] |
|---|---|---|---|
| Approx price | ~$15 | ~$3–5 | ~$8 |
| Requires flashing | No | Yes | Yes |
| Home Assistant Bluetooth Proxy support | Yes | Yes | Yes |
| Plug-and-play | Yes | No | No |
| Good for SwitchBot Lock Pro | Yes | Yes | Yes |
| Best for your homelab | Excellent | Excellent | Excellent |
| Technical difficulty | Low | Medium | Medium |

For you specifically:

- If you want **lowest cost possible** → entity["turn0product5","ESP32 Development Board Module"]
- If you want **least hassle** → entity["turn0product1","SCREEK BP1 Bluetooth Proxy"]

Since you already run Home Assistant, Docker, Proxmox, Zigbee2MQTT, and multiple Raspberry Pis, I honestly wouldn't buy a SwitchBot Hub at all. I'd spend ~$5–15 on an ESP32 Bluetooth proxy and use the lock locally through Home Assistant. citeturn0search0

explore_more{"selections":[["turn0product1","SCREEK BP1 Bluetooth Proxy"],["turn0product5","ESP32 Development Board Module"],["turn0product31","NodeMCU ESP32S CP2102 WiFi Bluetooth Board"],["turn0product2","ESP32 Development Board with ESPHome Bluetooth Proxy Installed"]]}

**You:** Why can’t I join the lock via matter on Apple

**ChatGPT:** Because the **SwitchBot Lock Pro itself is not a Matter device**.

That's the confusing part.

### SwitchBot architecture

| Device | Bluetooth | Matter | Apple Home directly |
|---|---|---|---|
| entity["turn0product0","SwitchBot Lock Pro"] | Yes | No | No |
| entity["turn0product9","SwitchBot Hub Mini Matter Enabled"] | Yes | Yes (bridge) | Yes |
| entity["turn0product14","SwitchBot Hub 2"] | Yes | Yes (bridge) | Yes |

The lock talks **Bluetooth only**. The Matter support comes from the hub acting as a bridge. SwitchBot's own documentation states that Matter support and Apple Home integration require a compatible hub. citeturn0product0turn0product9turn0product14

So even though you already own:
- entity["product","Apple HomePod mini","Apple smart speaker"]
- entity["product","Apple TV 4K","Apple streaming device"]

those only provide:
- Thread border router
- Apple Home hub functionality

They **cannot convert SwitchBot Bluetooth into Matter**.

### Why Aqara works differently

A lock like:
product["turn0product33","Aqara Smart Hub M100",{"render_as":"block","description":"Example Aqara Matter/Thread ecosystem hardware that communicates natively with Matter and Thread."}]

is built around Matter/Thread ecosystems, so Apple devices can talk to it more directly. citeturn0product33

### Your cheapest path

If you want:
- SwitchBot Lock Pro
- Apple Home
- Siri
- Lowest cost

then buy:

product["turn0product9","SwitchBot Hub Mini Matter Enabled",{"render_as":"hero","description":"Cheapest official way to expose a SwitchBot Lock Pro to Apple Home and Matter."}]

It's usually around $40–60 and is much cheaper than changing lock ecosystems. citeturn0product9turn0product4

### Alternative: no hub at all

You already run Home Assistant.

Use:
- SwitchBot Lock Pro
- ESP32 Bluetooth proxy
- Home Assistant HomeKit Bridge

Then:

SwitchBot Lock Pro → Bluetooth → Home Assistant → Apple Home

No SwitchBot hub required.

This is actually the route I'd take in your homelab because it's:
- cheaper
- fully local
- avoids another vendor hub
- works with Siri through Home Assistant

### Best option for you

product["turn0product0","SwitchBot Lock Pro",{"render_as":"block","description":"Best renter-friendly retrofit lock and works locally through Home Assistant Bluetooth without a SwitchBot hub."}]

| Attribute | entity["turn0product0","SwitchBot Lock Pro"] | entity["turn0product9","SwitchBot Hub Mini Matter Enabled"] | entity["turn0product14","SwitchBot Hub 2"] |
|---|---|---|---|
| Required for lock operation | Yes | No | No |
| Required for Apple Home direct Matter setup | No | Yes | Yes |
| Works with Home Assistant Bluetooth | Yes | — | — |
| Cheapest solution | Yes | Medium | No |
| Best fit for your existing homelab | Yes | Good | Good |

So the reason you can't just pair the Lock Pro to Apple Home is simply that Apple sees Matter, Thread, Wi-Fi, and HomeKit devices — but the Lock Pro is only exposing Bluetooth. Something has to bridge it, either:
1. a SwitchBot hub, or
2. Home Assistant. citeturn0product0turn0product5turn0product9

explore_more{"selections":[["turn0product0","SwitchBot Lock Pro"],["turn0product9","SwitchBot Hub Mini Matter Enabled"],["turn0product14","SwitchBot Hub 2"],["turn0product30","SwitchBot Lock Ultra"]]}

**You:** I don’t think my NUC has Bluetooth, would it? If not how do I enable it like a device or something

**ChatGPT:** Your **NUC10i5FNH almost certainly has built-in Bluetooth**.

Intel NUCs from that generation typically have:
- Wi-Fi 6
- Bluetooth 5.x
- Intel wireless card installed from the factory

Since your Plex server is the NUC10i5FNH running Ubuntu Docker, check first before buying anything.

SSH into the NUC and run:

```bash
bluetoothctl list
```

or

```bash
hciconfig -a
```

or

```bash
lsusb
```

You can also check in Home Assistant:

**Settings → Devices & Services → Bluetooth**

If Home Assistant sees a Bluetooth adapter, you're done.

---

### If the NUC doesn't have Bluetooth

Cheapest option:

A generic USB Bluetooth 5.0 dongle.

Look for:
- ASUS USB-BT500
- TP-Link UB500
- Plugable USB Bluetooth 5

Usually $10–20.

Plug it into the NUC and Home Assistant should discover it.

---

### But here's the catch

Your lock is at the apartment door.

Your NUC may be:
- In your office
- In a closet
- In a rack

Bluetooth range through walls is often disappointing.

For a lock, I prefer:

```text
SwitchBot Lock
       ↓
ESP32 Bluetooth Proxy
       ↓ WiFi
Home Assistant
```

An ESP32 near the door gives much more reliable connectivity than a USB Bluetooth dongle plugged into a server across the apartment.

---

### What I'd do in your apartment

1. Buy the SwitchBot Lock Pro.
2. Check if Home Assistant can already see Bluetooth on the NUC.
3. If it can:
   - Test the lock first.
4. If signal is weak:
   - Add a $5–10 ESP32 Bluetooth Proxy near the entryway.

Since you already have multiple Raspberry Pis and a Home Assistant setup, I'd spend **$0 first** and see whether the NUC's built-in Bluetooth reaches the door. There's a good chance it does if the NUC isn't too far away.

**You:** Not that NUC the home assistant one

**ChatGPT:** Your Home Assistant NUC is the **NUC8i7BEH**, right?

That model almost certainly shipped with:
- Intel Wireless-AC 9560
- Bluetooth 5.0 built in citeturn0search0

Before buying anything, check Home Assistant:

**Settings → Devices & Services → Bluetooth**

If Bluetooth appears there, you're done.

Or on the host:

```bash
bluetoothctl list
```

or

```bash
hciconfig -a
```

If you don't see Bluetooth, it could be:
- disabled in BIOS
- not passed through correctly (if HA is in a VM)
- missing drivers
- wireless card removed

For your setup, if Bluetooth is missing or weak, I'd use a cheap USB adapter.

### Best cheap option
product["turn0product5","ASUS USB-BT500 Bluetooth 5.0 Adapter",{"render_as":"hero","description":"Reliable Bluetooth 5 adapter commonly used with Linux and Home Assistant setups."}]

### Cheapest option
product["turn0product36","TP-Link UB500 Bluetooth 5.0 Nano USB Adapter",{"render_as":"block","description":"Tiny inexpensive Bluetooth adapter that works well for many Home Assistant Bluetooth integrations."}]

### Better range option
product["turn0product27","TP-Link UB500 Plus Bluetooth 5.3 Adapter",{"render_as":"block","description":"Bluetooth adapter with external antenna for stronger lock connectivity if the NUC is farther from the door."}]

| Attribute | entity["turn0product5","ASUS USB-BT500 Bluetooth 5.0 Adapter"] | entity["turn0product36","TP-Link UB500 Bluetooth 5.0 Nano USB Adapter"] | entity["turn0product27","TP-Link UB500 Plus Bluetooth 5.3 Adapter"] |
|---|---|---|---|
| Approx cost | ~$20 | ~$15 | ~$20 |
| Linux/Home Assistant use | Good | Good | Good |
| External antenna | No | No | Yes |
| Best for lock reliability | Good | Good | Best |
| Plug-and-play | Usually | Usually | Usually |

For your apartment specifically:

- If the NUC is within ~20 feet of the door → try built-in Bluetooth first.
- If Bluetooth is weak → buy the TP-Link UB500 Plus with the antenna.
- If you later want maximum reliability → add a cheap ESP32 Bluetooth proxy near the door.

First thing I'd do is check whether Home Assistant already sees Bluetooth. There's a decent chance the NUC8 already has everything you need. citeturn0search0

explore_more{"selections":[["turn0product5","ASUS USB-BT500 Bluetooth 5.0 Adapter"],["turn0product36","TP-Link UB500 Bluetooth 5.0 Nano USB Adapter"],["turn0product27","TP-Link UB500 Plus Bluetooth 5.3 Adapter"],["turn0product2","Plugable USB Bluetooth 5 Adapter"]]}

**You:** If it sees blue tooth can it talk to the lock without anything else

**ChatGPT:** Yes.

If all of these are true:

- Your Home Assistant NUC can see Bluetooth
- The NUC is close enough to the front door
- You install the SwitchBot integration in Home Assistant

Then the setup is simply:

```text
SwitchBot Lock Pro
        ↓ Bluetooth
Home Assistant
        ↓
Automations / Dashboard / Apple Home via HomeKit Bridge
```

No SwitchBot Hub.
No Aqara Hub.
No Matter.

### How to check

In Home Assistant:

**Settings → Devices & Services → Bluetooth**

If Bluetooth is working, you'll see a Bluetooth integration loaded.

Then install the SwitchBot integration:

**Settings → Devices & Services → Add Integration → SwitchBot**

If the lock is within range, Home Assistant should discover it.

### For Apple Home

You still don't need a SwitchBot Hub.

Use Home Assistant's HomeKit Bridge:

```text
SwitchBot Lock
    ↓ Bluetooth
Home Assistant
    ↓ HomeKit Bridge
Apple Home
```

Your HomePod mini / Apple TV acts as the Apple Home hub.

### The only thing that might stop you

Distance.

Bluetooth locks are much more sensitive than Bluetooth headphones.

If your NUC is:
- Same room = usually great
- One wall away = often fine
- Across apartment = maybe
- In a closet/rack at the far end = unreliable

Given your apartment layout, if the Home Assistant NUC is within about 15–20 feet of the entry door, I'd try it with **zero additional hardware** before buying anything.

A quick check:
- Where is the NUC physically located relative to the front door?
- Same room, one room away, or opposite end of the apartment?

That will tell us whether you'll likely need an ESP32 proxy or not.

**You:** In network rack about 15 feet 1 wall

**ChatGPT:** Honestly, **15 feet and one wall is probably fine**.

I'd estimate:

- 70–90% chance the NUC's built-in Bluetooth can talk directly to the lock.
- 95%+ if the wall isn't masonry, tile, or metal-backed.

Before buying any Bluetooth proxy or hub, I'd do this:

1. Install the lock.
2. Add the SwitchBot integration in Home Assistant.
3. See if Home Assistant discovers it.
4. Test:
   - Lock
   - Unlock
   - Battery reporting
   - Status updates

If commands complete in 1–3 seconds consistently, you're done.

### Worst case

If the signal is weak, then spend $5–10 on an ESP32 Bluetooth proxy and plug it somewhere near the front door.

Since you already have:
- Home Assistant
- Apple TV
- HomePod minis
- Zigbee2MQTT
- A homelab

I would **not buy a SwitchBot Hub Mini or Hub 2** just for the lock.

### My recommendation

For your apartment:

1. Buy **SwitchBot Lock Pro**.
2. Try direct Bluetooth from Home Assistant.
3. Expose it to Apple Home through the HomeKit Bridge integration.
4. Only buy an ESP32 Bluetooth proxy if the connection proves unreliable.

That's the cheapest path and keeps everything local.

One other thing: since you fixed the strike plate, I'd manually lock/unlock the deadbolt about 20 times tonight. If it never sticks now, you're in a good place for a motorized lock. A smart lock will amplify any mechanical issues, so you want it feeling smooth before installation.

**You:** Which switch bot locks are blue tooth controlled and can lock unlock with features listed

**ChatGPT:** For **your use case** (renter, existing deadbolt, Home Assistant, no hub required), there are really only two SwitchBot locks I'd consider.

product["turn0product1","SwitchBot Lock Pro",{"render_as":"block","description":"The proven retrofit lock with Bluetooth control, auto-lock, Home Assistant compatibility, and optional keypad support."}]

product["turn0product13","SwitchBot Lock Ultra",{"render_as":"block","description":"The newer, faster, quieter model with improved battery system and Apple Home Key support in supported configurations."}]

| Feature | entity["turn0product1","SwitchBot Lock Pro"] | entity["turn0product13","SwitchBot Lock Ultra"] |
|---|---|---|
| Bluetooth control | Yes | Yes |
| Home Assistant via Bluetooth | Yes | Yes |
| No SwitchBot hub required | Yes | Yes |
| Auto-lock | Yes | Yes |
| Lock/unlock from app | Yes | Yes |
| Physical key still works | Yes | Yes |
| Existing deadbolt stays installed | Yes | Yes |
| Keypad support | Yes | Yes |
| Fingerprint support (with keypad) | Yes | Yes |
| Apple Home / Matter without hub | No | No* |
| Quieter/faster | Good | Better |
| Price | Lower | Higher |

\*The Ultra has newer Apple Home Key/Matter options depending on bundle and accessories, but the simplest local setup is still Bluetooth to Home Assistant. citeturn0product37turn0product13

### What you can do without any hub

With either lock:

- Lock/unlock from Home Assistant
- Lock/unlock from your phone over Bluetooth
- Auto-lock after X seconds
- Notifications when locked/unlocked
- Add to Apple Home through Home Assistant HomeKit Bridge
- Create automations (leave home = lock, bedtime = lock, etc.)

Assuming the Bluetooth connection reaches your NUC. citeturn0product1turn0search0

### If you add a keypad

product["turn0product26","SwitchBot Keypad Touch",{"render_as":"block","description":"Adds fingerprint unlock, PIN codes, NFC cards, and guest access to the SwitchBot lock."}]

Then you gain:
- Fingerprint unlock
- PIN codes
- Temporary guest codes
- NFC cards
- Family member access

without needing a hub. citeturn0product26turn0product14

### What I'd buy

For your apartment:

**SwitchBot Lock Pro + Keypad Touch**

Why:
- Cheapest good setup
- Fingerprint unlock
- Bluetooth only
- Home Assistant compatible
- Keeps your existing lock
- Works well for renters
- You've already fixed the strike plate issue

The Ultra is nice, but I don't think it's worth the extra money for your first smart lock. The Pro is mature, proven, and does everything you've asked for. citeturn0product1turn0product14

**You:** List all options

**ChatGPT:** Since you're specifically looking at **SwitchBot retrofit locks** that fit over your existing deadbolt, here are the actual options worth considering.

products{"selections":[["turn0product0","SwitchBot Lock Pro"],["turn0product24","SwitchBot Lock Ultra"],["turn0product38","SwitchBot Lock Vision"],["turn0product2","SwitchBot Lock Vision Pro"]]}

### Current SwitchBot Retrofit Lineup

| Feature | entity["turn0product0","SwitchBot Lock Pro"] | entity["turn0product24","SwitchBot Lock Ultra"] | entity["turn0product38","SwitchBot Lock Vision"] | entity["turn0product2","SwitchBot Lock Vision Pro"] |
|---|---|---|---|---|
| Fits existing deadbolt | Yes | Yes | Yes | Yes |
| Bluetooth control | Yes | Yes | Yes | Yes |
| Home Assistant via Bluetooth | Yes | Yes | Yes | Yes |
| Hub required for basic use | No | No | No | No |
| Auto-lock | Yes | Yes | Yes | Yes |
| Physical key still works | Yes | Yes | Yes | Yes |
| Fingerprint unlock | With keypad | With keypad | Optional | Included |
| Facial recognition | No | No | Yes | Yes |
| Quiet mode | Basic | Improved | Improved | Improved |
| Matter support | Hub required | Hub required | Hub required | Hub required |
| Approx. cost | Lowest | Low-Mid | Mid | Highest |

### What I'd buy for your setup

#### Best value
product["turn0product0","SwitchBot Lock Pro",{"render_as":"hero","description":"Cheapest proven retrofit lock with Bluetooth, Home Assistant support, auto-lock, and optional fingerprint keypad."}]

Why it fits you:
- Apartment renter
- Existing deadbolt
- Home Assistant
- No hub required
- Network rack only ~15 ft away
- Cheapest option that still does everything important citeturn0product0turn0product9

#### If buying today with a little extra budget
product["turn0product24","SwitchBot Lock Ultra",{"render_as":"block","description":"Newer, quieter, faster version with better battery design and broader lock compatibility."}]

The Ultra is essentially the next-generation Lock Pro. It adds quieter operation, faster response, and better battery redundancy. citeturn0product24turn0product37

#### If you want face unlock
product["turn0product38","SwitchBot Lock Vision",{"render_as":"block","description":"Adds 3D facial recognition so the door unlocks as you approach."}]

Cool technology, but probably overkill for your apartment. citeturn0product38turn0product41

### Accessories

If you want fingerprint unlock:

product["turn0product6","SwitchBot Keypad Touch",{"render_as":"block","description":"Adds fingerprint reader, PIN codes, NFC cards, and guest access without requiring a hub."}]

For most people, **Lock Pro + Keypad Touch** is the sweet spot. citeturn0product6turn0product1

### For your exact situation

Given:
- You fixed the strike plate
- You have Home Assistant
- You don't want another hub
- You want cheap
- You already have Apple TVs/HomePods

I'd rank them:

1. **SwitchBot Lock Pro**
2. **SwitchBot Lock Ultra**
3. **SwitchBot Lock Pro + Keypad Touch**
4. Vision models

The Lock Pro is still the one I'd spend my own money on in your apartment. It gets you Bluetooth control, Home Assistant integration, auto-lock, Apple Home exposure through Home Assistant, and keeps the total cost reasonable. citeturn0product0turn0search0

**You:** What about the base one

**ChatGPT:** The **base SwitchBot Lock** (the one before the Pro existed) is still a viable option for you, but I wouldn't buy it today unless you find a really good deal.

product["turn0product8","SwitchBot Lock",{"render_as":"block","description":"The original retrofit Bluetooth smart lock that mounts over your existing deadbolt and works without a hub."}]

product["turn0product3","SwitchBot Lock Pro",{"render_as":"block","description":"The upgraded version with stronger motor, better compatibility, improved battery system, and more unlock methods."}]

| Attribute | entity["turn0product8","SwitchBot Lock"] | entity["turn0product3","SwitchBot Lock Pro"] | entity["turn0product6","SwitchBot Lock Ultra"] |
|---|---|---|---|
| Bluetooth control | Yes | Yes | Yes |
| Home Assistant Bluetooth | Yes | Yes | Yes |
| Hub required | No | No | No |
| Auto lock | Yes | Yes | Yes |
| Works over existing deadbolt | Yes | Yes | Yes |
| Motor strength | Good | Better | Best |
| Battery system | Basic | Improved | Triple battery protection |
| Lock compatibility | Good | Better | Best |
| Apartment/rental use | Excellent | Excellent | Excellent |
| Value today | Fair | Excellent | Good |

The biggest difference is that the **Pro was specifically designed to fix complaints about the original Lock**—stronger motor, better fitment, better batteries, and broader deadbolt compatibility. SwitchBot itself describes the Pro as being more compatible and more robust than the original. citeturn0search0turn0product3

For **your apartment**:
- You already fixed the strike plate.
- You want Bluetooth.
- You want Home Assistant.
- You don't want another hub.

So I'd rank them:

1. **SwitchBot Lock Pro** ← sweet spot
2. **SwitchBot Lock Ultra** ← only if you want the newest model
3. **Original SwitchBot Lock** ← only if it's significantly cheaper

If you can get the original Lock for **under $80**, it's worth considering. If it's within $20–30 of the Pro, I'd spend the extra money and get the Pro every time. citeturn0product8turn0product3

explore_more{"selections":[["turn0product8","SwitchBot Lock"],["turn0product3","SwitchBot Lock Pro"],["turn0product6","SwitchBot Lock Ultra"],["turn0product25","SwitchBot Lock Vision"]]}
