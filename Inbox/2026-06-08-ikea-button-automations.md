---
date: 2026-06-08
source: chatgpt
title: "IKEA Button Automations"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** I added IKEA smart buttons

**ChatGPT:** Nice. IKEA buttons open up a lot of useful Home Assistant automations.

Based on your setup, I'd use them for things that are annoying to do with motion sensors alone:

### 1. Bedroom "Going to Bed" Button
Put it on your nightstand.

**Single Press**
- Sets `input_boolean.sleep_mode` = on
- Turns off living room, kitchen, office lights
- Leaves bedroom lights alone

**Double Press**
- Triggers your night-motion automation mode
- All non-bedroom lights can come on at 1% if motion is detected overnight

**Long Press**
- Turns everything in the apartment off

---

### 2. Office Button
Put on your desk.

**Single Press**
- Office lights on
- Office fan on

**Double Press**
- Office lights 100%
- Focus/work scene

**Long Press**
- Everything in office off

---

### 3. Living Room Movie Button
Near couch.

**Single Press**
- Living room lamps 20%
- Home theater smart plug on

**Double Press**
- All living room lights off

**Long Press**
- Turn everything in apartment off

---

### 4. Home Assistant Panic Button
Hidden somewhere.

**Single Press**
- Turn all lights on

**Long Press**
- Turn all smart plugs off
- Useful if something gets stuck on

---

### 5. Arrival Button
Near front door.

**Single Press**
- Kitchen light on
- Living room light on
- Office light on

**Long Press**
- Leaving home scene
- All lights off
- Fan off
- Home theater off

---

To write the actual automations, I need the IKEA button entity names. In Home Assistant go to:

**Settings → Devices & Services → Devices → IKEA Button**

and send:
- Device name(s)
- Entity IDs
- Or a screenshot of the button device page

Then I can generate the exact YAML for your setup instead of placeholders.

**You:** One is at kitchen near entry. Other 2 are at bathroom and bedroom doors

**ChatGPT:** Perfect. I’d map them like this:

### Kitchen entry button
**Single press:** “I’m home”
- Kitchen light on
- Living room lights on
- Office lamp on if dark

**Double press:** “Leaving”
- All lights off
- Fans off
- Home theater plug off

**Long press:** “All lights on”
- Useful when walking in or cleaning

### Bathroom door button
**Single press:** bathroom/night path
- Non-bedroom lights to 1%
- Bedroom stays off

**Double press:** normal hallway/kitchen light
- Kitchen/living room lights on low

**Long press:** all non-bedroom lights off

### Bedroom door button
**Single press:** bedtime mode
- Turn off living room, kitchen, office
- Enable sleep/night motion mode

**Double press:** night path
- All non-bedroom lights to 1%

**Long press:** everything off except bedroom untouched

Next step: send the three button **device names or event/entity IDs** from Home Assistant, and I’ll write the exact YAML.

**You:** BILRESA

**ChatGPT:** `BILRESA` is the IKEA button model/name.

In Home Assistant, use the button **device trigger**, not an entity ID.

Go to:

**Settings → Automations & Scenes → Create Automation → Add Trigger → Device**

Pick each **BILRESA** button and you should see triggers like:

- Short press
- Double press
- Long press

Name the three devices something like:

- `IKEA Button - Kitchen Entry`
- `IKEA Button - Bathroom Door`
- `IKEA Button - Bedroom Door`

Then I can write the YAML using those device triggers.

**You:** But each button has a bottom and top

**ChatGPT:** Even better.

The IKEA **BILRESA** buttons have **top** and **bottom** buttons, and Home Assistant usually exposes events for:

- Top button short press
- Top button long press
- Bottom button short press
- Bottom button long press

That effectively gives you **4 actions per button**.

For your locations, I'd do:

## Kitchen Entry Button

### Top Press
"I'm home"
- Kitchen light on
- Living room lights on
- Office lamp on if dark

### Top Hold
All lights on

### Bottom Press
Leaving home
- All lights off
- Fan off
- Home theater off

### Bottom Hold
Emergency everything off
- All lights
- All smart plugs

---

## Bathroom Door Button

### Top Press
Night path
- Kitchen
- Living room
- Hallway
- Office
all at 1%

### Top Hold
Bathroom bright mode
- Nearby lights 100%

### Bottom Press
Turn off night path lights

### Bottom Hold
All non-bedroom lights off

---

## Bedroom Door Button

### Top Press
Bedtime
- Enable sleep mode helper
- Turn off kitchen
- Turn off living room
- Turn off office

### Top Hold
Goodnight
- Everything off except bedroom

### Bottom Press
Late-night snack mode
- Kitchen and path lights 1%

### Bottom Hold
Disable sleep mode

---

Honestly, these buttons are more useful than motion sensors for your apartment because you can intentionally switch between:
- Home
- Away
- Bedtime
- Night path
- Movie mode

without the automations guessing what you're doing.

If you show me one BILRESA device page (the triggers/events Home Assistant lists), I can write the exact YAML using the actual event names Home Assistant is generating.

**You:** {"asset_pointer": "sediment://file_000000007ca8722fb94c568248613656", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 180750, "width": 709}
{"asset_pointer": "sediment://file_0000000063c0722fb066b840f8fcab6d", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 207027, "width": 709}
{"asset_pointer": "sediment://file_00000000dc2c720ca03dbe7929766d8e", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 206961, "width": 709}
{"asset_pointer": "sediment://file_00000000ad9071f589c35a189f35eb67", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 182930, "width": 709}
{"asset_pointer": "sediment://file_00000000be48720c9a5635f3ca8d7fc1", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 199399, "width": 709}
{"asset_pointer": "sediment://file_000000006cfc722fb2f5c878f66c8f6b", "content_type": "image_asset_pointer", "fovea": null, "height": 1536, "metadata": {"asset_pointer_link": null, "container_pixel_height": null, "container_pixel_width": null, "dalle": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "generation": null, "gizmo": null, "is_no_auth_placeholder": null, "lpe_delta_encoding_channel": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "watermarked_asset_pointer": null}, "size_bytes": 202594, "width": 709}

**ChatGPT:** You're close, but those screenshots don't show the actual button events.

I can see:

- Kitchen Button
- Bathroom Button
- Bedroom Button
- `Button (1)`
- `Button (2)`

What I need is what event Home Assistant generates when you press them.

### Do this:

**Developer Tools → Events**

Listen to:

```text
state_changed
```

Then:

1. Press the TOP button on the Bedroom Button.
2. Stop listening.
3. Copy the event that appears.

Or easier:

**Settings → Devices → Bedroom Button → Automations → Create Automation**

When selecting a trigger, Home Assistant should show options such as:

- Button (1) pressed
- Button (1) long pressed
- Button (2) pressed
- Button (2) long pressed

Take a screenshot of that trigger selection screen.

---

Based on the Matter device, I'm 95% sure:

- Button (1) = Top button
- Button (2) = Bottom button

If that's true, I'd configure them like this:

### Kitchen Button
**Top**
- Kitchen + Living Room lights on

**Bottom**
- Leaving Home
  - All lights off
  - Fan off
  - Home Theater off

### Bathroom Button
**Top**
- Night path mode
  - Kitchen, Living Room, Office = 1%

**Bottom**
- Turn off night path lights

### Bedroom Button
**Top**
- Bedtime
  - All non-bedroom lights off
  - Enable sleep mode

**Bottom**
- Midnight snack
  - Kitchen path lights = 1%

Honestly, for your apartment, the Bedroom button triggering Sleep Mode is probably the most useful automation you've added so far because it can tie into the overnight motion automations we've already discussed. Send the trigger screen and I'll write the exact automations.

**You:** description: ""
mode: single
triggers:
  - device_id: c283294877631640f647551e004184c0
    domain: button
    entity_id: ce9dc48daac366a57868f3481d10fd5f
    type: pressed
    trigger: device
conditions:
  - type: is_battery_level
    condition: device
    device_id: e32b7604418c3a410d6fb80bb8f11ea2
    entity_id: 711396304a13b8a56935fa4da2829c64
    domain: sensor
actions:
  - device_id: 8a97d9426db4340ff1434e62acaafd1f
    domain: button
    entity_id: a37f43046d4b008eb659dbcd21c8fb18
    type: press

**ChatGPT:** That YAML is not useful yet because it has:

```yaml
conditions:
  - type: is_battery_level
```

That means the button only works based on a battery condition, not what you want.

Also this action:

```yaml
domain: button
type: press
```

is pressing another button entity, not turning lights on/off.

Use this structure instead:

```yaml
alias: Kitchen Button - Entry Lights
description: ""
mode: single

trigger:
  - platform: device
    device_id: c283294877631640f647551e004184c0
    domain: button
    entity_id: ce9dc48daac366a57868f3481d10fd5f
    type: pressed

condition: []

action:
  - service: light.turn_on
    target:
      entity_id:
        - light.kitchen_light
        - light.living_room
```

Replace the light IDs with your real ones.

For your button automations, **delete the battery condition** and use the button press only as the trigger.

**You:** That code is from home assistant

**ChatGPT:** Right — Home Assistant generated it, but it generated a bad starter automation because you accidentally selected:

- a **battery condition**
- a **button press action**

Instead, keep the **trigger** only.

Use this:

```yaml
description: ""
mode: single
triggers:
  - device_id: c283294877631640f647551e004184c0
    domain: button
    entity_id: ce9dc48daac366a57868f3481d10fd5f
    type: pressed
    trigger: device
conditions: []
actions:
  - action: light.turn_on
    target:
      entity_id:
        - light.kitchen_light
```

Then add the lights/switches you want under `entity_id`.

The important part: **Button (1)/(2) entities are triggers only. You don’t “press” them as actions.**
