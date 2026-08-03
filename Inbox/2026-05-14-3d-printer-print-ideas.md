---
date: 2026-05-14
source: chatgpt
title: "3D Printer Print Ideas"
category: "Design & Creative"
tags: [chatgpt-import]
status: pending-review
sensitive: false
---

**You:** help me make some prints for my 3d printer

**ChatGPT:** You’ve got a few solid directions depending on what kind of prints you want to make with your brand["brand","Prusa","3D printing company"] Mini. Since you already started getting prints working, I’d focus on prints that are:

- useful for your homelab / setup
- easy enough to tune your printer
- visually impressive
- good practice for calibration

Here are some high-value ideas:

---

# Homelab / Tech Prints

These fit your current setup really well.

## Raspberry Pi / NUC Mounts
Print:
- Raspberry Pi 5 cases
- wall mounts
- stackable mini-server racks
- Intel NUC vertical stands

Search terms on:
- urlPrintableshttps://www.printables.com
- urlThingiversehttps://www.thingiverse.com

Example searches:
- “NUC rack mount”
- “Raspberry Pi 5 case”
- “homelab cable management”

---

## Cable Management
Very practical and easy to print.

Ideas:
- desk cable clips
- under-desk cable trays
- ethernet combs
- label holders
- headphone hooks

These are perfect first “functional prints.”

---

## Home Assistant / Smart Home
For your smart home setup:

- Zigbee dongle holders
- sensor mounts
- smart button wall plates
- camera mounts for brand["brand","Ubiquiti","Networking company"] G3 Instant
- Google speaker stands

---

# Cool Display / Decor Prints

## Roman Busts
You were already exploring this.

You could print:
- your own bust
- Greek statues
- MMA-themed busts
- UFC-style trophy display

Matte white PLA works GREAT for statues.

---

## Topographic Maps
These look amazing.

Ideas:
- New Hampshire mountains
- Boston skyline
- favorite hiking areas

---

## LED Lamp Prints
You can print:
- lithophane lamps
- geometric lamps
- cyberpunk desk lighting

These make your setup look much more polished.

---

# Useful Beginner Calibration Prints

These help tune your printer while making useful objects.

## Print These First
- Benchy
- calibration cube
- tolerance test
- filament swatch holder

Especially because you were dealing with the red PLA oozing issue.

---

# Filament Recommendations

For your current stage:

## Best Overall
### PLA+
Easy and forgiving.

Good brands:
- brand["brand","Polymaker","3D printing filament company"]
- brand["brand","Overture","3D printing filament company"]
- brand["brand","Prusament","3D printing filament company"]

---

## Best Colors
- Matte white → statues
- Matte black → tech accessories
- Gray → homelab parts
- Orange → tools
- Galaxy black → decorative prints

---

# Sites You Should Use

## Best Overall
- urlPrintableshttps://www.printables.com
- urlMakerWorldhttps://makerworld.com

## More Massive Libraries
- urlThingiversehttps://www.thingiverse.com
- urlThangshttps://thangs.com

---

# My Recommendation For Your Next 5 Prints

1. Benchy
2. Cable organizer
3. NUC stand
4. Roman bust
5. LED desk lamp

That progression will:
- calibrate your printer
- improve reliability
- give useful results
- make your setup look better

If you want, I can also help you:
- find actual STL files
- make custom prints
- design homelab accessories
- generate wall mount ideas
- make MMA-themed desk items
- create printable organizers for your network gear
- make a custom rack system for your NUCs and Pi cluster

**You:** For now I want coasters

**ChatGPT:** Coasters are a perfect early project. They print fast, help tune first-layer quality, and are actually useful.

Here are the best coaster directions for your setup/interests:

---

# Best Types of Coasters to Print

## Minimal Modern Coasters
Easy prints that look clean in matte PLA.

Good colors:
- matte black
- slate gray
- white marble PLA

Search:
- “minimal hex coaster”
- “modern coaster set”

---

## Topographic Coasters
These look REALLY good.

Ideas:
- New Hampshire mountains
- Boston skyline elevation
- lake contours

Great conversation pieces.

---

## MMA / UFC Style
Since you run entity["organization","Ultimate Fighting Championship","MMA promotion"] content:

Ideas:
- octagon-shaped coasters
- glove silhouette
- “MMA MAC SHOW” logo coaster
- fight-night themed sets

---

## Homelab / Tech Coasters
Honestly perfect for your desk.

Ideas:
- motherboard trace designs
- ethernet-symbol coasters
- Linux logo
- Proxmox-inspired cluster patterns
- pixel-art terminal aesthetic

---

# Best Practical Design Features

Look for coasters with:
- slight lip around edge
- textured bottom
- 3–5 mm thickness
- rounded corners
- recessed design instead of raised

Raised designs can trap condensation.

---

# Recommended Print Settings

For your brand["brand","Prusa","3D printing company"] Mini:

## Easy Reliable Settings
- 0.20 layer height
- 15–20% infill
- 3 perimeters
- PLA+
- textured PEI sheet if you have one

---

# Important Tip

For coasters:
- use more top layers (5–6)
- slower first layer
- enable monotonic top infill if available

This makes the top surface MUCH cleaner.

---

# Filament Recommendation

Your red PLA that’s oozing may string on coaster details.

For clean coasters:
- matte PLA
- PLA+
- dry filament if possible

Matte PLA especially hides imperfections well.

---

# Best Beginner Strategy

Start with:
1. Simple round coaster
2. Hex coaster
3. Embossed logo coaster
4. Multi-color layered coaster later

That progression helps you dial in:
- first layer
- seam quality
- top surface finish

---

# Best Sites for Coasters

## Best Quality
- urlPrintableshttps://www.printables.com

## More Variety
- urlMakerWorldhttps://makerworld.com
- urlThingiversehttps://www.thingiverse.com

Search:
- “coaster set”
- “hex coaster”
- “minimal coaster”
- “topographic coaster”

---

I can also help you make:
- a custom MMA Mac Show coaster
- Boston sports coasters
- a homelab/server-rack themed set
- topographic NH mountain coasters
- custom text/logo coasters for your setup

**You:** No i want you to make the files

**ChatGPT:** I made you a full customizable coaster pack with multiple ready-to-print OpenSCAD coaster designs:

- Minimal modern coaster
- Hex homelab coaster
- MMA octagon coaster
- Topographic-style coaster
- Fully customizable text coaster

You can paste the code into urlOpenSCADhttps://openscad.org and export directly to STL for your brand["brand","Prusa","3D printing company"] Mini.

**You:** What makes that thing hexagon like.

**ChatGPT:** The “hex” look comes from this part of the code:

```scad
$fn=6;
```

and this:

```scad
module hexagon(size, height){
    cylinder(h=height, r=size);
}
```

In OpenSCAD, a cylinder normally becomes round because it uses many sides.

But:

```scad
$fn=6
```

forces it to use only 6 sides.

So the “cylinder” becomes a hexagon instead of a circle.

Then this section:

```scad
for(x=[-30:15:30])
    for(y=[-30:15:30])
```

repeats lots of tiny hexagons in a grid pattern to create the honeycomb/tech appearance.

The coaster itself is still circular:

```scad
cylinder(h=4, d=95, $fn=100);
```

but the pattern cut into it is made of repeating 6-sided shapes.

That’s what creates the homelab / futuristic honeycomb look.
