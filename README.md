# RasPi Smart Home

A collection of Raspberry Pi projects for home automation, starting with an automatic plant watering system.

## Project Philosophy

**Start Simple, Scale Smart**
- Begin with single-device projects to learn the fundamentals
- Build modular, reusable components
- Scale to multi-node distributed systems
- Document everything for future reference

## Current Projects

### 🌱 [Automatic Plant Watering System](./projects/plant-watering/)

**Status:** In Development - Phase 1

**Goal:** Build a distributed plant watering system that monitors soil moisture and automatically waters plants across multiple locations in the home.

**Phased Approach:**
- **Phase 1:** Single plant with manual controls (Learning phase)
- **Phase 2:** Automated single plant with web dashboard
- **Phase 3:** 3-plant multi-node system with MQTT communication
- **Phase 4:** Scale to unlimited plants with advanced features

See [Plant Watering Project](./projects/plant-watering/README.md) for details.

## Repository Structure

```
RasPi/
├── docs/                      # Documentation
│   ├── hardware/             # Hardware specs & setup guides
│   ├── projects/             # Project-specific documentation
│   └── getting-started/      # Raspberry Pi setup tutorials
├── projects/
│   ├── plant-watering/       # Automatic plant watering system
│   └── common/               # Shared libraries & utilities
├── infrastructure/           # Network setup, MQTT broker, etc.
├── hardware-inventory/       # Component tracking & shopping lists
└── examples/                 # Learning examples & quick starts
```

## Technology Stack

**Hardware:**
- Raspberry Pi Zero W (sensor nodes)
- Raspberry Pi 4 (central controller)
- Various sensors and actuators

**Software:**
- **Language:** Python 3
- **Communication:** MQTT (Mosquitto broker)
- **Web Interface:** Flask or Node-RED
- **Database:** SQLite / InfluxDB
- **Version Control:** Git

## Getting Started

1. **Hardware Setup:** See [docs/getting-started/](./docs/getting-started/)
2. **Choose a Project:** Browse [projects/](./projects/)
3. **Follow Project Guide:** Each project has its own README with setup instructions

## Documentation

- [Raspberry Pi Initial Setup](./docs/getting-started/raspberry-pi-setup.md)
- [Hardware Inventory](./hardware-inventory/README.md)
- [Common Libraries](./projects/common/README.md)

## Contributing

This is a personal learning project, but feel free to fork and adapt for your own use!

## License

MIT License - Feel free to use and modify for your own projects.
