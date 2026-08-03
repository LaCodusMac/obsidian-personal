---
date: 2026-06-01
source: chatgpt
title: "Home Assistant Automations"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Living Room

Kitchen

Bedroom

Office

Bathroom

Kitchen (2)Today's consumption
Bedroom ▸ BedroomDoor
Sensor

Today's consumption
Bedroom ▸ BedRoomFarsideLight
Sensor

Today's consumption
Office ▸ Office
Sensor

Today's consumption
Office ▸ Office2
Sensor

Today's consumption
Office ▸ OfficeLamp
Sensor

Total consumption
Bedroom ▸ Bedroom near window
Sensor

Total consumption
Bedroom ▸ BedroomDoor
Sensor

Total consumption
Bedroom ▸ BedRoomFarsideLight
Sensor

Total consumption
Office ▸ Office
Sensor

Total consumption
Office ▸ Office2
Sensor

Total consumption
Office ▸ OfficeLamp
Sensor

Turn off delay
Kitchen ▸ Kitchen Light
Number

Turn off delay
Living Room ▸ Smart Plug Home Theater
Number

Turn off delay
Office ▸ Smart Plug for fan
Number

Turn off delay
Office ▸ Smart Plug Home Lab
Number

Turn on delay
Kitchen ▸ Kitchen Light
Number

Turn on delay
Living Room ▸ Smart Plug Home Theater
Number

Turn on delay
Office ▸ Smart Plug for fan
Number

Turn on delay
Office ▸ Smart Plug Home Lab
Number

Update
AirCast
Update

Update
Home Assistant Core
Update

Update
Home Assistant Operating System
Update

Update
Home Assistant Supervisor
Update

Update
Matter Server
Update

Update
Mosquitto broker
Update

Update
Plex Media Server
Update

Update
Spotify Connect
Update

Update
Zigbee2MQTT
Update

Upload throughput
goingmerry
Sensor

Used space
goingmerry (Volume 1)
Sensor

Voltage
Kitchen ▸ Kitchen Light
Sensor

Voltage
Living Room ▸ Smart Plug Home Theater
Sensor

Voltage
Office ▸ Smart Plug for fan
Sensor

Voltage
Office ▸ Smart Plug Home Lab
Sensor

Volume used
goingmerry (Volume 1)
Sensor
AirCast
Home Assistant Supervisor


Backup
Backup


Bathroom
Bathroom
Apple TV


Bedroom near window
Bedroom
TP-Link Smart Home


Bedroom TV
Bedroom
Android TV Remote


Bedroom TV
Bedroom
Google Cast

Bedroom TV:21066
HomeKit Bridge


Bedroom
Bedroom
Apple TV


BedroomDoor
Bedroom
TP-Link Smart Home


BedRoomFarsideLight
Bedroom
TP-Link Smart Home


E26LivingRoomLightBig
Living Room
Zigbee Home Automation


E26LivingRoomSmall
Living Room
Zigbee Home Automation


Forecast
Meteorologisk institutt (Met.no)


goingmerry (Drive 1)
Synology DSM


goingmerry (Drive 2)
Synology DSM


goingmerry (Volume 1)
Synology DSM


goingmerry
Synology DSM


Google Translate en com
Google Translate text-to-speech

HASS Bridge:21064
HomeKit Bridge


Home Assistant Connect ZBT-2 (DCB4D90D54E0)
Office
Home Assistant Connect ZBT-2


Home Assistant Connect ZBT-2
Office
Zigbee Home Automation


Home Assistant Core
Home Assistant Supervisor


Home Assistant Host
Home Assistant Supervisor


Home Assistant Operating System
Home Assistant Supervisor 

All YAML configuration
Reload

Automations
Reload

Conversation
Reload

HomeKit
Reload

Input booleans
Reload

Input buttons
Reload

Input datetimes
Reload

Input numbers
Reload

Input selects
Reload

Input texts
Reload

Location & customizations
Reload


Manually configured MQTT entities
Reload

People
Reload

Restart Home Assistant
Interrupts all running automations and scripts

Scenes
Reload

Schedule
Reload

Scripts
Reload

Stop Home Assistant
Interrupts all running automations and scripts


Themes
Reload

Timer
Reload

Zones
Reload

**ChatGPT:** I can work from this. The big thing I see is you pasted mostly device/entity names, not the exact `entity_id`s, so I’ll write the automations using likely IDs and show you exactly where to swap them if Home Assistant names differ.

**ChatGPT:** Use these as **starter automations**. Replace any entity that is red in Home Assistant with your real entity ID from **Settings → Devices & services → Entities**.

```yaml
alias: Kitchen auto off after delay
trigger:
  - platform: state
    entity_id: light.kitchen_light
    to: "on"
    for:
      minutes: 30
action:
  - service: light.turn_off
    target:
      entity_id: light.kitchen_light
mode: restart
```

```yaml
alias: Office fan on when hot
trigger:
  - platform: numeric_state
    entity_id: sensor.office_temperature
    above: 75
action:
  - service: switch.turn_on
    target:
      entity_id: switch.smart_plug_for_fan
mode: single
```

```yaml
alias: Office fan off when cool
trigger:
  - platform: numeric_state
    entity_id: sensor.office_temperature
    below: 72
    for:
      minutes: 10
action:
  - service: switch.turn_off
    target:
      entity_id: switch.smart_plug_for_fan
mode: single
```

```yaml
alias: Bedroom motion night light
trigger:
  - platform: state
    entity_id: binary_sensor.bedroom_motion
    to: "on"
condition:
  - condition: sun
    after: sunset
    before: sunrise
action:
  - service: light.turn_on
    target:
      entity_id:
        - light.bedroom_near_window
        - light.bedroomdoor
    data:
      brightness_pct: 30
mode: restart
```

```yaml
alias: Bedroom lights off after no motion
trigger:
  - platform: state
    entity_id: binary_sensor.bedroom_motion
    to: "off"
    for:
      minutes: 10
condition:
  - condition: sun
    after: sunset
    before: sunrise
action:
  - service: light.turn_off
    target:
      entity_id:
        - light.bedroom_near_window
        - light.bedroomdoor
        - light.bedroomfarsidelight
mode: restart
```

```yaml
alias: Home theater off overnight
trigger:
  - platform: time
    at: "02:00:00"
action:
  - service: switch.turn_off
    target:
      entity_id: switch.smart_plug_home_theater
mode: single
```

```yaml
alias: Home lab power warning
trigger:
  - platform: numeric_state
    entity_id: sensor.smart_plug_home_lab_power
    above: 250
    for:
      minutes: 10
action:
  - service: notify.mobile_app_YOUR_PHONE
    data:
      title: Home Lab Power Warning
      message: Home lab plug has been over 250W for 10 minutes.
mode: single
```

```yaml
alias: Synology storage warning
trigger:
  - platform: numeric_state
    entity_id: sensor.goingmerry_volume_1_volume_used
    above: 85
action:
  - service: persistent_notification.create
    data:
      title: Synology storage warning
      message: goingmerry Volume 1 is over 85% used.
mode: single
```

```yaml
alias: Home Assistant update available
trigger:
  - platform: state
    entity_id:
      - update.home_assistant_core_update
      - update.home_assistant_operating_system_update
      - update.home_assistant_supervisor_update
      - update_zigbee2mqtt_update
    to: "on"
action:
  - service: persistent_notification.create
    data:
      title: Update available
      message: A Home Assistant or add-on update is available.
mode: single
```

Main issue: your list shows **many sensors**, but not the exact motion/temp entities. For best results, export this:

```text
Settings → Devices & services → Entities → Download CSV
```

Then send me the entity list and I can make the YAML exact.

**You:** Entity
Device
Area
Integration
Status
AirCast
Update
AirCast
Home Assistant Supervisor
—
Backup
Automatic backup
Backup
Backup
—
Last attempted automatic backup
Backup
Backup
—
Last successful automatic backup
Backup
Backup
—
Manager state
Backup
Backup
—
Next scheduled automatic backup
Backup
Backup
—
Bathroom
Bathroom
Bathroom
Bathroom
Apple TV
—
Bathroom
Bathroom
Bathroom
Apple TV
—
Bedroom
Bedroom
Bedroom
Bedroom
Apple TV
—
Bedroom
Bedroom
Bedroom
Apple TV
—
Bedroom near window
Bedroom near window
Bedroom near window
Bedroom
TP-Link Smart Home
—
Cloud connection
Bedroom near window
Bedroom
TP-Link Smart Home
—
Current consumption
Bedroom near window
Bedroom
TP-Link Smart Home
—
Light preset
Bedroom near window
Bedroom
TP-Link Smart Home
—
This month's consumption
Bedroom near window
Bedroom
TP-Link Smart Home
—
Today's consumption
Bedroom near window
Bedroom
TP-Link Smart Home
—
Total consumption
Bedroom near window
Bedroom
TP-Link Smart Home
—
Bedroom TV (Bedroom)
Bedroom TV
Bedroom TV
Bedroom
Android TV Remote
—
Bedroom TV
Bedroom TV
Bedroom
Android TV Remote
—
Bedroom TV
Bedroom TV
Bedroom
Google Cast
—
BedroomDoor
BedroomDoor
BedroomDoor
Bedroom
TP-Link Smart Home
—
Cloud connection
BedroomDoor
Bedroom
TP-Link Smart Home
—
Current consumption
BedroomDoor
Bedroom
TP-Link Smart Home
—
Light preset
BedroomDoor
Bedroom
TP-Link Smart Home
—
This month's consumption
BedroomDoor
Bedroom
TP-Link Smart Home
—
Today's consumption
BedroomDoor
Bedroom
TP-Link Smart Home
—
Total consumption
BedroomDoor
Bedroom
TP-Link Smart Home
—
BedRoomFarsideLight
Cloud connection
BedRoomFarsideLight
Bedroom
TP-Link Smart Home
—
Current consumption
BedRoomFarsideLight
Bedroom
TP-Link Smart Home
—
Light preset
BedRoomFarsideLight
Bedroom
TP-Link Smart Home
—
Not bedroom
BedRoomFarsideLight
Bedroom
TP-Link Smart Home
—

**ChatGPT:** Good — this confirms your bedroom lights are probably:

```yaml
light.bedroom_near_window
light.bedroomdoor
light.bedroomfarsidelight
```

Use this cleaned bedroom automation:

```yaml
alias: Bedroom night motion lights
trigger:
  - platform: state
    entity_id: binary_sensor.YOUR_BEDROOM_MOTION_SENSOR
    to: "on"
condition:
  - condition: sun
    after: sunset
    before: sunrise
action:
  - service: light.turn_on
    target:
      entity_id:
        - light.bedroom_near_window
        - light.bedroomdoor
        - light.bedroomfarsidelight
    data:
      brightness_pct: 25
mode: restart
```

```yaml
alias: Bedroom lights off after no motion
trigger:
  - platform: state
    entity_id: binary_sensor.YOUR_BEDROOM_MOTION_SENSOR
    to: "off"
    for:
      minutes: 10
action:
  - service: light.turn_off
    target:
      entity_id:
        - light.bedroom_near_window
        - light.bedroomdoor
        - light.bedroomfarsidelight
mode: restart
```

Important: **“Not bedroom” is probably the actual light entity for `BedRoomFarsideLight`**, just renamed badly in Home Assistant. Open that entity and check its Entity ID. It may be something like:

```yaml
light.not_bedroom
```

If so, replace:

```yaml
light.bedroomfarsidelight
```

with:

```yaml
light.not_bedroom
```

**You:** alias: Bedroom night motion lights
trigger:
  - platform: state
    entity_id: binary_sensor.YOUR_BEDROOM_MOTION_SENSOR
    to: "on"
condition:
  - condition: sun
    after: sunset
    before: sunrise
action:
  - service: light.turn_on
    target:
      entity_id:
        - light.bedroom_near_window
        - light.bedroomdoor
        - light.bedroomfarsidelight
    data:
      brightness_pct: 25
mode: restart


Do not turn bedroom light on, turn eveyrthing else on to 1 percent, then have it all turn off when i got back to bed.

**ChatGPT:** That's actually a better nighttime automation.

The logic would be:

- Motion detected in bedroom at night
- Turn on **everything except your main bedroom light**
- Set brightness to **1%**
- When motion stops for a few minutes, turn everything back off

Example:

```yaml
alias: Bedroom Night Path Lighting
trigger:
  - platform: state
    entity_id: binary_sensor.YOUR_BEDROOM_MOTION_SENSOR
    to: "on"

condition:
  - condition: sun
    after: sunset
    before: sunrise

action:
  - service: light.turn_on
    target:
      entity_id:
        - light.bedroomdoor
        - light.bedroomfarsidelight
    data:
      brightness_pct: 1

mode: restart
```

Then:

```yaml
alias: Bedroom Night Path Lighting Off
trigger:
  - platform: state
    entity_id: binary_sensor.YOUR_BEDROOM_MOTION_SENSOR
    to: "off"
    for:
      minutes: 2

action:
  - service: light.turn_off
    target:
      entity_id:
        - light.bedroomdoor
        - light.bedroomfarsidelight

mode: restart
```

I'd actually make it even smarter:

- Between 11 PM and 6 AM
- Motion detected
- Only turn on `BedroomDoor`
- Brightness 1%
- Turn off after 60 seconds of no motion

That gives you a bathroom/night-walk light without lighting up the whole room or waking you up. Since you only have one bedroom motion sensor right now, that's probably the most useful automation in your apartment.

**You:** Have it run after I go to bed not at sunset

**ChatGPT:** Even better. Instead of sunset, create a **"Bedtime Mode"** helper.

### Step 1 - Create Helper
Settings → Devices & Services → Helpers → Create Helper

Create:

```text
Input Boolean
Name: Bedtime Mode
```

This creates:

```yaml
input_boolean.bedtime_mode
```

### Step 2 - Turn Bedtime Mode On

You can:

- Put a button on your dashboard
- Have Siri/HomeKit toggle it
- Have it automatically turn on at 11 PM
- Have it turn on when your bedroom TV turns off

### Step 3 - Motion Automation

```yaml
alias: Bedroom Night Path Lighting
trigger:
  - platform: state
    entity_id: binary_sensor.YOUR_BEDROOM_MOTION_SENSOR
    to: "on"

condition:
  - condition: state
    entity_id: input_boolean.bedtime_mode
    state: "on"

action:
  - service: light.turn_on
    target:
      entity_id:
        - light.bedroomdoor
        - light.bedroomfarsidelight
    data:
      brightness_pct: 1

mode: restart
```

### Step 4 - Turn Lights Back Off

```yaml
alias: Bedroom Night Path Lighting Off
trigger:
  - platform: state
    entity_id: binary_sensor.YOUR_BEDROOM_MOTION_SENSOR
    to: "off"
    for:
      minutes: 2

condition:
  - condition: state
    entity_id: input_boolean.bedtime_mode
    state: "on"

action:
  - service: light.turn_off
    target:
      entity_id:
        - light.bedroomdoor
        - light.bedroomfarsidelight

mode: restart
```

### Step 5 - Automatically Exit Bedtime Mode

At 7 AM:

```yaml
alias: Disable Bedtime Mode Morning
trigger:
  - platform: time
    at: "07:00:00"

action:
  - service: input_boolean.turn_off
    target:
      entity_id: input_boolean.bedtime_mode
```

Since you have Apple TVs, a future upgrade would be:

- Apple TV in bedroom turns off
- Bedtime Mode turns on automatically
- Motion sensor becomes a bathroom/night-light trigger
- First motion after 6 AM turns Bedtime Mode off

That makes the apartment adapt to when you actually go to sleep instead of using fixed times.

**You:** THe lights in bedroom should stay off for partner all other lights in house should turn on to 1 percent

**ChatGPT:** That's a great use case.

The bedroom motion sensor becomes a **"night trip detector."**

When you're in bed:

- Bedroom lights stay OFF
- Partner isn't disturbed
- Motion in bedroom means someone got up
- Hallway/living room/kitchen lights come on at 1%
- Everything turns back off after you're back in bed

Example:

```yaml
alias: Night Walk Lighting
trigger:
  - platform: state
    entity_id: binary_sensor.YOUR_BEDROOM_MOTION_SENSOR
    to: "on"

condition:
  - condition: state
    entity_id: input_boolean.bedtime_mode
    state: "on"

action:
  - service: light.turn_on
    target:
      entity_id:
        - light.e26livingroomlightbig
        - light.e26livingroomsmall
        - light.kitchen_light
    data:
      brightness_pct: 1

mode: restart
```

Then turn them off when you're back in bed:

```yaml
alias: Night Walk Lighting Off
trigger:
  - platform: state
    entity_id: binary_sensor.YOUR_BEDROOM_MOTION_SENSOR
    to: "off"
    for:
      minutes: 2

condition:
  - condition: state
    entity_id: input_boolean.bedtime_mode
    state: "on"

action:
  - service: light.turn_off
    target:
      entity_id:
        - light.e26livingroomlightbig
        - light.e26livingroomsmall
        - light.kitchen_light

mode: restart
```

A better version, once you add a motion sensor in the hallway or bathroom, is:

1. Bedroom motion → turns path lights on at 1%.
2. Hallway/bathroom motion keeps them on.
3. No motion anywhere for 2 minutes → lights off.

That way the lights don't turn off while you're still in the bathroom grabbing water or brushing your teeth. For your current setup, I'd recommend adding one Zigbee motion sensor in the bathroom next; it'll enable much smarter nighttime automations.
