# Plant Watering System - Hardware Shopping List

This guide provides component options at various price points for Phase 1 (single plant) with notes for scaling to Phase 3 (3 plants).

## Phase 1: Single Plant System

### Required Components

#### 1. Raspberry Pi

| Option | Model | Price | Notes |
|--------|-------|-------|-------|
| **Budget** | Raspberry Pi Zero W | $15 | Perfect for sensor nodes, built-in WiFi |
| **Recommended** | Raspberry Pi Zero 2 W | $15 | 5x faster than Zero W, same size |
| **Overkill** | Raspberry Pi 4 (2GB) | $45 | Good if you want to add camera/display later |

**What to buy:** Pi Zero 2 W + microSD card (16GB minimum)

---

#### 2. Soil Moisture Sensor

| Option | Type | Price | Pros | Cons |
|--------|------|-------|------|------|
| **Avoid** | Resistive | $3-5 | Very cheap | Corrodes quickly, inaccurate |
| **Recommended** | Capacitive v1.2 | $8-12 | Corrosion-resistant, accurate | Needs calibration |
| **Premium** | I2C Capacitive | $15-20 | Digital output, easy to use | More expensive |

**Recommended Purchase:**
- Capacitive Soil Moisture Sensor v1.2 (x3 for future expansion)
- Search: "capacitive soil moisture sensor v1.2" on Amazon/AliExpress

---

#### 3. Water Pump System

**Option A: Submersible Pump (Recommended for Reservoirs)**

| Model | Voltage | Flow Rate | Price | Best For |
|-------|---------|-----------|-------|----------|
| Mini submersible pump | 3-6V DC | 80-120 L/h | $5-8 | Small pots, short tubes |
| Aquarium pump | 5V USB | 200 L/h | $10-15 | Medium pots, longer runs |
| Peristaltic pump | 12V DC | Precise | $15-25 | Exact dosing, no backflow |

**Option B: Solenoid Valve** (if using gravity feed)

| Type | Voltage | Price | Notes |
|------|---------|-------|-------|
| 12V DC solenoid | 12V | $8-12 | Requires 12V power, very reliable |
| 5V DC solenoid | 5V | $10-15 | Easier to power from Pi supply |

**Recommendation:** Start with **mini submersible pump (5V)** - easiest for reservoirs

---

#### 4. Pump Control (Relay or MOSFET)

| Option | Type | Channels | Price | Best For |
|--------|------|----------|-------|----------|
| **Simple** | 5V Relay Module | 1-channel | $3-5 | Easy for beginners |
| **Expandable** | 5V Relay Module | 4-channel | $8-10 | Future multi-pump setup |
| **Efficient** | MOSFET Module | 1-channel | $5-7 | Less power draw, silent |

**Recommendation:** **4-channel relay module** - you'll use the extra channels for Phase 3

---

#### 5. Water Reservoir System

**Reservoir Options:**

| Option | Capacity | Price | Pros | Cons |
|--------|----------|-------|------|------|
| Food storage container | 2-5L | $5-10 | Cheap, food-safe | Manual refill |
| Gravity-feed bottle | 1-2L | $8-12 | Simple, self-regulating | Small capacity |
| Small bucket + lid | 5-10L | $10-15 | Large capacity | Takes up space |
| **Recommended:** Drink dispenser | 3-5L | $15-25 | Easy refill, spigot option | More expensive |

**Additional Reservoir Hardware:**
- Silicone tubing (1/4" or 3/8" inner diameter) - $5-10 for 10ft
- Tube connectors/splitters - $5
- Drip irrigation stakes (optional) - $8 for 10-pack

---

#### 6. Water Level Detection (Optional for Phase 1, Required for Phase 2)

| Option | Type | Price | Pros | Cons |
|--------|------|-------|------|------|
| **Simple** | Float switch | $3-5 | Binary (full/empty) | Only 2 states |
| **Better** | Ultrasonic (HC-SR04) | $5-8 | Distance measurement | Needs mounting above water |
| **Advanced** | Capacitive level sensor | $8-12 | Multiple levels | More complex setup |

**Recommendation for Phase 2:** **Float switch** (simple) or **HC-SR04** (more data)

---

#### 7. Power Supply

| Option | Output | Price | Notes |
|--------|--------|-------|-------|
| **Basic** | 5V 2.5A USB | $8-10 | Powers Pi + small pump |
| **Better** | 5V 3A USB-C | $10-12 | More headroom for accessories |
| **Multi-voltage** | 5V/12V adapter | $15-20 | If using 12V pump/solenoid |

**Recommendation:** 5V 3A USB power supply (official Raspberry Pi adapter)

---

#### 8. Optional Components

| Component | Price | Purpose |
|-----------|-------|---------|
| Pushbutton | $2 | Manual pump trigger |
| LED + 220Ω resistor | $2 | Status indicator |
| Waterproof case | $10-15 | Protect electronics |
| Breadboard + jumper wires | $8-12 | Prototyping |
| MicroSD card (16GB) | $8-12 | Operating system |

---

## Phase 1 Complete Kit - Recommended Shopping List

### Budget Build (~$75-90)
- [ ] Raspberry Pi Zero 2 W - $15
- [ ] MicroSD Card 16GB - $8
- [ ] Capacitive soil moisture sensor - $10
- [ ] 5V mini submersible pump - $7
- [ ] 4-channel 5V relay module - $8
- [ ] 5V 3A power supply - $10
- [ ] Silicone tubing (10ft) - $8
- [ ] 3L drink dispenser (reservoir) - $15
- [ ] Jumper wires kit - $6
- [ ] LED, resistor, button kit - $5

**Total: ~$92**

### Quality Build (~$110-130)
- [ ] Raspberry Pi Zero 2 W - $15
- [ ] MicroSD Card 32GB (high speed) - $12
- [ ] I2C capacitive moisture sensor - $18
- [ ] Peristaltic pump 5V - $20
- [ ] 4-channel relay module - $8
- [ ] 5V 3A official power supply - $12
- [ ] Quality silicone tubing + connectors - $12
- [ ] 5L drink dispenser - $20
- [ ] Breadboard + quality wires - $12
- [ ] Waterproof case - $12
- [ ] HC-SR04 ultrasonic sensor - $6

**Total: ~$147**

---

## Phase 3 Expansion (2 Additional Plants)

When you're ready to add 2 more plants:

### Additional Hardware Needed:
- [ ] 2x Raspberry Pi Zero 2 W + SD cards - $46
- [ ] 2x Capacitive soil moisture sensors - $20
- [ ] 2x 5V submersible pumps - $14
- [ ] 2x Relay modules (or use spare channels) - $6
- [ ] 2x Water reservoirs - $30
- [ ] Additional tubing and connectors - $15
- [ ] 2x Power supplies - $20

**Expansion Cost: ~$151**

### Central Controller Option:
- [ ] Raspberry Pi 4 (2-4GB) for central MQTT broker - $45-55
- [ ] Power supply for Pi 4 - $10

---

## Where to Buy

**US Retailers:**
- **Amazon** - Fast shipping, easy returns
- **Adafruit** - Quality components, great documentation
- **SparkFun** - Educational focus, reliable
- **CanaKit** - Raspberry Pi starter kits
- **Micro Center** - In-store pickup (if available)

**Budget Options:**
- **AliExpress** - Cheapest, 2-4 week shipping
- **eBay** - Mixed quality, check reviews

**Reservoir/Tubing:**
- **Home Depot / Lowe's** - Containers, tubing
- **Amazon** - Drink dispensers, drip irrigation kits

---

## Shopping Tips

1. **Buy extras:** Get 2-3 sensors/pumps now (they're cheap, shipping is not)
2. **Combo deals:** Look for "Raspberry Pi Zero starter kits" with SD card + power supply
3. **Quality matters:** Don't cheap out on power supplies (fire hazard) or SD cards (corruption)
4. **Future-proof:** Get the 4-channel relay now even for 1 plant
5. **Reservoir size:** 3-5L per plant should last 1-2 weeks depending on plant size

---

## Next Steps

After purchasing:
1. See [Phase 1 Setup Guide](../docs/phase1-setup.md)
2. Review [Wiring Diagrams](./phase1-wiring.md)
3. Test components individually before assembly
