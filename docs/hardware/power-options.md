# Power Options for Plant Watering System

Choosing between battery power and outlet power depends on your plant locations and power availability.

## Power Consumption Analysis

### Typical Power Draw:

| Component | Power Draw | Notes |
|-----------|------------|-------|
| Raspberry Pi Zero 2 W (idle) | 0.4-0.6W | ~100-120mA @ 5V |
| Raspberry Pi Zero 2 W (active) | 0.7-1W | ~140-200mA @ 5V |
| Moisture sensor | 0.1W | ~20mA @ 5V |
| 5V mini water pump | 2-4W | ~400-800mA @ 5V (only when running) |
| Relay module | 0.35W | ~70mA @ 5V (per channel) |

**Total idle:** ~1W (200mA @ 5V)
**Total when pumping:** ~5-6W (1000-1200mA @ 5V)

**Daily usage estimate:**
- 23.5 hours idle: ~24Wh
- 0.5 hours pumping: ~3Wh
- **Daily total: ~27Wh** (5400mAh @ 5V)

---

## Option 1: Outlet Power (Recommended for Phase 1-2)

### Pros:
- Unlimited runtime
- No battery maintenance
- More reliable
- Simpler setup
- Can run 24/7 web dashboard
- No worry about pump power draw

### Cons:
- Requires nearby outlet
- Less portable
- Cable management needed
- Power outage = system down

### Recommended Setup:

**Standard Configuration:**
```
Wall Outlet → 5V 3A Power Supply → Raspberry Pi → Components
```

**Equipment:**
- Official Raspberry Pi 5V 3A USB-C power supply - $12
- 6ft power cable extension (if needed) - $8
- Surge protector (recommended) - $15

**Best For:**
- Plants near outlets (living room, kitchen, office)
- Permanent installations
- Central controller (always-on)
- Phase 2-3 with web dashboard

---

## Option 2: Battery Power (Good for Remote Locations)

### Pros:
- Place anywhere in home
- No cables to manage
- Portable between plants
- Clean look
- Works during power outages

### Cons:
- Needs recharging (every 1-3 days)
- Battery degradation over time
- More expensive upfront
- Pump draws significant power
- Need UPS or power bank

### Battery Options:

#### A) USB Power Bank (Easiest)

**Recommended:**
- **Anker PowerCore 20000mAh** - $45
  - Runtime: ~15-18 hours with pumping
  - Recharge: Every 1-2 days
  - Pass-through charging: Yes (charge while using)

- **RAVPower 26800mAh** - $50
  - Runtime: ~20-24 hours
  - Recharge: Every 2 days
  - Output: 2.4A per port

**Setup:**
```
Power Bank (USB) → USB to Micro-USB cable → Raspberry Pi Zero
```

**Pros:** Simple, portable, safe
**Cons:** Frequent recharging needed

---

#### B) Lithium Battery + UPS HAT (Better)

**PiSugar 2 Plus (Recommended)**
- Capacity: 5000mAh
- Runtime: ~9-12 hours
- Features: Auto power on/off, RTC
- Price: $50

**PiJuice HAT**
- Capacity: 12000mAh (with largest battery)
- Runtime: ~18-24 hours
- Features: Solar panel input, software control
- Price: $70-90

**Setup:**
```
Battery HAT → Raspberry Pi GPIO → Components
```

**Pros:**
- Clean integration
- Auto power management
- Can schedule wake/sleep
- RTC for timekeeping without WiFi

**Cons:**
- More expensive
- Limited capacity
- Still needs periodic charging

---

#### C) Large Battery + Solar (Advanced Phase 3+)

**For truly remote/outdoor locations:**

**Components:**
- 12V 20Ah LiFePO4 battery - $80-100
- 12V to 5V buck converter (5A) - $12
- 20W solar panel - $40
- Solar charge controller - $20
- Waterproof enclosure - $25

**Runtime:** 7-10 days between charges (with solar: indefinite)

**Setup:**
```
Solar Panel → Charge Controller → 12V Battery → Buck Converter → 5V Pi
```

**Pros:**
- Near-infinite runtime with sun
- Good for outdoor plants
- Powers multiple sensor nodes

**Cons:**
- Complex setup
- Expensive (~$175-200)
- Requires sun exposure
- Overkill for indoor use

---

## Hybrid Option: Outlet + Battery Backup (Best of Both)

### Setup 1: UPS Power Bank

**CyberPower UPS** (small 600VA) - $60
- Normal: Runs from outlet
- Outage: Switches to battery
- Runtime: 2-4 hours on battery
- Protects multiple devices

**Best for:** Critical plants that can't miss watering

---

### Setup 2: Smart Power Management

**Use outlet power + sleep mode:**

```python
# Pseudocode for power optimization
def power_efficient_mode():
    # Wake up every 15 minutes
    # Read sensor (5 seconds)
    # Water if needed (30 seconds)
    # Sleep/low power mode
    # Battery life: 3-5 days instead of 1
```

**Equipment:**
- Power bank with pass-through charging - $40
- WiFi smart plug (optional auto-scheduling) - $15

---

## Recommendations by Phase

### Phase 1: Single Plant Learning
**Recommended: Outlet Power**
- Simplest to set up
- Focus on learning, not power management
- Likely near your workspace anyway

**Budget:** $12 (power supply)

---

### Phase 2: Automated Single Plant
**Recommended: Outlet Power**
- Web dashboard needs 24/7 uptime
- Frequent watering = battery drain

**Alternative:** Battery with pass-through charging
- Anker PowerCore 20000 - $45
- Keep plugged in normally
- Works during outages

---

### Phase 3: Three Plants
**Recommended: Mixed Approach**

1. **Central Controller (Pi 4):** Outlet power - always on
2. **Sensor Nodes (3x Pi Zero):**
   - **Option A:** Outlet power if near outlets
   - **Option B:** Battery + sleep mode for remote spots
   - **Option C:** Mix - 1-2 on outlet, 1 on battery

**Strategy:**
- Sensor nodes wake every 30 min
- Report to central controller
- Sleep between readings
- Battery life: 2-3 days with sleep mode

---

## Power Comparison Table

| Scenario | Solution | Cost | Runtime | Maintenance |
|----------|----------|------|---------|-------------|
| Plant near outlet | 5V 3A adapter | $12 | Infinite | None |
| Plant 10ft from outlet | Adapter + extension | $20 | Infinite | None |
| Plant in remote corner | 20000mAh power bank | $45 | 15-18h | Recharge daily |
| Multiple remote plants | 3x power banks | $135 | 15-18h | Recharge all daily |
| Outdoor/patio plant | Solar + battery | $175 | Infinite* | Seasonal cleaning |
| Critical plant | UPS backup | $72 | Infinite + 2h backup | None |

*Weather dependent

---

## Recommended Purchase Strategy

### For Phase 1 (Start Simple):
1. **Buy outlet power supply** - $12
2. **Test with single plant near outlet**
3. **Evaluate power needs**

### For Phase 3 (After Testing):
1. **Keep Phase 1 plant on outlet power**
2. **Add 2 more plants:**
   - If near outlets: 2x power supplies ($24)
   - If remote: 2x power banks ($90)
   - If outdoor: Consider solar ($175)

---

## Power-Saving Tips

### Software Optimizations:
```python
# Reduce WiFi power
sudo iwconfig wlan0 power on

# Disable HDMI (saves 25mA)
sudo /usr/bin/tvservice -o

# Disable LEDs
echo 0 | sudo tee /sys/class/leds/led0/brightness

# Use deep sleep between readings
# Wake via RTC or timer
```

**Savings:** 30-40% reduction in idle power

### Hardware Optimizations:
- Use Pi Zero (not Pi 4) for sensor nodes
- Disable unused USB ports
- Turn off pump relay when not in use
- Use momentary pump activation (30s max)

---

## Final Recommendations

### Start Here (Phase 1):
- **5V 3A Official Raspberry Pi Power Supply** - $12
- Test outlet power first, simplest to debug

### Upgrade Later (Phase 3):
- **Plants near outlets:** Stick with outlet power
- **1-2 remote plants:** Add power banks with pass-through charging
- **Outdoor plants:** Consider solar in Phase 4

### Don't Overbuy:
- ❌ Don't buy batteries until you need them
- ❌ Don't buy solar for indoor plants
- ✅ Start simple, add complexity as needed

---

## Next Steps

1. Map your plant locations
2. Note which are near outlets
3. Decide: All outlet vs mixed
4. Update your shopping list accordingly

See [Shopping List](../../projects/plant-watering/hardware/shopping-list.md) for specific product links.
