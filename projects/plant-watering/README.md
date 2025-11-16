# Automatic Plant Watering System

A smart, distributed plant watering system that monitors soil moisture and automatically waters plants based on their needs.

## Project Phases

### Phase 1: Single Plant Learning System ⬅️ **YOU ARE HERE**

**Goals:**
- Learn basic GPIO control (sensors and pumps)
- Understand moisture sensor readings
- Build confidence with hardware interfacing
- Create reusable code modules

**Features:**
- Read moisture sensor data
- Manually trigger water pump via button or command
- Log sensor readings to file
- Simple LED indicator (dry/moist/wet)

**Hardware Required:**
- 1x Raspberry Pi Zero W (or any Pi model)
- 1x Capacitive soil moisture sensor
- 1x 5V water pump or solenoid valve
- 1x 5V relay module or MOSFET
- 1x Button (optional - for manual trigger)
- 1x LED + resistor (optional - for status indicator)
- Jumper wires
- Power supply (5V 2.5A recommended)
- Water reservoir/tubing

**Estimated Cost:** $40-60 (excluding Raspberry Pi)

---

### Phase 2: Smart Single Plant

**Features:**
- Automated watering based on moisture threshold
- Web dashboard (Flask) showing real-time data
- Configurable watering schedule (time windows)
- Water reservoir level monitoring
- Historical data logging (SQLite)

**Additional Hardware:**
- Water level sensor (float switch or ultrasonic)

---

### Phase 3: Multi-Node System (3 Plants)

**Goals:**
- Build distributed architecture
- Learn MQTT communication
- Create central control system

**Features:**
- 3 sensor nodes (Pi Zero W each) monitoring individual plants
- 1 central controller (Pi 4) running MQTT broker
- Centralized dashboard showing all plants
- Individual plant profiles and schedules
- Node health monitoring

**Architecture:**
```
Central Controller (Pi 4)
├── MQTT Broker (Mosquitto)
├── Web Dashboard
├── Database (InfluxDB)
└── Scheduling Engine

Sensor Nodes (3x Pi Zero W)
├── Moisture Sensor
├── Water Pump/Valve
├── MQTT Client
└── Local Control Logic
```

**Additional Hardware:**
- 2x additional Pi Zero W kits
- 2x additional sensor/pump sets

---

### Phase 4: Advanced Features

**Potential Additions:**
- Weather API integration (skip watering before rain)
- Plant type profiles (cacti vs ferns)
- Camera integration (timelapse growth monitoring)
- Mobile app with push notifications
- Fertilizer injection system
- pH and temperature monitoring
- ML-based watering optimization

## Getting Started

See the [Phase 1 Guide](./docs/phase1-setup.md) to begin building your first plant monitoring system.

## Project Structure

```
plant-watering/
├── hardware/              # Wiring diagrams, schematics
│   ├── phase1-wiring.md
│   └── schematics/
├── src/                   # Source code
│   ├── phase1/           # Single plant code
│   ├── phase2/           # Automated single plant
│   ├── phase3/           # Multi-node system
│   └── shared/           # Shared utilities
├── config/               # Configuration files
│   └── plant-profiles.json
└── docs/                 # Phase-specific documentation
    ├── phase1-setup.md
    ├── phase2-setup.md
    └── phase3-setup.md
```

## Documentation

- [Phase 1 Setup Guide](./docs/phase1-setup.md)
- [Hardware Shopping List](./hardware/shopping-list.md)
- [Wiring Diagrams](./hardware/phase1-wiring.md)
- [Troubleshooting](./docs/troubleshooting.md)

## Safety Notes

- **Water and Electronics:** Keep electronics in waterproof enclosures
- **Power:** Use proper 5V power supplies, avoid overloading
- **Relays:** Properly isolate high-voltage circuits if using AC pumps
- **Overflow:** Include overflow protection for water reservoirs
- **Testing:** Always test pumps with manual controls before automation

## Progress Tracking

- [x] Project planning and structure
- [ ] Phase 1: Hardware assembly
- [ ] Phase 1: Basic sensor reading
- [ ] Phase 1: Pump control
- [ ] Phase 1: Complete system test
- [ ] Phase 2: Automation logic
- [ ] Phase 2: Web dashboard
- [ ] Phase 3: Multi-node architecture
- [ ] Phase 3: MQTT implementation
