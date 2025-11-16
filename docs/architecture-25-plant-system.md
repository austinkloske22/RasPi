# 25-Plant Smart Monitoring System - Optimized Architecture

**Realistic IoT design for monitoring 25+ plants with central control**

## Why This Architecture?

**Original Problem:**
- 25 × Raspberry Pi Zero 2 W = €425 just for boards
- 25 × Power supplies = €250
- 25 × Wall outlets needed
- Total overkill for simple sensor reading

**Smart Solution:**
- 25 × ESP32 boards = €100-125
- 1 × Raspberry Pi 4 (central brain) = €55
- Battery-powered sensor nodes
- **Save €495+ and much simpler!**

---

## System Architecture

### Overview

```
┌─────────────────────────────────────────┐
│      Central Raspberry Pi 4             │
│  ┌─────────────────────────────────┐   │
│  │  MQTT Broker (Mosquitto)        │   │
│  │  InfluxDB (time-series data)    │   │
│  │  Grafana (dashboards)           │   │
│  │  Web Interface (plant status)   │   │
│  │  Alerting (low moisture)        │   │
│  └─────────────────────────────────┘   │
└─────────────────┬───────────────────────┘
                  │ WiFi Network
        ┌─────────┴─────────┬─────────────┬───── (25 nodes total)
        │                   │             │
  ┌─────▼──────┐      ┌────▼─────┐   ┌───▼──────┐
  │  ESP32 #1  │      │ ESP32 #2 │   │ ESP32 #25│
  │  Living Rm │      │ Kitchen  │   │ Bedroom  │
  │            │      │          │   │          │
  │ [Sensor]   │      │ [Sensor] │   │ [Sensor] │
  │ [Battery]  │      │ [Battery]│   │ [Battery]│
  └────────────┘      └──────────┘   └──────────┘
       Plant 1           Plant 2        Plant 25
```

### Communication Flow

1. **Every 6 hours** (4x per day):
   - ESP32 wakes from deep sleep
   - Reads moisture sensor
   - Connects to WiFi
   - Publishes to MQTT: `plants/{plant_id}/moisture`
   - Goes back to sleep (saves battery)

2. **Central Pi 4** continuously:
   - Receives MQTT messages
   - Stores data in InfluxDB
   - Updates Grafana dashboard
   - Sends alerts if moisture too low
   - Provides web interface for viewing

3. **You** (manual watering Phase 1):
   - Check Grafana dashboard
   - See which plants need water
   - Water manually
   - Log watering events in system

---

## Hardware Components

### Central Hub (1x Raspberry Pi 4)

| Component | Purpose | Price EUR |
|-----------|---------|-----------|
| Raspberry Pi 4 (4GB) | Central controller | €55 |
| 32GB microSD card | OS + databases | €10 |
| Power supply 5V 3A | Always-on power | €12 |
| Case + heatsink | Protection, cooling | €10 |

**Hub Total: €87**

---

### Sensor Nodes (25x ESP32)

**Option A: ESP32 DevKit (Recommended)**

| Component | Qty | Unit Price | Total |
|-----------|-----|------------|-------|
| ESP32 DevKit C | 25 | €4-5 | €100-125 |
| Capacitive moisture sensors | 25 | €2.40 | €60 |
| 18650 battery holders | 25 | €1.50 | €38 |
| 18650 batteries (2x per node) | 50 | €3 | €150 |
| TP4056 charging modules | 25 | €0.80 | €20 |
| Jumper wires (bulk) | 1 | €15 | €15 |
| Small project boxes | 25 | €2 | €50 |

**Sensor Nodes Total: €433-458**

**Option B: ESP8266 (Budget)**

| Component | Qty | Unit Price | Total |
|-----------|-----|------------|-------|
| ESP8266 NodeMCU | 25 | €2.50 | €63 |
| Capacitive moisture sensors | 25 | €2.40 | €60 |
| USB power banks (reuse old) | 25 | Free-€5 | €0-125 |
| Jumper wires (bulk) | 1 | €15 | €15 |

**Sensor Nodes Total: €138-263** (if reusing power banks)

---

## Complete System Cost

### Option 1: ESP32 with Batteries (Best)

| Category | Cost EUR |
|----------|----------|
| Central Hub (Pi 4) | €87 |
| 25× ESP32 sensor nodes | €433 |
| **TOTAL** | **€520** |
| **Per plant** | **€21** |

### Option 2: ESP32 USB Powered (Simpler)

| Category | Cost EUR |
|----------|----------|
| Central Hub (Pi 4) | €87 |
| 25× ESP32 boards | €125 |
| 25× USB power adapters | €125 |
| 25× Moisture sensors | €60 |
| Misc (wires, boxes) | €40 |
| **TOTAL** | **€437** |
| **Per plant** | **€17** |

### Option 3: ESP8266 Budget Build

| Category | Cost EUR |
|----------|----------|
| Central Hub (Pi 4) | €87 |
| 25× ESP8266 boards | €63 |
| 25× Moisture sensors | €60 |
| 25× USB power (old phone chargers) | €0-100 |
| Misc (wires) | €15 |
| **TOTAL** | **€225-325** |
| **Per plant** | **€9-13** |

---

## Phase 1: Manual Watering with Smart Monitoring

### Features

**Sensor Nodes:**
- Read soil moisture every 6 hours
- Report to central Pi via MQTT
- Battery lasts 2-6 months between charges
- LED indicator: Green (good) / Yellow (check) / Red (dry)

**Central Dashboard:**
- Grafana showing all 25 plants
- Color-coded moisture levels
- Last reading timestamp
- Historical charts (track trends)
- Mobile-friendly web view

**Manual Watering:**
- Dashboard shows which plants need water
- You water manually based on data
- Optional: Log watering events in dashboard
- Get email/Telegram alerts for dry plants

### Benefits Over Automated

✅ **Much cheaper** - No pumps, valves, plumbing
✅ **More reliable** - No pump failures, leaks, clogs
✅ **Flexibility** - You decide watering amount
✅ **Learning** - Understand each plant's needs
✅ **Scalable** - Easy to add plants 26-50
✅ **Battery powered** - Place anywhere, no outlets

---

## Phase 2: Semi-Automated (Optional Future)

**Add automated watering for 3-5 "priority plants":**

1. Keep 20-22 plants on monitoring-only
2. Add automation to 3-5 critical plants:
   - High-maintenance plants
   - Hard to reach locations
   - Vacation watering
3. Use the original Pi Zero + pump setup from earlier plans
4. Best of both worlds!

---

## ESP32 vs ESP8266 Comparison

| Feature | ESP32 | ESP8266 | Winner |
|---------|-------|---------|--------|
| **Price** | €4-5 | €2.50 | ESP8266 |
| **WiFi** | 2.4GHz | 2.4GHz | Tie |
| **Bluetooth** | Yes (BLE) | No | ESP32 |
| **Deep Sleep** | 10µA | 20µA | ESP32 |
| **Battery Life** | 3-6 months | 2-4 months | ESP32 |
| **GPIO Pins** | 34 | 17 | ESP32 |
| **CPU Speed** | 240MHz | 80MHz | ESP32 |
| **Memory** | 520KB | 80KB | ESP32 |
| **Ecosystem** | Newer, active | Mature, stable | Tie |

**Recommendation:**
- **ESP32** if you want best battery life and future features
- **ESP8266** if you want cheapest solution and USB-powered nodes

---

## Detailed Sensor Node Design

### ESP32 Battery-Powered Node

**Components per node:**
```
┌─────────────────────────────┐
│    Project Box (10x6x3cm)   │
│                             │
│  ┌──────────────┐           │
│  │   ESP32      │           │
│  │   DevKit     │           │
│  └──────┬───────┘           │
│         │                   │
│  ┌──────▼──────┐            │
│  │ TP4056 USB  │◄─── Charging port
│  │  Charger    │            │
│  └──────┬──────┘            │
│         │                   │
│  ┌──────▼──────┐            │
│  │ 2x 18650    │            │
│  │ Batteries   │            │
│  │  (7.4V)     │            │
│  └─────────────┘            │
│         ↓                   │
│  [Moisture Sensor] ───►     │
│    (stuck in soil)          │
└─────────────────────────────┘
```

**Power Consumption:**
- Deep sleep: 10µA (0.00001A)
- Wake + read: 80mA for 5 seconds
- WiFi transmit: 160mA for 3 seconds

**Battery Life Calculation:**
- 2× 18650 batteries = 6000mAh at 3.7V
- Reading 4× per day = 96 readings/month
- Deep sleep 99.9% of time
- **Expected life: 4-6 months per charge**

### ESP32 USB-Powered Node (Simpler)

**Components per node:**
```
┌─────────────────────────────┐
│    Project Box              │
│                             │
│  ┌──────────────┐           │
│  │   ESP32      │           │
│  │   DevKit     │           │
│  └──────────────┘           │
│         ↑                   │
│         │                   │
│    USB Cable ───────► Wall Adapter
│         │                   │
│         ↓                   │
│  [Moisture Sensor] ───►     │
│    (stuck in soil)          │
└─────────────────────────────┘
```

**Pros:** Simpler, no battery management
**Cons:** Needs outlet near each plant

---

## Software Stack

### Central Raspberry Pi 4

**Operating System:**
- Raspberry Pi OS Lite (64-bit)

**Services:**
1. **Mosquitto MQTT Broker**
   - Receives sensor data
   - Handles 25+ concurrent connections
   - Persists messages

2. **InfluxDB 2.x**
   - Stores time-series sensor data
   - Efficient for millions of readings
   - Built-in retention policies

3. **Grafana**
   - Real-time dashboards
   - 25-plant overview grid
   - Individual plant detail views
   - Mobile-responsive

4. **Node-RED** (optional)
   - Visual flow programming
   - Alert rules
   - Telegram/Email notifications

**Storage Requirements:**
- 25 plants × 4 readings/day × 365 days = 36,500 readings/year
- ~1KB per reading = 36MB per year
- 32GB SD card = decades of data

### ESP32 Sensor Node

**Platform:** Arduino IDE or PlatformIO

**Libraries:**
- WiFi.h (built-in)
- PubSubClient.h (MQTT)
- Wire.h (I2C sensors)

**Basic Code Structure:**
```cpp
#include <WiFi.h>
#include <PubSubClient.h>

// Deep sleep for 6 hours (21600 seconds)
#define SLEEP_DURATION 21600

void setup() {
  // Read moisture sensor
  int moisture = analogRead(SENSOR_PIN);

  // Connect to WiFi
  WiFi.begin(ssid, password);

  // Connect to MQTT broker
  client.connect("plant_living_room_01");

  // Publish moisture reading
  char msg[50];
  snprintf(msg, 50, "{\"moisture\":%d,\"battery\":%d}", moisture, battery);
  client.publish("plants/living_room_01/moisture", msg);

  // Go to deep sleep
  esp_deep_sleep_start();
}

void loop() {
  // Never reaches here (deep sleep reboots)
}
```

**Full code examples:** See `/projects/plant-watering/src/phase1-esp32/`

---

## Grafana Dashboard Design

### Main Dashboard: 25-Plant Overview

```
┌────────────────────────────────────────────────┐
│  🌱 House Plant Monitoring - 25 Plants         │
│  Last Update: 2 minutes ago                    │
├────────────────────────────────────────────────┤
│                                                │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐          │
│  │ 🟢 │ │ 🟢 │ │ 🟡 │ │ 🔴 │ │ 🟢 │   Row 1  │
│  │ 85%│ │ 72%│ │ 45%│ │ 12%│ │ 91%│          │
│  │ LR1│ │ LR2│ │Kit │ │BR1 │ │BR2 │          │
│  └────┘ └────┘ └────┘ └────┘ └────┘          │
│                                                │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐          │
│  │ 🟢 │ │ 🟡 │ │ 🟢 │ │ 🔴 │ │ 🟢 │   Row 2  │
│  │ 78%│ │ 38%│ │ 82%│ │ 15%│ │ 88%│          │
│  └────┘ └────┘ └────┘ └────┘ └────┘          │
│                                                │
│  ... (5 rows total)                           │
│                                                │
├────────────────────────────────────────────────┤
│  Alerts:                                       │
│  ⚠️  Bedroom Plant #1 needs water (12%)       │
│  ⚠️  Bedroom Plant #4 needs water (15%)       │
│  ℹ️  Kitchen Plant should be checked (38%)    │
└────────────────────────────────────────────────┘
```

### Individual Plant View

Click any plant tile → Detailed view:
- Last 7 days moisture chart
- Watering history
- Battery level (if applicable)
- Last reading timestamp
- Manual watering log button

---

## Deployment Strategy for 25 Plants

### Week 1: Build Central Hub
- [ ] Set up Raspberry Pi 4
- [ ] Install Mosquitto, InfluxDB, Grafana
- [ ] Create basic dashboard
- [ ] Test with dummy data

### Week 2-3: Build 5 Test Nodes
- [ ] Order ESP32 boards × 5
- [ ] Order sensors × 5
- [ ] Build and test first 5 nodes
- [ ] Deploy to 5 plants
- [ ] Verify MQTT communication
- [ ] Tune dashboard

### Week 4-5: Scale to 15 Nodes
- [ ] Order ESP32 × 10 more
- [ ] Build nodes 6-15
- [ ] Deploy and test
- [ ] Optimize battery life

### Week 6-7: Complete 25-Node System
- [ ] Order final ESP32 × 10
- [ ] Build nodes 16-25
- [ ] Full deployment
- [ ] System tuning

### Week 8+: Optimization
- [ ] Monitor battery levels
- [ ] Adjust reading frequency
- [ ] Add alert rules
- [ ] Consider automation for 3-5 plants

---

## Shopping List - 25 Plant System

See detailed shopping list: [Netherlands ESP32 Shopping List](./shopping-list-netherlands-esp32.md)

**Quick Summary:**

| Option | Total Cost | Per Plant | Notes |
|--------|------------|-----------|-------|
| **ESP32 Battery** | €520 | €21 | Best, wire-free |
| **ESP32 USB** | €437 | €17 | Simpler setup |
| **ESP8266 Budget** | €225-325 | €9-13 | Cheapest |

---

## Advantages Over Original Plan

| Aspect | Original (25× Pi Zero) | New (ESP32 + Pi 4) | Savings |
|--------|----------------------|-------------------|---------|
| **Board Cost** | €425 | €125 | €300 |
| **Power** | 25 outlets | 1 outlet + batteries | 24 outlets |
| **Setup Time** | 25× OS installs | 1× OS + 25× flash | Hours saved |
| **Maintenance** | 25× updates | 1× update | Much easier |
| **Total Cost** | €675+ | €437-520 | €155-238 |
| **Battery Option** | No | Yes | Flexibility |
| **Scalability** | Hard | Easy | Add node in 5 min |

---

## Future Expansion

### Add More Plants (26-50)
- Cost per additional plant: €17-21
- Just add another ESP32 + sensor
- No changes to central hub needed

### Add Automation (Phase 2)
- Keep monitoring system as-is
- Add 3-5 automated watering stations using original Pi Zero plan
- Hybrid system: 20 monitor-only + 5 auto-water

### Add Environmental Sensors
- Temperature/humidity (DHT22) - €5
- Light level (LDR) - €2
- Air quality (BME680) - €15

### Mobile App
- Native Android/iOS app
- Push notifications
- One-tap watering log

---

## Recommended Approach

**Start with 5 plants** to validate:
1. **Order** (Week 1):
   - 1× Raspberry Pi 4 kit - €87
   - 5× ESP32 DevKit - €25
   - 5× Capacitive sensors - €12
   - 5× USB power adapters - €25
   - Total: **€149**

2. **Build & Test** (Week 2-3):
   - Set up Pi 4 central hub
   - Flash 5 ESP32 nodes
   - Deploy to 5 different plant types
   - Monitor for 2 weeks

3. **Evaluate** (Week 4):
   - Does battery life work?
   - Is 4× per day enough?
   - Dashboard usability good?
   - Worth scaling to 25?

4. **Scale or Pivot** (Week 5+):
   - If successful: Order remaining 20 nodes
   - If issues: Adjust before scaling
   - Total investment so far: only €149

---

## Next Steps

1. **Review this architecture** - Does it fit your needs?
2. **Decide on ESP32 vs ESP8266** - Battery vs budget?
3. **Order starter kit (5 plants)** - Test before full commitment
4. **Read ESP32 code examples** - Understand the node logic

**Documentation:**
- [ESP32 Sensor Node Setup](./esp32-sensor-node-guide.md) (coming soon)
- [Central Pi 4 Configuration](./central-hub-setup.md) (coming soon)
- [Grafana Dashboard Templates](./grafana-templates/) (coming soon)

---

## Questions?

This architecture is **much better** for 25+ plants than the original Pi Zero approach.

**Key wins:**
- **5× cheaper** per plant
- **Battery powered** flexibility
- **Easier to scale** (just add nodes)
- **Central management** (one Pi to update, not 25)
- **Start small** (5 plants for €149)

Ready to order components? See [Netherlands ESP32 Shopping List](./shopping-list-netherlands-esp32.md)
