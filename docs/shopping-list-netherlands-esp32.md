# Netherlands Shopping List - ESP32 Based 25-Plant System

**Optimized for 25-plant monitoring with manual watering**

## Quick Cost Summary

| Configuration | 5 Plants (Test) | 25 Plants (Full) | Per Plant |
|--------------|-----------------|------------------|-----------|
| **ESP32 Battery** | €149 | €520 | €21 |
| **ESP32 USB** | €130 | €437 | €17 |
| **ESP8266 Budget** | €95 | €325 | €13 |

---

## Recommended: Start with 5 Plants (€149)

Test the system before committing to all 25 plants!

### Starter Kit Shopping List

**Central Hub:**
| Item | Shop | Link | Qty | Price |
|------|------|------|-----|-------|
| Raspberry Pi 4 (4GB) | Kiwi Electronics | [Link](https://www.kiwi-electronics.com/en/raspberry-pi-4-model-b-4gb-10298) | 1 | €55 |
| 32GB microSD | Amazon.nl | [Link](https://www.amazon.nl/-/en/SanDisk-microSDHC-Memory-Adapter-Performance/dp/B08HYFMVV6) | 1 | €10 |
| Pi 4 Power Supply | Amazon.nl | Search "raspberry pi 4 power supply" | 1 | €12 |
| Pi 4 Case + Heatsink | Amazon.nl | Search "raspberry pi 4 case" | 1 | €10 |

**Sensor Nodes (5×):**
| Item | Shop | Link | Qty | Price |
|------|------|------|-----|-------|
| ESP32 DevKit C | Amazon.nl | [Search](https://www.amazon.nl/s?k=esp32+devkit) | 5 | €25 |
| Capacitive Sensors | Amazon.nl | [8-pack](https://www.amazon.nl/Capacitieve-bodemvochtigheidssensor-ZSWQ-Sensor-Hygrometer-Vochtdetectie/dp/B08GC5KT4T) | 1 | €20 |
| USB Power Adapters 5V | Amazon.nl | Search "usb charger 5v 1a" | 5 | €25 |
| Jumper Wires | Bits & Parts | [Shop](https://www.bitsandparts.nl/en/) | 1 | €7 |

**TOTAL: €164** (test with 5 plants)

---

## Option 1: ESP32 USB-Powered (Recommended for 25 Plants)

**Most practical:** Plug into wall, no battery management needed

### Central Hub (1×) - €87

| Item | Shop | Link | Price EUR |
|------|------|------|-----------|
| Raspberry Pi 4 (4GB) | Kiwi Electronics | [Link](https://www.kiwi-electronics.com/en/raspberry-pi-4-model-b-4gb-10298) | €55 |
| 32GB microSD | Amazon.nl | [Link](https://www.amazon.nl/-/en/SanDisk-microSDHC-Memory-Adapter-Performance/dp/B08HYFMVV6) | €10 |
| Pi 4 Power Supply 5V 3A | Amazon.nl | [Link](https://www.amazon.nl/s?k=raspberry+pi+4+power+supply+official) | €12 |
| Pi 4 Case + Heatsink | Amazon.nl | [Link](https://www.amazon.nl/s?k=raspberry+pi+4+case+heatsink) | €10 |

### Sensor Nodes (25×) - €350

| Item | Shop | Link | Qty | Unit | Total |
|------|------|------|-----|------|-------|
| **ESP32 DevKit C** | Amazon.nl | [5-pack](https://www.amazon.nl/s?k=esp32+development+board+5+pack) | 5 packs | €20 | €100 |
| OR: Individual ESP32 | Bits & Parts / Amazon.nl | [Search](https://www.bitsandparts.nl/en/) | 25 | €4-5 | €100-125 |
| **Capacitive Sensors** | Amazon.nl | [ZSWQ 8-pack](https://www.amazon.nl/Capacitieve-bodemvochtigheidssensor-ZSWQ-Sensor-Hygrometer-Vochtdetectie/dp/B08GC5KT4T) × 4 | 4 packs | €20 | €80 |
| **USB Power Adapters** | Amazon.nl | [10-pack €35](https://www.amazon.nl/s?k=usb+charger+5v+1a+10+pack) × 3 | 3 packs | €35 | €105 |
| OR: Reuse old phone chargers | Free | N/A | 25 | €0 | €0 |
| **Micro USB Cables 1m** | Amazon.nl | [10-pack €12](https://www.amazon.nl/s?k=micro+usb+cable+1m+10+pack) × 3 | 3 packs | €12 | €36 |
| **Jumper Wires F-F** | Bits & Parts | [Link](https://www.bitsandparts.nl/en/) | 1 | €7 | €7 |
| **Dupont Connectors** (for sensors) | Amazon.nl | [Kit](https://www.amazon.nl/s?k=dupont+connector+kit) | 1 | €10 | €10 |
| **Small Project Boxes** (optional) | Amazon.nl | [10-pack €18](https://www.amazon.nl/s?k=small+project+box+plastic) × 3 | 3 | €18 | €54 |

**Nodes Subtotal: €292-392** (with/without boxes)

### Optional: Battery Backup

For power outage resilience:
| Item | Shop | Price |
|------|------|-------|
| UPS for Raspberry Pi 4 | Amazon.nl | €40-60 |

### **Total System Cost: €437** (€17/plant)

Without project boxes: **€383** (€15/plant)

---

## Option 2: ESP32 Battery-Powered (Maximum Flexibility)

**Wire-free:** Place anywhere, lasts 4-6 months per charge

### Central Hub (1×) - €87
Same as Option 1

### Sensor Nodes (25×) - €433

| Item | Shop | Link | Qty | Unit | Total |
|------|------|------|-----|------|-------|
| **ESP32 DevKit C** | Amazon.nl / Bits & Parts | [Search](https://www.amazon.nl/s?k=esp32+devkit) | 25 | €4-5 | €125 |
| **Capacitive Sensors** | Amazon.nl | [ZSWQ 8-pack €20](https://www.amazon.nl/Capacitieve-bodemvochtigheidssensor-ZSWQ-Sensor-Hygrometer-Vochtdetectie/dp/B08GC5KT4T) × 4 | 4 | €20 | €80 |
| **18650 Battery Holders (2-cell)** | Amazon.nl | [10-pack €15](https://www.amazon.nl/s?k=18650+battery+holder+2+cell) × 3 | 3 | €15 | €45 |
| **18650 Batteries** | Amazon.nl | [4-pack €12](https://www.amazon.nl/s?k=18650+battery+rechargeable) × 13 | 13 | €12 | €156 |
| **TP4056 USB Chargers** | Amazon.nl | [10-pack €8](https://www.amazon.nl/s?k=tp4056+charger+module+10+pack) × 3 | 3 | €8 | €24 |
| **Jumper Wires** | Bits & Parts | [Link](https://www.bitsandparts.nl/en/) | 1 | €7 | €7 |
| **Small Project Boxes** | Amazon.nl | [10-pack €18](https://www.amazon.nl/s?k=small+project+box) × 3 | 3 | €18 | €54 |

**Nodes Subtotal: €491**

### **Total System Cost: €578** (€23/plant)

**Battery life:** 4-6 months between USB charges

---

## Option 3: ESP8266 Budget Build

**Cheapest option:** Good for testing or budget constraint

### Central Hub (1×) - €87
Same as Option 1

### Sensor Nodes (25×) - €238

| Item | Shop | Link | Qty | Unit | Total |
|------|------|------|-----|------|-------|
| **ESP8266 NodeMCU** | Amazon.nl | [5-pack €13](https://www.amazon.nl/s?k=esp8266+nodemcu+5+pack) × 5 | 5 | €13 | €65 |
| **Capacitive Sensors** | Amazon.nl | [ZSWQ 8-pack €20](https://www.amazon.nl/Capacitieve-bodemvochtigheidssensor-ZSWQ-Sensor-Hygrometer-Vochtdetectie/dp/B08GC5KT4T) × 4 | 4 | €20 | €80 |
| **USB Chargers** (reuse old) | Free | N/A | 25 | €0 | €0 |
| OR: Buy new chargers | Amazon.nl | [10-pack €35] × 3 | 3 | €35 | €105 |
| **Micro USB Cables** | Amazon.nl | [10-pack €12] × 3 | 3 | €12 | €36 |
| **Jumper Wires** | Bits & Parts | Link | 1 | €7 | €7 |

**Nodes Subtotal: €188-293** (with/without chargers)

### **Total System Cost: €275-380** (€11-15/plant)

---

## Detailed Product Links

### ESP32 Boards

**Option A: Amazon.nl Individual**
- Search: "ESP32 development board"
- URL: https://www.amazon.nl/s?k=esp32+development+board
- Brands: AZDelivery, DEBO, Freenove
- Price: €4-6 each
- Buy: 25 individual or 5× 5-packs

**Option B: Bits & Parts**
- Shop: https://www.bitsandparts.nl/en/
- Search site for "ESP32"
- Usually €4-5 each
- Support local NL business

**Option C: AliExpress (Budget, slow)**
- URL: https://nl.aliexpress.com/w/wholesale-esp32-devkit.html
- Price: €2-3 each
- Shipping: 2-4 weeks
- Buy 30 (extras for testing)

**Recommended:** Amazon.nl 5-packs for best value

---

### ESP8266 Boards (Budget Alternative)

**Amazon.nl:**
- Search: "ESP8266 NodeMCU"
- URL: https://www.amazon.nl/s?k=esp8266+nodemcu
- Price: €2.50-3.50 each
- 5-packs available: ~€13

**Bits & Parts:**
- Usually stock ESP8266 boards
- €3-4 each

---

### Capacitive Soil Sensors

**Best Value: ZSWQ 8-Pack**
- URL: https://www.amazon.nl/Capacitieve-bodemvochtigheidssensor-ZSWQ-Sensor-Hygrometer-Vochtdetectie/dp/B08GC5KT4T
- Price: €18-22 per 8-pack
- Buy: 4 packs for 25+ sensors (32 sensors total)
- Total: €80

**Alternative: iHaospace Individual**
- URL: https://www.amazon.nl/-/en/iHaospace-Gardena-Moisture-Capacitive-Compatible/dp/B07DDFZ3MD
- Price: ~€9 each
- Better quality, more expensive
- Total for 25: €225

**Recommendation:** Buy 4× ZSWQ 8-packs (€80 total) + have 7 spares

---

### Raspberry Pi 4

**Kiwi Electronics (Recommended):**
- Pi 4 4GB: https://www.kiwi-electronics.com/en/raspberry-pi-4-model-b-4gb-10298
- Price: €55
- In stock, ships same day
- Official Pi reseller

**Alternative: RaspberryStore.nl**
- URL: https://www.raspberrystore.nl/
- Similar pricing
- Dutch company

**Amazon.nl:**
- Search: "Raspberry Pi 4 4GB"
- Usually €60-70 (slightly more expensive)

---

### Power Supplies

**For ESP32/ESP8266 (USB 5V 1A):**
- Amazon.nl: Search "usb charger 5v 1a"
- Individual: €2-3 each
- 10-pack: €35-40 (better value)
- Recommendation: Buy 3× 10-packs

**For Raspberry Pi 4 (USB-C 5V 3A):**
- Official: https://www.amazon.nl/s?k=raspberry+pi+4+official+power+supply
- Price: €12
- Must be 3A for Pi 4!

---

### Batteries (Option 2 Only)

**18650 Rechargeable Batteries:**
- Amazon.nl: Search "18650 battery rechargeable"
- URL: https://www.amazon.nl/s?k=18650+battery+rechargeable
- Brands: Samsung, LG, Panasonic (authentic!)
- Price: ~€3 per battery
- Need: 50 batteries (2 per node × 25)
- Buy: 4-packs, need 13 packs

**18650 Battery Holders:**
- Amazon.nl: Search "18650 battery holder 2 cell"
- URL: https://www.amazon.nl/s?k=18650+battery+holder+2+cell
- Price: €1.50 each in 10-pack
- Need: 25 holders

**TP4056 USB Charging Modules:**
- Amazon.nl: Search "TP4056 charger module"
- URL: https://www.amazon.nl/s?k=tp4056+charging+module
- Price: €0.80 each in 10-pack
- Need: 25 modules

**⚠️ Battery Warning:**
- Only buy authentic batteries (Samsung, LG, Panasonic)
- Avoid cheap Chinese knockoffs (fire hazard!)
- Check seller reviews carefully

---

### Accessories

**Jumper Wires:**
- Bits & Parts: https://www.bitsandparts.nl/en/
- Search: "dupont jumper wire female"
- Need: Female-to-Female (for sensors)
- Price: €7-10 for 120pc kit

**Project Boxes (Optional):**
- Amazon.nl: Search "small project box plastic"
- URL: https://www.amazon.nl/s?k=small+project+box+plastic
- Size: 10×6×3cm or similar
- Price: €1.50-2 each, or 10-packs for €15-20
- Need: 25 boxes

**MicroUSB Cables:**
- Amazon.nl: Search "micro usb cable 1m 10 pack"
- URL: https://www.amazon.nl/s?k=micro+usb+cable+1m+10+pack
- Price: €10-15 per 10-pack
- Need: 3 packs (30 cables)

---

## Shopping Strategy

### Phase 1: Test with 5 Plants (€149)

**Order This Week:**
1. Kiwi Electronics order (~€87):
   - 1× Raspberry Pi 4 4GB
   - 1× Pi 4 case
   - Free shipping if >€40

2. Amazon.nl order (~€60):
   - 1× 32GB microSD card
   - 1× Pi 4 power supply
   - 5× ESP32 boards (or 1× 5-pack)
   - 1× ZSWQ 8-pack sensors
   - 5× USB chargers
   - Prime shipping

3. Bits & Parts (~€7):
   - 1× Jumper wire kit

**Total: €154**

**Timeline:**
- Order Monday → Delivery Wednesday/Thursday
- Weekend: Build and test central hub
- Week 2: Flash ESP32 nodes, deploy to 5 plants
- Week 3-4: Monitor and evaluate

### Phase 2: Scale to 25 Plants (Additional €288)

**After successful test:**

Amazon.nl order (~€280):
- 4× more 5-packs ESP32 (20 boards) - €80
- 3× more ZSWQ 8-packs (24 sensors) - €60
- 2× more 10-packs USB chargers (20 chargers) - €70
- 2× more 10-packs USB cables - €24
- 2× 10-packs project boxes (optional) - €36

**Total Phase 1 + 2: €442** (€18/plant for 25 plants)

---

## Cost Comparison

| Approach | 5 Plants | 25 Plants | Per Plant | Notes |
|----------|----------|-----------|-----------|-------|
| **ESP32 USB (Recommended)** | €149 | €437 | €17 | Plug & play |
| **ESP32 Battery** | €192 | €578 | €23 | Wire-free |
| **ESP8266 Budget** | €120 | €325 | €13 | Cheapest |
| **Original Pi Zero Plan** | €415 | €1,950 | €78 | ❌ Too expensive |

**Savings with ESP32:** €1,513 vs original plan!

---

## What to Order RIGHT NOW

### Minimal Test Order (€149)

Perfect for validating the concept:

**Kiwi Electronics (€67):**
- [ ] 1× Raspberry Pi 4 4GB - €55
- [ ] 1× Official Pi 4 Power Supply - €12

**Amazon.nl (€75):**
- [ ] 1× SanDisk Ultra 32GB microSD - €10
- [ ] 1× Pi 4 Case - €10
- [ ] 1× ESP32 5-pack - €20
- [ ] 1× ZSWQ Soil Sensor 8-pack - €20
- [ ] 5× USB Chargers (or use old ones) - €15
- [ ] Free Prime shipping

**Bits & Parts (€7):**
- [ ] 1× Dupont Jumper Wire Kit - €7

---

## Next Steps

1. **Order 5-plant test kit** (€149)
2. **While waiting (2-3 days):**
   - Read [ESP32 Setup Guide](./esp32-sensor-node-guide.md)
   - Review [Architecture](./architecture-25-plant-system.md)
   - Plan which 5 plants to monitor first

3. **When components arrive:**
   - Set up central Pi 4 hub
   - Flash ESP32 firmware
   - Test with first plant
   - Scale to 5 plants

4. **After 2-week test:**
   - Evaluate: Does it work well?
   - If yes: Order remaining 20 nodes
   - If no: Adjust before scaling

---

## Local Netherlands Shops

**Electronics:**
- **Kiwi Electronics** - https://www.kiwi-electronics.com/en/
- **Bits & Parts** - https://www.bitsandparts.nl/en/
- **Farnell** - https://nl.farnell.com/
- **Antratek** - https://www.antratek.nl/

**General:**
- **Action** - Cheap containers, USB cables
- **HEMA** - Storage boxes
- **Gamma/Praxis** - Project boxes in electrical section

---

## FAQ

**Q: Can I mix ESP32 and ESP8266?**
A: Yes! Same MQTT protocol, both work together.

**Q: Do I need 25 USB outlets?**
A: No - use multi-port USB chargers. One 10-port charger can power 10 nodes.

**Q: Battery vs USB power?**
A: USB if near outlets, battery if want to move plants around.

**Q: Can I add automation later?**
A: Yes! Add pumps to ESP32 nodes or use separate Pi Zero + pump setup.

**Q: What if my house is huge?**
A: Add WiFi extenders or use ESP32 with Ethernet adapters for distant nodes.

---

## Updates

**Last Updated:** November 2024
**Currency:** EUR (€)
**Availability:** All products in stock as of Nov 2024
**Prices:** Include VAT, may fluctuate ±10%

Ready to order? Start with the 5-plant test kit!
