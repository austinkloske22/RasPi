# Compact Plant Station Design

Complete guide for building a small, self-contained plant monitoring station that fits in ~1 square foot.

## Design Goals

- **Compact:** Entire setup under 12" x 12" footprint
- **Cost-effective:** $54-82 per station
- **Safe:** Water-resistant electronics placement
- **Expandable:** Easy to replicate for Phase 3
- **Indoor-friendly:** Clean appearance, minimal wires

---

## Compact Station Footprint

### Physical Dimensions

```
Top View (approximately to scale):

┌─────────────────────────────────┐
│  12" x 12" Maximum Area         │
│                                 │
│  ┌─────────────┐                │
│  │  Reservoir  │                │
│  │    3L       │  ┌──────┐      │
│  │   6"x8"     │  │ Pi + │      │
│  │             │  │Relay │      │
│  │    💧      │  │ Box  │      │
│  └─────────────┘  │4"x3" │      │
│                   └──────┘      │
│                                 │
│  [Plant Pot] ───tube───►  💧   │
│    6-8" dia                     │
└─────────────────────────────────┘

Components fit in ~70 sq inches (0.5 sq ft)
With plant: ~100 sq inches (0.7 sq ft)
```

### Component Sizes

| Component | Dimensions | Weight | Notes |
|-----------|------------|--------|-------|
| Pi Zero 2 W | 65mm x 30mm | 12g | Tiny! |
| 1-ch Relay | 35mm x 20mm | 15g | Compact option |
| 4-ch Relay | 75mm x 55mm | 40g | Expandable option |
| Mini pump | 40mm x 25mm | 30g | Fits in reservoir |
| Moisture sensor | 100mm x 20mm | 8g | Inserted in soil |
| 2L Food container | 150mm x 150mm x 150mm | - | Compact reservoir |
| 3L Cereal dispenser | 150mm x 200mm x 300mm | - | Narrow profile |

---

## Three Design Options

### Option 1: Ultra Compact ($58)

**Best for:** Tight spaces, single shelf, minimalist

**Layout:**
```
┌────────────────┐
│   Mason Jar    │  ← 1L reservoir (4"x7")
│      1L        │
│   [Pi+Relay]   │  ← Mounted on jar lid
│       ↓        │
│   ════tube════ │  ← Short tube to pot
│       ↓        │
│   [Plant Pot]  │
└────────────────┘
Footprint: 6" x 6" (0.25 sq ft)
```

**Pros:**
- Smallest footprint
- Electronics elevated (safe from splashes)
- Mason jar reservoir is stable

**Cons:**
- Only 1L capacity (refill every 3-4 days)
- Limited expansion space
- Harder to access Pi

---

### Option 2: Side-by-Side ($77)

**Best for:** Shelf placement, easy access, most popular

**Layout:**
```
┌──────────────────────────────┐
│                              │
│  ┌──────────┐  ┌─────────┐  │
│  │ Reservoir│  │ Pi Box  │  │
│  │   2-3L   │  │         │  │
│  │   (6"x8")│  │ [Pi]    │  │
│  │          │  │ [Relay] │  │
│  │  💧Pump │  │         │  │
│  └──────────┘  └─────────┘  │
│       │             │        │
│       └──tube───────┘        │
│              ↓               │
│        [Plant Pot]           │
│                              │
└──────────────────────────────┘
Footprint: 10" x 10" (0.7 sq ft)
```

**Pros:**
- Easy reservoir refills
- Electronics fully accessible
- Clean cable management
- Room for 3L reservoir

**Cons:**
- Larger footprint
- Needs small project box for Pi

---

### Option 3: Stacked/Vertical ($82)

**Best for:** Very tight spaces, corner placement

**Layout:**
```
Side View:

    ┌───────────┐
    │  Pi Box   │  ← Top level (elevated, safe)
    │  [Pi]     │
    │  [Relay]  │
    └─────┬─────┘
          │
    ┌─────┴─────┐
    │ Reservoir │  ← Middle level
    │    3L     │
    │  💧Pump  │
    └─────┬─────┘
          │ tube
          ↓
    ┌───────────┐
    │Plant Pot  │  ← Bottom level
    └───────────┘

Footprint: 6" x 8" (0.3 sq ft)
Height: 18-24"
```

**Pros:**
- Minimal floor space
- Electronics highest (safest from water)
- Gravity assists water flow

**Cons:**
- Taller profile
- Harder to refill reservoir
- Needs shelf or stand

---

## Compact Electronics Enclosure

### DIY Compact Box (Free)

**Materials:**
- Cardboard project box or food container
- Hot glue or tape
- Electrical tape

**Layout:**
```
┌────────────────────────────┐
│   Small Project Box        │
│   (4" x 3" x 2")          │
│                            │
│   [Pi Zero 2 W]            │  ← Bottom layer
│                            │
│   [4ch Relay] ──wires──►   │  ← Top layer
│                       out  │
│                            │
│   Power in ──USB──►        │
└────────────────────────────┘

Side holes for:
- Power cable
- Sensor wires
- Pump control
```

**Assembly:**
1. Cut holes for wires
2. Mount Pi with standoffs or foam tape
3. Place relay on top layer
4. Seal holes with hot glue
5. Label wires!

---

### Commercial Project Box ($8)

**Recommended:** [Zulkit Project Box](https://www.amazon.com/s?k=small+project+enclosure+box+100x60x25mm)

**Size:** 100mm x 60mm x 25mm (perfect for Pi Zero + Relay)

**Features:**
- Waterproof seal
- Mounting holes
- Cable entry points
- Professional look

**Wiring Plan:**
```
 Top View Inside Box:

 ┌─────────────────────────────┐
 │  ○     Power In (USB)       │
 │                             │
 │  [Pi Zero 2 W]              │
 │   connected to:             │
 │                             │
 │  [1-ch Relay Module]        │
 │   └── pump control wire     │
 │                             │
 │  ○  Sensor Wires (3)        │
 │  ○  Pump Wires (2)          │
 └─────────────────────────────┘
```

---

## Wiring for Compact Design

### Minimize Wire Clutter

**Use these techniques:**

1. **Twist sensor wires together**
   ```
   VCC ────┐
   GND ────┼── Twisted together
   SIG ────┘
   ```

2. **Use short jumper wires**
   - Male-to-Female: Pi → Relay
   - Female-to-Female: Relay → Sensors
   - Keep under 6" when possible

3. **Cable management**
   - Zip ties or velcro strips
   - Adhesive cable clips
   - Label with masking tape

### Compact Wiring Diagram

```
Raspberry Pi Zero 2 W
┌──────────────────┐
│ 1  2  3  4  5  6 │  ← Top 6 pins only!
│ ○  ○  ○  ○  ○  ○ │
└┬─┬──┬──┬──┬──┬───┘
 │ │  │  │  │  │
 │ │  │  │  │  └──────► GND → Sensor GND
 │ │  │  │  └─────────► 5V  → Relay VCC
 │ │  │  └────────────► 5V  → Sensor VCC
 │ │  └───────────────► NC (not connected)
 │ └──────────────────► 5V (optional 2nd device)
 └────────────────────► 3.3V (optional)

Additional Pins:
Pin 11 (GPIO17) ──► Sensor Signal
Pin 13 (GPIO27) ──► Relay IN1

All wiring within 4-6" total length!
```

---

## Assembly Instructions

### Step 1: Prepare Electronics (30 min)

1. **Solder headers to Pi Zero** (if not pre-soldered)
   - 40-pin GPIO header
   - Or use hammer headers (no solder!)

2. **Test components individually**
   ```bash
   # On Pi (after OS install):
   python3 -c "import RPi.GPIO as GPIO; print('GPIO works!')"
   ```

3. **Label all wires with tape**
   - "Sensor VCC", "Sensor GND", "Sensor SIG"
   - "Pump +", "Pump -"
   - "Relay IN1"

### Step 2: Mount in Enclosure (20 min)

1. **Pi placement:**
   - Bottom of box, centered
   - Use foam tape or standoffs
   - Leave room for heat dissipation

2. **Relay placement:**
   - Above or beside Pi
   - Ensure terminals accessible
   - Secure with foam tape

3. **Route wires:**
   - Drill/cut holes for external wires
   - Keep power separate from signal
   - Use cable glands if waterproofing

### Step 3: Reservoir Setup (15 min)

1. **Prepare container:**
   - Clean thoroughly
   - Mark minimum fill line (500ml)
   - Mark maximum fill line

2. **Install pump:**
   - Submerge fully
   - Secure with suction cup or weight
   - Route power wire through lid/side

3. **Attach tubing:**
   - Cut 12-18" length
   - Push firmly onto pump outlet
   - Test for leaks (run pump in water)

### Step 4: Final Assembly (15 min)

1. **Position components:**
   - Place reservoir on mat/tray
   - Position electronics box beside/above
   - Ensure power outlet accessible

2. **Connect all wires:**
   - Follow wiring diagram
   - Double-check polarity!
   - Secure with zip ties

3. **Route tubing to plant:**
   - Run along shelf edge
   - Use adhesive clips
   - Insert stake into soil (2-3" deep)

---

## Compact Station Checklist

**Before First Power-On:**

- [ ] All wiring double-checked against diagram
- [ ] Pump submerged in water
- [ ] Sensor inserted in soil (test pot first!)
- [ ] Electronics elevated above water level
- [ ] All connections secure (no loose wires)
- [ ] Power supply rated 5V 2.5A minimum
- [ ] SD card with OS installed (see deployment guide)

**Power-On Test Sequence:**

1. [ ] Pi boots (green LED blinks)
2. [ ] SSH connection works
3. [ ] Sensor reads data (`python3 moisture_sensor.py`)
4. [ ] Pump activates on command (`python3 pump_control.py`)
5. [ ] No water leaks for 5 minutes
6. [ ] Plant monitor runs successfully

---

## Space-Saving Tips

### For Multiple Stations:

1. **Vertical Shelving**
   ```
   Shelf 1: Station A (8" clearance)
   Shelf 2: Station B (8" clearance)
   Shelf 3: Station C (8" clearance)

   Total: 2 sq ft for 3 stations!
   ```

2. **Shared Power Strip**
   - One 6-outlet strip for all 3 stations
   - Mount behind shelf
   - Clean cable management

3. **Stacked Reservoirs**
   - Use rectangular containers
   - Stack when not in use
   - Label each reservoir

---

## Troubleshooting Compact Builds

### Common Issues:

**1. Overheating**
- **Symptom:** Pi shuts down randomly
- **Solution:** Add ventilation holes to box
- **Prevention:** Don't seal box completely

**2. Water Damage**
- **Symptom:** Pi won't boot after spill
- **Solution:** Dry completely, check for corrosion
- **Prevention:** Elevate electronics, use waterproof box

**3. Tangled Wires**
- **Symptom:** Hard to troubleshoot, looks messy
- **Solution:** Unplug everything, re-route neatly
- **Prevention:** Label and zip-tie from the start

**4. Pump Not Priming**
- **Symptom:** Pump runs but no water flows
- **Solution:** Submerge pump completely, remove air bubbles
- **Prevention:** Keep minimum water level marked

---

## Photos/Diagrams Needed

**TODO:** Add photos when building:
- [ ] Compact electronics box (inside view)
- [ ] Wire routing close-up
- [ ] Reservoir with pump installed
- [ ] Complete station (all options)
- [ ] 3-station shelf setup

---

## Next Steps

1. **Order components:** See [Shopping List](./shopping-list.md)
2. **Prepare Raspberry Pi:** See [Pi Setup Guide](../../docs/getting-started/raspberry-pi-setup.md)
3. **Deploy code:** See [Deployment Guide](../../docs/deployment-guide.md)
4. **Test Phase 1:** See [Phase 1 Setup](../docs/phase1-setup.md)

---

## References

- GPIO Pinout: https://pinout.xyz
- Raspberry Pi Zero Dimensions: https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/
- Relay Wiring Guide: [Phase 1 Setup](../docs/phase1-setup.md)
