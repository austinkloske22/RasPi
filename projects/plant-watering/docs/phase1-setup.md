# Phase 1 Setup Guide - Single Plant Monitor

This guide walks through setting up your first plant monitoring system with manual watering control.

## Goals

By the end of this phase, you will:
- ✅ Read soil moisture from a sensor
- ✅ Manually control a water pump
- ✅ Log moisture data to a file
- ✅ Understand GPIO basics
- ✅ Build confidence for Phase 2 automation

## Prerequisites

### Hardware
- [ ] Raspberry Pi Zero 2 W (or any Pi model)
- [ ] MicroSD card with Raspberry Pi OS installed
- [ ] Capacitive soil moisture sensor
- [ ] 5V water pump
- [ ] Relay module (4-channel recommended)
- [ ] Power supply (5V 3A)
- [ ] Jumper wires (male-to-female)
- [ ] Water reservoir with tubing
- [ ] Test plant in pot

### Software
- [ ] Raspberry Pi OS (Bullseye or newer)
- [ ] Python 3.7+
- [ ] SSH or monitor/keyboard access

---

## Step 1: Raspberry Pi Setup

### 1.1 Install Raspberry Pi OS

If starting fresh:
```bash
# Download Raspberry Pi Imager
# https://www.raspberrypi.com/software/

# Flash OS to SD card
# Enable SSH and WiFi during setup
```

### 1.2 Initial Configuration

SSH into your Pi:
```bash
ssh pi@raspberrypi.local
# Default password: raspberry (change this!)
```

Update system:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip git
```

Enable GPIO:
```bash
# Should be enabled by default, verify:
ls /dev/gpiomem  # Should exist
```

---

## Step 2: Wiring

**⚠️ POWER OFF your Pi before wiring!**

### 2.1 Moisture Sensor Wiring

Capacitive sensor typically has 3 wires:
- **VCC** → Pi Pin 2 (5V)
- **GND** → Pi Pin 6 (Ground)
- **AOUT/DOUT** → Pi Pin 11 (GPIO 17)

### 2.2 Relay Module Wiring

Relay module (using channel 1):
- **VCC** → Pi Pin 4 (5V)
- **GND** → Pi Pin 9 (Ground)
- **IN1** → Pi Pin 13 (GPIO 27)

### 2.3 Pump Connection

Water pump to relay:
- **Pump +** → External 5V power supply +
- **Pump -** → Relay NO (Normally Open) terminal
- **Relay COM** → External 5V power supply -

**Note:** Relay switches the ground connection

### 2.4 Complete Wiring Diagram

```
Raspberry Pi Zero
┌─────────────────┐
│  1 [3.3V]       │
│  2 [5V] ────────┼──→ Sensor VCC
│  3              │
│  4 [5V] ────────┼──→ Relay VCC
│  5              │
│  6 [GND] ───────┼──→ Sensor GND
│  7              │
│  8              │
│  9 [GND] ───────┼──→ Relay GND
│ 10              │
│ 11 [GPIO17] ────┼──→ Sensor OUT
│ 12              │
│ 13 [GPIO27] ────┼──→ Relay IN1
│ ...             │
└─────────────────┘

Relay Module          Water Pump
┌──────────┐          ┌─────┐
│ NO  COM  │          │ +   │
│  |   |   │          │ -   │
└──┼───┼───┘          └──┼──┘
   |   |                 |
   |   └────External─────┘
   |        5V GND
   |
   └────────Pump -
```

See [detailed wiring diagram](../hardware/phase1-wiring.md) for photos

---

## Step 3: Software Setup

### 3.1 Clone Repository

```bash
cd ~
git clone https://github.com/yourusername/RasPi.git
cd RasPi/projects/plant-watering
```

### 3.2 Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 3.3 Configure Settings

```bash
cd config
cp config.example.json config.json
nano config.json
```

Adjust GPIO pins to match your wiring:
```json
{
  "sensor_pin": 17,
  "pump_pin": 27,
  "sensor_mode": "digital",
  "max_pump_runtime": 30,
  "log_file": "plant_data.log",
  "plant_name": "Living Room Pothos"
}
```

---

## Step 4: Testing

### 4.1 Test Moisture Sensor

```bash
cd ~/RasPi/projects/plant-watering/src/phase1
python3 moisture_sensor.py
```

**Expected output:**
```
Moisture Sensor Test
========================================
Sensor pin: GPIO 17
Press Ctrl+C to exit

Moisture: dry
Moisture: dry
Moisture: wet  # After touching sensor or putting in water
```

**Troubleshooting:**
- No output? Check wiring and GPIO pin number
- Always "dry"? Sensor might be in analog mode, needs ADC
- Always "wet"? Sensor might be inverted, check datasheet

### 4.2 Test Water Pump

**⚠️ IMPORTANT: Put pump in bucket of water first!**

```bash
python3 pump_control.py
```

Follow prompts to run test waterings.

**Expected behavior:**
- Hear relay click
- Pump runs for specified duration
- Pump stops automatically

**Troubleshooting:**
- Relay clicks but pump doesn't run? Check relay wiring (NO vs NC)
- Pump runs continuously? Pin may be inverted, check code
- No relay click? Verify relay power and GPIO pin

### 4.3 Test Combined System

```bash
python3 plant_monitor.py
```

Should display moisture readings every 5 minutes.

**Manual watering:**
- Not implemented in Phase 1 base code
- You can manually run: `python3 pump_control.py`

---

## Step 5: Deploy to Plant

### 5.1 Physical Setup

1. **Prepare reservoir:**
   - Fill with 2-3 liters of water
   - Insert pump submersed
   - Run tubing to plant pot

2. **Place sensor:**
   - Insert into soil 2-3 inches deep
   - Near plant roots
   - Not touching pot edge

3. **Test water flow:**
   - Run pump manually
   - Verify water reaches soil
   - Check for leaks

4. **Organize cables:**
   - Keep electronics dry and elevated
   - Secure loose wires
   - Label connections

### 5.2 Run Monitor

```bash
# Run in foreground for testing
python3 plant_monitor.py

# Or run in background
nohup python3 plant_monitor.py &
```

### 5.3 Run on Boot (Optional)

Create systemd service:
```bash
sudo nano /etc/systemd/system/plant-monitor.service
```

Add:
```ini
[Unit]
Description=Plant Monitor Phase 1
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/RasPi/projects/plant-watering/src/phase1
ExecStart=/usr/bin/python3 plant_monitor.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable:
```bash
sudo systemctl enable plant-monitor
sudo systemctl start plant-monitor
sudo systemctl status plant-monitor
```

---

## Step 6: Monitoring and Data

### 6.1 View Logs

```bash
cd ~/RasPi/projects/plant-watering/src/phase1
tail -f plant_data.log
```

Example log entry:
```json
{"timestamp": "2024-11-16T14:30:00", "type": "moisture", "value": "moist"}
{"timestamp": "2024-11-16T14:32:15", "type": "watering", "value": 5}
```

### 6.2 Analyze Data

```bash
# Count readings by type
grep moisture plant_data.log | wc -l

# View all watering events
grep watering plant_data.log
```

---

## Phase 1 Completion Checklist

- [ ] Sensor reads moisture correctly
- [ ] Pump activates on command
- [ ] Data logs to file
- [ ] System runs for 24 hours without issues
- [ ] You understand GPIO basics
- [ ] Comfortable with the hardware

---

## Next Steps

Ready for automation? Move to [Phase 2 Setup Guide](./phase2-setup.md):
- Automatic watering based on thresholds
- Web dashboard
- Scheduling and rules

---

## Troubleshooting

### Permission Errors
```bash
# Add user to GPIO group
sudo usermod -a -G gpio pi
# Logout and login again
```

### GPIO Already in Use
```bash
# Check what's using GPIO
sudo lsof /dev/gpiomem

# Kill conflicting process or reboot
sudo reboot
```

### Sensor Not Reading
1. Check voltage: should be 3.3-5V on VCC pin
2. Verify GPIO pin with multimeter
3. Test with different GPIO pin
4. Try analog mode if available

### Pump Not Working
1. Verify relay is clicking
2. Check relay is in NO mode (not NC)
3. Test pump directly with power supply
4. Verify external power supply amperage (2A+ recommended)

---

## Resources

- [Raspberry Pi GPIO Pinout](https://pinout.xyz)
- [RPi.GPIO Documentation](https://sourceforge.net/projects/raspberry-gpio-python/)
- [Project Repository](https://github.com/yourusername/RasPi)

## Questions?

Document issues in your project journal or repository issues page.
