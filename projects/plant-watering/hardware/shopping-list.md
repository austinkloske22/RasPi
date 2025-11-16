# Plant Watering System - Hardware Shopping List

Detailed component guide with **actual prices** and **shopping links** for compact, cost-effective plant stations.

## Quick Cost Summary

| Configuration | Per Station | 3 Stations | Notes |
|--------------|-------------|------------|-------|
| **Ultra Budget** | $55-65 | $165-195 | Bare minimum, works well |
| **Recommended** | $75-85 | $225-255 | Best value for reliability |
| **Quality Build** | $95-110 | $285-330 | Premium components |

---

## Phase 1: Single Compact Plant Station

**Design Goal:** Self-contained unit under $85 that fits in ~1 sq ft space

### Required Components with Shopping Links

#### 1. Raspberry Pi Brain

| Option | Model | Price | Link | Notes |
|--------|-------|-------|------|-------|
| **Recommended** | Pi Zero 2 W | $15 | [Adafruit](https://www.adafruit.com/product/5291) / [Amazon](https://www.amazon.com/s?k=raspberry+pi+zero+2+w) | 5x faster, same compact size |
| **Budget** | Pi Zero W | $10-15 | [Amazon](https://www.amazon.com/s?k=raspberry+pi+zero+w) | Slower but adequate |
| **Kit Option** | Zero 2 W Starter Kit | $35-40 | [CanaKit](https://www.canakit.com/raspberry-pi-zero-2-w.html) | Includes SD card, power, headers |

**Recommended Purchase:**
- Pi Zero 2 W standalone if you have SD/power
- OR CanaKit starter kit (saves $5-10 vs buying separately)

---

#### 2. Soil Moisture Sensor

| Option | Type | Price | Link | Qty | Notes |
|--------|------|-------|------|-----|-------|
| **Budget** | Capacitive v1.2 | $2.50 ea | [Amazon 5-pack $12](https://www.amazon.com/s?k=capacitive+soil+moisture+sensor+5+pack) | Buy 5 | Get extras now |
| **Recommended** | Capacitive v1.2 | $8 ea | [Amazon Single](https://www.amazon.com/s?k=capacitive+soil+moisture+sensor+v1.2) | Buy 3 | Individual quality |
| **Premium** | STEMMA I2C | $7 ea | [Adafruit #4026](https://www.adafruit.com/product/4026) | Buy 3 | Digital, no calibration |

**Recommended Purchase:**
- 5-pack capacitive sensors ($12 / $2.40 each) - **Best value**
- Keep spares for future expansion

---

#### 3. Water Pump (Compact Size Critical)

| Model | Voltage | Size | Price | Link | Notes |
|-------|---------|------|-------|------|-------|
| **Recommended** | DC Mini Submersible | 5V | 40x25mm | $5-7 | [Amazon 3-pack $15](https://www.amazon.com/s?k=mini+submersible+pump+5v+3+pack) | Tiny, reliable |
| **Budget** | DC Micro Pump | 3-6V | 35x30mm | $4 ea | [Amazon 5-pack $18](https://www.amazon.com/s?k=dc+mini+water+pump+3v) | Very cheap |
| **Quality** | Peristaltic Pump | 5V | 65x50mm | $12-15 | [Amazon](https://www.amazon.com/s?k=peristaltic+pump+5v) | Precise, larger |

**Recommended Purchase:**
- 3-pack mini submersible 5V pumps ($15 / $5 each) - **Best value for 3 stations**

---

#### 4. Relay Module (Compact Board)

| Type | Channels | Size | Price | Link | Notes |
|------|----------|------|-------|------|-------|
| **Budget** | 1-channel | 35x20mm | $2 ea | [Amazon 5-pack $8](https://www.amazon.com/s?k=5v+relay+module+1+channel+5+pack) | One per station |
| **Recommended** | 4-channel | 75x55mm | $7 | [Amazon](https://www.amazon.com/s?k=4+channel+5v+relay+module) | Expandable, better terminals |
| **Compact** | 2-channel | 50x40mm | $5 | [Amazon](https://www.amazon.com/s?k=2+channel+5v+relay+module) | Good middle ground |

**Recommended Purchase:**
- **For 1 station**: 4-channel relay ($7) - future-proof
- **For 3 stations**: 5-pack 1-channel ($8) OR 2x 4-channel ($14) for flexibility

---

#### 5. Compact Water Reservoir

**Key: Must be compact and stable for indoor use**

| Option | Capacity | Size (approx) | Price | Link | Notes |
|--------|----------|---------------|-------|------|-------|
| **Ultra Budget** | Mason jar 1L | 4"x7" | $3 | [Amazon](https://www.amazon.com/s?k=mason+jar+quart) | DIY, very compact |
| **Budget** | Food container 2L | 6"x6"x6" | $6 | [Amazon](https://www.amazon.com/s?k=food+storage+container+2+liter) | Rectangular, stackable |
| **Recommended** | Cereal dispenser 3L | 6"x8"x12" | $12-15 | [Amazon](https://www.amazon.com/s?k=cereal+dispenser+3+liter) | Narrow, easy refill |
| **Premium** | Beverage dispenser 3.5L | 7"x7"x11" | $18-22 | [Amazon](https://www.amazon.com/s?k=glass+beverage+dispenser+1+gallon) | Looks nice, glass |

**Recommended Purchase:**
- **Budget**: Food containers 2L - $6 each x3 = $18
- **Best**: Cereal dispensers 3L - $13 each x3 = $39

---

#### 6. Tubing & Connections

| Item | Size | Length | Price | Link | Notes |
|------|------|--------|-------|------|-------|
| **Silicone tubing** | 1/4" ID | 25ft | $10 | [Amazon](https://www.amazon.com/s?k=silicone+tubing+1%2F4+inch) | Enough for 3 stations |
| **Tube connectors** | 1/4" | 20pc | $7 | [Amazon](https://www.amazon.com/s?k=1%2F4+barb+connector+kit) | Tees, elbows, straight |
| **Irrigation stakes** | - | 10pc | $8 | [Amazon](https://www.amazon.com/s?k=drip+irrigation+stakes) | Optional, directs water |

**Recommended Purchase:**
- 25ft silicone tubing + connector kit ($17 total)

---

#### 7. Power Supply (One per Station)

| Option | Output | Size | Price | Link | Notes |
|--------|--------|------|-------|------|-------|
| **Budget** | 5V 2.5A USB | Standard | $6 | [Amazon 3-pack $15](https://www.amazon.com/s?k=5v+2.5a+power+supply+3+pack) | Adequate for Pi Zero |
| **Recommended** | 5V 3A Official Pi | Compact | $8 | [Amazon](https://www.amazon.com/s?k=raspberry+pi+official+power+supply) | Best quality |
| **Multi-pack** | 5V 3A USB-C | Standard | $8 ea | [Amazon 3-pack $22](https://www.amazon.com/s?k=5v+3a+usb+c+power+supply+3+pack) | Good for 3 stations |

**Recommended Purchase:**
- **For 3 stations**: 3-pack 5V 3A ($22 / $7.33 each) - **Best value**

---

#### 8. Storage & Wiring

| Component | Price | Link | Notes |
|-----------|-------|------|-------|
| **MicroSD card 32GB** (buy 3) | $7 ea | [Amazon 3-pack $18](https://www.amazon.com/s?k=microsd+32gb+3+pack) | SanDisk/Samsung |
| **Jumper wire kit** F-F, M-F | $7 | [Amazon](https://www.amazon.com/s?k=jumper+wire+kit+dupont) | 120pc kit |
| **Small project box** (optional) | $8 ea | [Amazon](https://www.amazon.com/s?k=small+project+enclosure+box) | Keep electronics dry |

**Recommended Purchase:**
- 3-pack microSD cards ($18)
- 1x jumper wire kit ($7) - shares across all stations

---

## Complete Shopping Lists with Links

### Option A: Ultra Budget Single Station ($58)

**Perfect for:** Testing Phase 1, tight budget, single plant

| Item | Price | Link | Qty |
|------|-------|------|-----|
| Pi Zero W (not Zero 2) | $10 | [Amazon](https://www.amazon.com/s?k=raspberry+pi+zero+w) | 1 |
| 16GB microSD card | $5 | [Amazon](https://www.amazon.com/s?k=microsd+16gb) | 1 |
| Capacitive sensor (from 5-pack) | $2.40 | [Amazon 5-pack $12](https://www.amazon.com/s?k=capacitive+soil+moisture+sensor+5+pack) | - |
| Mini pump (from 5-pack) | $3.60 | [Amazon 5-pack $18](https://www.amazon.com/s?k=dc+mini+water+pump+3v) | - |
| 1-ch relay (from 5-pack) | $1.60 | [Amazon 5-pack $8](https://www.amazon.com/s?k=5v+relay+module+1+channel+5+pack) | - |
| 5V 2.5A power supply | $6 | [Amazon](https://www.amazon.com/s?k=5v+2.5a+raspberry+pi+power) | 1 |
| Mason jar 1L reservoir | $3 | [Amazon](https://www.amazon.com/s?k=mason+jar+quart) | 1 |
| Tubing (from 25ft roll) | $3 | [Amazon 25ft $10](https://www.amazon.com/s?k=silicone+tubing+1%2F4+inch) | - |
| Jumper wires (from kit) | $7 | [Amazon](https://www.amazon.com/s?k=jumper+wire+kit+dupont) | - |

**TOTAL: $58** (plus extra components from multi-packs for future use)

---

### Option B: Recommended Single Station ($82)

**Perfect for:** Quality build, future expansion, most reliable

| Item | Price | Link | Qty |
|------|-------|------|-----|
| Pi Zero 2 W | $15 | [Adafruit](https://www.adafruit.com/product/5291) | 1 |
| 32GB microSD (from 3-pack) | $6 | [Amazon 3-pack $18](https://www.amazon.com/s?k=microsd+32gb+3+pack) | - |
| Capacitive sensor (from 5-pack) | $2.40 | [Amazon 5-pack $12](https://www.amazon.com/s?k=capacitive+soil+moisture+sensor+5+pack) | - |
| Mini pump (from 3-pack) | $5 | [Amazon 3-pack $15](https://www.amazon.com/s?k=mini+submersible+pump+5v+3+pack) | - |
| 4-channel relay module | $7 | [Amazon](https://www.amazon.com/s?k=4+channel+5v+relay+module) | 1 |
| 5V 3A power supply | $8 | [Amazon](https://www.amazon.com/s?k=raspberry+pi+official+power+supply) | 1 |
| 3L cereal dispenser | $13 | [Amazon](https://www.amazon.com/s?k=cereal+dispenser+3+liter) | 1 |
| Tubing + connectors | $17 | [Amazon](https://www.amazon.com/s?k=silicone+tubing+1%2F4+inch) + [connectors](https://www.amazon.com/s?k=1%2F4+barb+connector+kit) | - |
| Jumper wire kit | $7 | [Amazon](https://www.amazon.com/s?k=jumper+wire+kit+dupont) | - |

**TOTAL: $82** (includes extras for expansion)

---

### Option C: Three Station Complete System ($232)

**Perfect for:** Full Phase 3 deployment, best value per station

| Item | Unit Price | Link | Qty | Total |
|------|------------|------|-----|-------|
| Pi Zero 2 W | $15 | [Adafruit](https://www.adafruit.com/product/5291) | 3 | $45 |
| 32GB microSD 3-pack | - | [Amazon](https://www.amazon.com/s?k=microsd+32gb+3+pack) | 1 | $18 |
| Capacitive sensors 5-pack | - | [Amazon](https://www.amazon.com/s?k=capacitive+soil+moisture+sensor+5+pack) | 1 | $12 |
| Mini pumps 3-pack | - | [Amazon](https://www.amazon.com/s?k=mini+submersible+pump+5v+3+pack) | 1 | $15 |
| 1-ch relay 5-pack | - | [Amazon](https://www.amazon.com/s?k=5v+relay+module+1+channel+5+pack) | 1 | $8 |
| 5V 3A power supply 3-pack | - | [Amazon](https://www.amazon.com/s?k=5v+3a+usb+c+power+supply+3+pack) | 1 | $22 |
| Food containers 2L | $6 | [Amazon](https://www.amazon.com/s?k=food+storage+container+2+liter) | 3 | $18 |
| Silicone tubing 25ft | - | [Amazon](https://www.amazon.com/s?k=silicone+tubing+1%2F4+inch) | 1 | $10 |
| Tube connector kit | - | [Amazon](https://www.amazon.com/s?k=1%2F4+barb+connector+kit) | 1 | $7 |
| Jumper wire kit | - | [Amazon](https://www.amazon.com/s?k=jumper+wire+kit+dupont) | 1 | $7 |

**TOTAL: $232** ($77 per station with extras)

**Add Central Controller (Phase 3):**
- Raspberry Pi 4 (4GB) - $55 [Amazon](https://www.amazon.com/s?k=raspberry+pi+4+4gb)
- Pi 4 power supply - $10 [Amazon](https://www.amazon.com/s?k=raspberry+pi+4+power+supply)
- **Controller Total: +$65**

---

### Option D: Premium Three Station System ($320)

**Perfect for:** Best quality, minimal troubleshooting, looks great

| Item | Unit Price | Link | Qty | Total |
|------|------------|------|-----|-------|
| Pi Zero 2 W | $15 | [Adafruit](https://www.adafruit.com/product/5291) | 3 | $45 |
| 32GB high-speed microSD | $10 | [Amazon](https://www.amazon.com/s?k=sandisk+extreme+32gb+3+pack) | 3 | $30 |
| STEMMA I2C sensors | $7 | [Adafruit #4026](https://www.adafruit.com/product/4026) | 3 | $21 |
| Peristaltic pumps 5V | $13 | [Amazon](https://www.amazon.com/s?k=peristaltic+pump+5v) | 3 | $39 |
| 2-ch relay modules | $5 | [Amazon](https://www.amazon.com/s?k=2+channel+5v+relay+module) | 3 | $15 |
| Official Pi power supply | $8 | [Amazon](https://www.amazon.com/s?k=raspberry+pi+official+power+supply) | 3 | $24 |
| Glass beverage dispensers | $20 | [Amazon](https://www.amazon.com/s?k=glass+beverage+dispenser+1+gallon) | 3 | $60 |
| Premium tubing + fittings | - | [Amazon](https://www.amazon.com/s?k=premium+silicone+tubing+kit) | 1 | $18 |
| Quality jumper wires | - | [Amazon](https://www.amazon.com/s?k=premium+dupont+wire+kit) | 1 | $12 |
| Project boxes | $8 | [Amazon](https://www.amazon.com/s?k=small+project+enclosure+box) | 3 | $24 |

**TOTAL: $320** ($107 per station)

**Add Central Controller:**
- Raspberry Pi 4 (4GB) + case + heatsinks - $65
- **Total with controller: $385**

---

## Quick Order Links (Click to Buy)

### Recommended "Start with One, Plan for Three" Order

**Total: ~$100 (all you need for Phase 1 → Phase 3)**

- [ ] [Pi Zero 2 W x3 - $45](https://www.adafruit.com/product/5291) (buy 3 now, best availability)
- [ ] [32GB microSD 3-pack - $18](https://www.amazon.com/s?k=microsd+32gb+3+pack+sandisk)
- [ ] [Capacitive sensors 5-pack - $12](https://www.amazon.com/s?k=capacitive+soil+moisture+sensor+5+pack)
- [ ] [Mini pumps 3-pack 5V - $15](https://www.amazon.com/s?k=mini+submersible+pump+5v+3+pack)
- [ ] [4-channel relay module - $7](https://www.amazon.com/s?k=4+channel+5v+relay+module)
- [ ] [5V 3A power supplies 3-pack - $22](https://www.amazon.com/s?k=5v+3a+usb+c+power+supply+3+pack)
- [ ] [Silicone tubing 25ft - $10](https://www.amazon.com/s?k=silicone+tubing+1%2F4+inch+25+feet)
- [ ] [Tube connector kit - $7](https://www.amazon.com/s?k=barb+connector+kit+1%2F4+inch)
- [ ] [Jumper wire kit 120pc - $7](https://www.amazon.com/s?k=jumper+wire+kit+dupont+120)

**Electronics Subtotal: $143**

**Add Reservoirs Later (when you deploy each station):**
- Station 1: Food container 2L - $6
- Station 2: Food container 2L - $6
- Station 3: Food container 2L - $6

**Grand Total: $161 for all 3 stations** ($54 per station!)

---

## Shopping Strategy

### Best Approach:
1. **Order electronics NOW** (items above) - $143
2. **Build & test Station 1** with what you have
3. **Order reservoirs** as you deploy each station
4. **Expand at your pace** - all electronics ready to go!

### Why This Works:
- Electronics are the hard part (shipping, availability)
- Reservoirs are easy (local stores, same-day)
- Multi-packs = huge savings ($54/station vs $82 individual)
- Components in stock for future stations

---

## Where to Buy

### Primary Retailers

| Store | Best For | Shipping | Notes |
|-------|----------|----------|-------|
| [**Adafruit**](https://www.adafruit.com) | Pi boards, I2C sensors | 2-5 days | Quality, great docs |
| [**Amazon**](https://www.amazon.com) | Everything else | 1-2 days | Prime shipping, easy returns |
| [**CanaKit**](https://www.canakit.com) | Pi starter kits | 3-7 days | Bundled deals |
| [**SparkFun**](https://www.sparkfun.com) | Quality sensors | 3-5 days | Educational focus |

### Budget Options

| Store | Savings | Tradeoff | Timeline |
|-------|---------|----------|----------|
| **AliExpress** | 30-50% cheaper | 3-6 week shipping, variable quality | Order now for spring |
| **eBay** | 20-40% cheaper | Check seller ratings carefully | 1-3 weeks |

### Local Stores

| Store | Good For | Notes |
|-------|----------|-------|
| **Micro Center** | Pi boards, immediate pickup | Only 25 US locations |
| **Home Depot** | Reservoirs, tubing | Plumbing section |
| **Target/Walmart** | Food containers, mason jars | Housewares |

---

## Money-Saving Tips

1. **Buy Multi-Packs Now**
   - 5-pack sensors: $2.40/ea vs $8/ea (save $5.60 each!)
   - 3-pack pumps: $5/ea vs $7/ea (save $2 each)
   - 3-pack SD cards: $6/ea vs $10/ea (save $4 each)
   - **Total savings: ~$30** on 3-station system

2. **Skip Unnecessary Items (Phase 1)**
   - ❌ Water level sensors (Phase 2)
   - ❌ Project boxes (nice-to-have)
   - ❌ LEDs/buttons (code-controlled is better)
   - **Save: $20-30**

3. **DIY Reservoir Options**
   - Reuse juice bottles (free!)
   - Thrift store containers ($1-2)
   - Mason jars you already have
   - **Save: $15-40**

4. **Wait for Sales**
   - Amazon Prime Day (July)
   - Black Friday (November)
   - Electronics typically 15-25% off
   - **Save: $20-40** on full system

---

## Quality vs Budget Decision Matrix

| If You Value... | Choose... | Cost | Why |
|----------------|-----------|------|-----|
| **Learning cheap** | Ultra Budget | $58 | Test before investing |
| **Best value** | Option C (3 stations) | $232 | Lowest per-station cost |
| **Reliability** | Recommended Single | $82 | Quality components, expandable |
| **Aesthetics** | Premium Option D | $320 | Looks great, reliable |
| **Fastest start** | CanaKit Starter | $40 | Pre-packaged, quick |

---

## Next Steps After Ordering

1. **While waiting for delivery:**
   - [ ] Read [Raspberry Pi Setup Guide](../../docs/getting-started/raspberry-pi-setup.md)
   - [ ] Review [Phase 1 Setup Guide](../docs/phase1-setup.md)
   - [ ] Plan station locations in your home

2. **When components arrive:**
   - [ ] Test each component individually
   - [ ] Follow [Compact Station Assembly](./compact-station-design.md)
   - [ ] Deploy using [Code Deployment Guide](../../docs/deployment-guide.md)

3. **Join the community:**
   - Raspberry Pi Forums
   - r/raspberry_pi subreddit
   - Adafruit Discord

---

## Cost Comparison vs Commercial

| Solution | Cost | Features | Notes |
|----------|------|----------|-------|
| **DIY (This project)** | $54-110 | Custom, learning, expandable | You built it! |
| Xiaomi Mi Flora | $25 | Monitor only, no watering | Per plant |
| Elgato Eve Aqua | $100 | Timer-based, no moisture sensing | Per plant |
| Rainpoint WiFi | $70 | Basic moisture control | Per plant |
| **Commercial 3-plant** | $210-300 | Limited customization | No learning |

**Our advantage:** Cheaper, educational, infinitely customizable, Grafana dashboards!
