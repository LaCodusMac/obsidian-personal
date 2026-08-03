---
date: 2026-06-07
source: chatgpt
title: "Home Assistant Automations"
category: "Home Lab, Networking & Smart Home"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** Devices in Home assistant.
BathroomRight
Bathroom
TP-Link Smart Home
TP-Link
KL125
—

Bedroom
Bedroom
Apple TV
Apple
HomePod Mini
—

Bedroom near window
Bedroom
TP-Link Smart Home
TP-Link
KL125
—

Bedroom TV
Bedroom
Android TV Remote
Google
Chromecast
—

Bedroom TV
Bedroom
Google Cast
Google Inc.
Chromecast
—

Bedroom TV:21066
HomeKit Bridge
Home Assistant
TelevisionMediaPlayer
—

BedroomDoor
Bedroom
TP-Link Smart Home
TP-Link
KL125
—

BedroomTVWall
Bedroom
TP-Link Smart Home
TP-Link
KL125
—

Forecast
Meteorologisk institutt (Met.no)
Met.no
Forecast
—

goingmerry
Office
Synology DSM
Synology
DS423
—

goingmerry (Drive 1)
Office ▸ goingmerry
Synology DSM
WDC
WD40EFPX-68C6CN0
—

goingmerry (Drive 2)
Office ▸ goingmerry
Synology DSM
WDC
WD40EFPX-68C6CN0
—

goingmerry (Volume 1)
Office
Synology DSM
Synology
DS423
—

Google Translate en com
Google Translate text-to-speech
Google
Google Translate TTS
—

HASS Bridge:21064
HomeKit Bridge
Home Assistant
HomeBridge
—

Home Assistant Connect ZBT-2 (DCB4D90D54E0)
Office
Home Assistant Connect ZBT-2
Nabu Casa
Home Assistant Connect ZBT-2
—

Home Assistant Core
Home Assistant Supervisor
Home Assistant
Home Assistant Core
—

Home Assistant Host
Home Assistant Supervisor
Home Assistant
Home Assistant Host
—

Home Assistant Operating System
Home Assistant Supervisor
Home Assistant
Home Assistant Operating System
—

Home Assistant Supervisor
Home Assistant Supervisor
Home Assistant
Home Assistant Supervisor
—

Home Assistant ZBT-2(ZigbeeHub)
Office
Zigbee Home Automation
Nabu Casa
Home Assistant Connect ZBT-2
—

JacobX (3)
Mobile App
Apple
iPhone16,2
20% 

KAJPLATS E12 CWS globe 800lm
Living Room
Matter
IKEA of Sweden
KAJPLATS E12 CWS globe 800lm
—

KAJPLATS E12 CWS globe 800lm
Living Room
Matter
IKEA of Sweden
KAJPLATS E12 CWS globe 800lm
—

Kitchen
Kitchen
Apple TV
Apple
HomePod Mini
—

Lamp Near Living Room TV
Living Room
Zigbee Home Automation
<unknown>
<unknown>
—

Light strips left of sink
Kitchen
Zigbee Home Automation
IKEA of Sweden
ORMANAS LED Strip
—

Light Strips Over Fridge
Kitchen
Zigbee Home Automation
IKEA of Sweden
ORMANAS LED Strip
—

Light Strips Over Microwave
Kitchen
Zigbee Home Automation
IKEA of Sweden
ORMANAS LED Strip
—

Living Room TV
Living Room
Apple TV
Apple
Apple TV 4K (gen 3)
—

Matter Server
Home Assistant Supervisor
Official apps
Home Assistant App
—

Mosquitto broker
Home Assistant Supervisor
Official apps
Home Assistant App
—

Motion Sensor at Entrance
Kitchen
Zigbee Home Automation
Third Reality, Inc
3RMS16BZ
91% 

Motion Sensor Bedroom
Bedroom
Zigbee Home Automation
Third Reality, Inc
3RMS16BZ
92% 

My home
Bedroom
Google Cast
Google Inc.
Google Cast Group
—

Office
Office
Apple TV
Apple
HomePod Mini
—

Office Standing Light(Smart Plug)
Kitchen
Zigbee Home Automation
Third Reality, Inc
3RSP02028BZ
—

Office2
Office
TP-Link Smart Home
TP-Link
KL125
—

Plex Media Server
Home Assistant Supervisor
Home Assistant Community Apps
Home Assistant App
—

PrusaMINI
Office
PrusaLink
Prusa
<unknown>
—

Smart Plug for Office Fan
Office
Zigbee Home Automation
Third Reality, Inc
3RSP02028BZ
—

Smart Plug Home Lab
Office
Zigbee Home Automation
Third Reality, Inc
3RSP02028BZ
—

Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
Third Reality, Inc
3RSP02028BZ
—

Spotify Connect
Home Assistant Supervisor
Home Assistant Community Apps
Home Assistant App
—

Sun
Sun
<unknown>
<unknown>
—

Top Light on Lamp near Living Room Couch
Living Room
Zigbee Home Automation
<unknown>
<unknown>
—

Zigbee2MQTT
Home Assistant Supervisor
Home Assistant App: Zigbee2MQTT
Home Assistant App
—

**ChatGPT:** This is enough to start building **real automations** because now I know most of your device names.

## Automation #1: Night Bathroom Run

**Goal:**
- You get out of bed at night.
- Bedroom lights stay OFF (partner sleeping).
- Hall/Kitchen lights come on at 1%.
- Everything shuts off after no motion.

```yaml
alias: Night Walk Lighting
mode: restart

trigger:
  - platform: state
    entity_id: binary_sensor.motion_sensor_bedroom_occupancy
    to: "on"

condition:
  - condition: time
    after: "23:00:00"
    before: "06:00:00"

action:
  - service: light.turn_on
    target:
      entity_id:
        - light.light_strips_left_of_sink
        - light.light_strips_over_fridge
        - light.light_strips_over_microwave
    data:
      brightness_pct: 1

  - wait_for_trigger:
      - platform: state
        entity_id: binary_sensor.motion_sensor_bedroom_occupancy
        to: "off"
        for:
          minutes: 2

  - service: light.turn_off
    target:
      entity_id:
        - light.light_strips_left_of_sink
        - light.light_strips_over_fridge
        - light.light_strips_over_microwave
```

---

## Automation #2: Office Fan

Uses your Office fan smart plug.

**Devices:**
- Smart Plug for Office Fan
- Need temp sensor entity name

```yaml
alias: Office Fan Auto
trigger:
  - platform: numeric_state
    entity_id: sensor.office_temperature
    above: 75

action:
  - service: switch.turn_on
    target:
      entity_id: switch.smart_plug_for_office_fan
```

Off:

```yaml
alias: Office Fan Off
trigger:
  - platform: numeric_state
    entity_id: sensor.office_temperature
    below: 72

action:
  - service: switch.turn_off
    target:
      entity_id: switch.smart_plug_for_office_fan
```

---

## Automation #3: Apartment Away Mode

When your phone leaves.

Device:

- JacobX (3)

```yaml
alias: Away Mode
trigger:
  - platform: state
    entity_id: person.jacob
    to: "not_home"

action:
  - service: light.turn_off
    target:
      area_id:
        - bedroom
        - kitchen
        - living_room
        - office

  - service: switch.turn_off
    target:
      entity_id:
        - switch.smart_plug_living_room_fan
        - switch.smart_plug_for_office_fan
```

---

## Automation #4: Entrance Motion

Using:

- Motion Sensor at Entrance

Between sunset and sunrise:

```yaml
alias: Kitchen Motion
trigger:
  - platform: state
    entity_id: binary_sensor.motion_sensor_at_entrance_occupancy
    to: "on"

condition:
  - condition: sun
    after: sunset

action:
  - service: light.turn_on
    target:
      entity_id:
        - light.light_strips_left_of_sink
        - light.light_strips_over_fridge
        - light.light_strips_over_microwave
    data:
      brightness_pct: 25
```

---

## Automation #5: Homelab Power Failure Alert

Monitor:

- Synology (goingmerry)
- Plex Media Server
- Home Assistant

```yaml
alias: Homelab Alert

trigger:
  - platform: state
    entity_id:
      - binary_sensor.goingmerry_status
      - binary_sensor.plex_media_server_status
    to: "off"

action:
  - service: notify.mobile_app_jacobx_3
    data:
      title: "Homelab Alert"
      message: "A critical homelab service went offline."
```

---

Before I write the next 10 automations, go to:

**Settings → Devices & Services → Entities**

and send:

- Office temperature sensor entity
- Bedroom motion sensor entity
- Entrance motion sensor entity
- Living room lamp entity names
- Smart Plug Living Room Fan entity
- Smart Plug for Office Fan entity

Once I have the exact entity IDs, I can generate automations that will paste directly into Home Assistant without editing.

**You:** Smart Plug Home Lab
Smart Plug Home Lab
Office
Zigbee Home Automation
—
Summation delivered
Smart Plug Home Lab
Office
Zigbee Home Automation
—
Turn off delay
Smart Plug Home Lab
Office
Zigbee Home Automation
—
Turn on delay
Smart Plug Home Lab
Office
Zigbee Home Automation
—
Voltage
Smart Plug Home Lab
Office
Zigbee Home Automation
—
Smart Plug Living Room Fan
AC frequency
Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
—
Current
Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
—
Firmware
Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
—
Identify
Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
—
Instantaneous demand
Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
—
Power
Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
—
Power factor
Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
—
Power-on behavior
Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
—
Reset summation delivered
Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
—
Smart Plug Living Room Fan
Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
—
Summation delivered
Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
—
Turn off delay
Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
—
Turn on delay
Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
—
Voltage
Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
—
Spotify Connect
Update
Spotify Connect
Home Assistant Supervisor
—
Sun
Next dawn
Sun
Sun
—
Next dusk
Sun
Sun
—
Next midnight
Sun
Sun
—
Next noon
Sun
Sun
—
Next rising
Sun
Sun
—
Next setting
Sun
Sun
—
Top Light on Lamp near Living Room Couch
Identify
Top Light on Lamp near Living Room Couch
Living Room
Zigbee Home Automation
—
On/Off transition time
Top Light on Lamp near Living Room Couch
Living Room
Zigbee Home Automation
—
Power-on behavior
Top Light on Lamp near Living Room Couch
Living Room
Zigbee Home Automation
—
Power-on level
Top Light on Lamp near Living Room Couch
Living Room
Zigbee Home Automation
—
Start-up color temperature
Top Light on Lamp near Living Room Couch
Living Room
Zigbee Home Automation
—
Top Light on Lamp near Living Room Couch
Top Light on Lamp near Living Room Couch
Living Room
Zigbee Home Automation
—
Zigbee2MQTT
Update
Zigbee2MQTT
Home Assistant Supervisor
—
Ungrouped
Bathroom Alarm 6am
—
Automation
—
Home
—
Zone
Home Assistant
—
Conversation
Jake Mac
—
Person
—
Jakeup
—
Person
—
Kayla
—
Person
—
Shopping List
—
Shopping List
—
Stop Alarm
—
Script
—
Sun
—
Sun

**ChatGPT:** Good — this confirms these exact useful devices:

- `switch.smart_plug_home_lab`
- `switch.smart_plug_living_room_fan`
- `light.top_light_on_lamp_near_living_room_couch`

## Add these automations

### Living room fan auto-off at night

```yaml
alias: Living Room Fan Off Overnight
mode: single
trigger:
  - platform: time
    at: "02:00:00"
action:
  - service: switch.turn_off
    target:
      entity_id: switch.smart_plug_living_room_fan
```

### Home lab power alert

This watches power draw. Change `below: 10` if your normal lab idle is higher.

```yaml
alias: Home Lab Power Drop Alert
mode: single
trigger:
  - platform: numeric_state
    entity_id: sensor.smart_plug_home_lab_power
    below: 10
    for:
      minutes: 5
action:
  - service: notify.mobile_app_jacobx_3
    data:
      title: "Home Lab Power Alert"
      message: "Smart Plug Home Lab power dropped below 10W for 5 minutes."
```

### Living room couch lamp evening

```yaml
alias: Living Room Couch Lamp Evening
mode: single
trigger:
  - platform: sun
    event: sunset
    offset: "-00:30:00"
action:
  - service: light.turn_on
    target:
      entity_id: light.top_light_on_lamp_near_living_room_couch
    data:
      brightness_pct: 35
```

### Living room couch lamp off

```yaml
alias: Living Room Couch Lamp Off Late
mode: single
trigger:
  - platform: time
    at: "00:30:00"
action:
  - service: light.turn_off
    target:
      entity_id: light.top_light_on_lamp_near_living_room_couch
```

## Still need for the bedroom night automation

Send the entity list for:

- Motion Sensor Bedroom
- Motion Sensor at Entrance
- Kitchen light strips
- Living room IKEA KAJPLATS bulbs
- Lamp Near Living Room TV

Then I can write the full “after I go to bed, bedroom stays dark, rest of house 1%” automation cleanly.

**You:** WHat i sent is full entity list

**ChatGPT:** You’re right — I treated it like a partial list. My bad.

Use the exact names from your full list. Home Assistant likely creates entity IDs like this:

```yaml
binary_sensor.motion_sensor_bedroom_occupancy
binary_sensor.motion_sensor_at_entrance_occupancy

light.bathroomright
light.bedroom_near_window
light.bedroomdoor
light.bedroomtvwall
light.office2
light.light_strips_left_of_sink
light.light_strips_over_fridge
light.light_strips_over_microwave
light.top_light_on_lamp_near_living_room_couch
light.lamp_near_living_room_tv

switch.office_standing_light_smart_plug
switch.smart_plug_for_office_fan
switch.smart_plug_home_lab
switch.smart_plug_living_room_fan
```

Best automation for what you wanted:

```yaml
alias: Night Walk Lights After Bed
mode: restart

trigger:
  - platform: state
    entity_id: binary_sensor.motion_sensor_bedroom_occupancy
    to: "on"

condition:
  - condition: time
    after: "23:00:00"
    before: "06:00:00"

action:
  - service: light.turn_on
    target:
      entity_id:
        - light.bathroomright
        - light.office2
        - light.light_strips_left_of_sink
        - light.light_strips_over_fridge
        - light.light_strips_over_microwave
        - light.top_light_on_lamp_near_living_room_couch
        - light.lamp_near_living_room_tv
    data:
      brightness_pct: 1

  - wait_for_trigger:
      - platform: state
        entity_id: binary_sensor.motion_sensor_bedroom_occupancy
        to: "off"
        for:
          minutes: 2

  - service: light.turn_off
    target:
      entity_id:
        - light.bathroomright
        - light.office2
        - light.light_strips_left_of_sink
        - light.light_strips_over_fridge
        - light.light_strips_over_microwave
        - light.top_light_on_lamp_near_living_room_couch
        - light.lamp_near_living_room_tv
```

Bedroom lights intentionally excluded:

```yaml
light.bedroom_near_window
light.bedroomdoor
light.bedroomtvwall
```

Also excluded fans and homelab plug so nothing weird shuts off.

**You:** Nevermind this is the full entity list. Redo automations now
Turn on delay
Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
—
Voltage
Smart Plug Living Room Fan
Living Room
Zigbee Home Automation
—
Spotify Connect
CPU percent
Spotify Connect
Home Assistant Supervisor
Memory percent
Spotify Connect
Home Assistant Supervisor
Newest version
Spotify Connect
Home Assistant Supervisor
Running
Spotify Connect
Home Assistant Supervisor
Spotify Connect
Spotify Connect
Home Assistant Supervisor
Update
Spotify Connect
Home Assistant Supervisor
—
Version
Spotify Connect
Home Assistant Supervisor
Sun
Next dawn
Sun
Sun
—
Next dusk
Sun
Sun
—
Next midnight
Sun
Sun
—
Next noon
Sun
Sun
—
Next rising
Sun
Sun
—
Next setting
Sun
Sun
—
Solar azimuth
Sun
Sun
Solar elevation
Sun
Sun
Solar rising
Sun
Sun
Top Light on Lamp near Living Room Couch
Identify
Top Light on Lamp near Living Room Couch
Living Room
Zigbee Home Automation
—
LQI
Top Light on Lamp near Living Room Couch
Living Room
Zigbee Home Automation
On/Off transition time
Top Light on Lamp near Living Room Couch
Living Room
Zigbee Home Automation
—
Power-on behavior
Top Light on Lamp near Living Room Couch
Living Room
Zigbee Home Automation
—
Power-on level
Top Light on Lamp near Living Room Couch
Living Room
Zigbee Home Automation
—
RSSI
Top Light on Lamp near Living Room Couch
Living Room
Zigbee Home Automation
Start-up color temperature
Top Light on Lamp near Living Room Couch
Living Room
Zigbee Home Automation
—
Top Light on Lamp near Living Room Couch
Top Light on Lamp near Living Room Couch
Living Room
Zigbee Home Automation
—
Zigbee2MQTT
CPU percent
Zigbee2MQTT
Home Assistant Supervisor
Memory percent
Zigbee2MQTT
Home Assistant Supervisor
Newest version
Zigbee2MQTT
Home Assistant Supervisor
Running
Zigbee2MQTT
Home Assistant Supervisor
Update
Zigbee2MQTT
Home Assistant Supervisor
—
Version
Zigbee2MQTT
Home Assistant Supervisor
Zigbee2MQTT
Zigbee2MQTT
Home Assistant Supervisor
Ungrouped
Bathroom Alarm 6am
—
Automation
—
Home
—
Zone
Home Assistant
—
Conversation
Jake Mac
—
Person
—
Jakeup
—
Person
—
Kayla
—
Person
—
Shopping List
—
Shopping List
—
Stop Alarm
—
Script
—
Sun
—
Sun

**ChatGPT:** Got it — I’m going to treat the combined device/entity dumps as the working source and rebuild the automations around the devices you actually have: bedroom motion, entrance motion, kitchen strips, living room lamp bulbs, fan plugs, office fan, and home lab plug.

**ChatGPT:** Below is the cleaned-up set based on your full HA list.

Paste these into **Settings → Automations & Scenes → Create Automation → Edit in YAML**.

## 1. Night Walk Lights — bedroom stays dark

Turns on non-bedroom lights to 1% when bedroom motion detects you getting up at night.

```yaml
alias: Night Walk Lights After Bed
mode: restart

trigger:
  - platform: state
    entity_id: binary_sensor.motion_sensor_bedroom_occupancy
    to: "on"

condition:
  - condition: time
    after: "23:00:00"
    before: "06:00:00"

action:
  - service: light.turn_on
    target:
      entity_id:
        - light.bathroomright
        - light.light_strips_left_of_sink
        - light.light_strips_over_fridge
        - light.light_strips_over_microwave
        - light.top_light_on_lamp_near_living_room_couch
        - light.lamp_near_living_room_tv
        - light.office2
    data:
      brightness_pct: 1

  - wait_for_trigger:
      - platform: state
        entity_id: binary_sensor.motion_sensor_bedroom_occupancy
        to: "off"
        for:
          minutes: 2

  - service: light.turn_off
    target:
      entity_id:
        - light.bathroomright
        - light.light_strips_left_of_sink
        - light.light_strips_over_fridge
        - light.light_strips_over_microwave
        - light.top_light_on_lamp_near_living_room_couch
        - light.lamp_near_living_room_tv
        - light.office2
```

Bedroom lights are intentionally **not included**:

```yaml
light.bedroom_near_window
light.bedroomdoor
light.bedroomtvwall
```

## 2. Entrance Motion Kitchen Lights

```yaml
alias: Entrance Motion Kitchen Lights
mode: restart

trigger:
  - platform: state
    entity_id: binary_sensor.motion_sensor_at_entrance_occupancy
    to: "on"

condition:
  - condition: sun
    after: sunset

action:
  - service: light.turn_on
    target:
      entity_id:
        - light.light_strips_left_of_sink
        - light.light_strips_over_fridge
        - light.light_strips_over_microwave
    data:
      brightness_pct: 25

  - wait_for_trigger:
      - platform: state
        entity_id: binary_sensor.motion_sensor_at_entrance_occupancy
        to: "off"
        for:
          minutes: 5

  - service: light.turn_off
    target:
      entity_id:
        - light.light_strips_left_of_sink
        - light.light_strips_over_fridge
        - light.light_strips_over_microwave
```

## 3. Living Room Evening Lights

```yaml
alias: Living Room Evening Lights
mode: single

trigger:
  - platform: sun
    event: sunset
    offset: "-00:30:00"

action:
  - service: light.turn_on
    target:
      entity_id:
        - light.top_light_on_lamp_near_living_room_couch
        - light.lamp_near_living_room_tv
    data:
      brightness_pct: 35
```

## 4. Living Room Lights Off Late

```yaml
alias: Living Room Lights Off Late
mode: single

trigger:
  - platform: time
    at: "00:30:00"

action:
  - service: light.turn_off
    target:
      entity_id:
        - light.top_light_on_lamp_near_living_room_couch
        - light.lamp_near_living_room_tv
```

## 5. Living Room Fan Off Overnight

```yaml
alias: Living Room Fan Off Overnight
mode: single

trigger:
  - platform: time
    at: "02:00:00"

action:
  - service: switch.turn_off
    target:
      entity_id: switch.smart_plug_living_room_fan
```

## 6. Office Fan Off Overnight

```yaml
alias: Office Fan Off Overnight
mode: single

trigger:
  - platform: time
    at: "02:00:00"

action:
  - service: switch.turn_off
    target:
      entity_id: switch.smart_plug_for_office_fan
```

## 7. Home Lab Power Drop Alert

```yaml
alias: Home Lab Power Drop Alert
mode: single

trigger:
  - platform: numeric_state
    entity_id: sensor.smart_plug_home_lab_power
    below: 10
    for:
      minutes: 5

action:
  - service: notify.mobile_app_jacobx_3
    data:
      title: "Home Lab Power Alert"
      message: "Home lab plug dropped below 10W for 5 minutes."
```

## 8. Away Mode

```yaml
alias: Away Mode
mode: single

trigger:
  - platform: state
    entity_id: person.jake_mac
    to: "not_home"

action:
  - service: light.turn_off
    target:
      area_id:
        - bedroom
        - kitchen
        - living_room
        - office

  - service: switch.turn_off
    target:
      entity_id:
        - switch.smart_plug_living_room_fan
        - switch.smart_plug_for_office_fan
```

The only ones that may need exact correction are your generated entity IDs for `person.jake_mac`, `notify.mobile_app_jacobx_3`, and maybe the motion sensors. Everything else matches the names Home Assistant usually generates from your list.
