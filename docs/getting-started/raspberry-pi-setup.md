# Raspberry Pi Initial Setup Guide

Quick start guide for setting up a fresh Raspberry Pi for smart home projects.

## What You'll Need

- Raspberry Pi (any model)
- MicroSD card (16GB minimum, 32GB recommended)
- Power supply (5V 2.5A minimum, 3A recommended)
- Computer with SD card reader
- WiFi network credentials

## Step 1: Flash Raspberry Pi OS

### Download Raspberry Pi Imager

**Windows/Mac/Linux:**
- Download from: https://www.raspberrypi.com/software/
- Install and run

### Flash the OS

1. **Choose OS:**
   - Click "Choose OS"
   - Select "Raspberry Pi OS Lite (64-bit)" for headless setup
   - Or "Raspberry Pi OS (64-bit)" for desktop

2. **Choose Storage:**
   - Insert microSD card
   - Click "Choose Storage"
   - Select your SD card

3. **Advanced Options (IMPORTANT):**
   - Click the gear icon ⚙️
   - Configure:
     - ✅ **Set hostname:** `raspberrypi` (or custom name)
     - ✅ **Enable SSH:** Use password authentication
     - ✅ **Set username/password:**
       - Username: `pi` (or custom)
       - Password: (choose secure password)
     - ✅ **Configure WiFi:**
       - SSID: Your network name
       - Password: Your WiFi password
       - Country: Your country code
     - ✅ **Set locale:**
       - Timezone: Your timezone
       - Keyboard: Your layout

4. **Write:**
   - Click "Write"
   - Wait for completion (5-10 minutes)

## Step 2: First Boot

1. **Insert SD card** into Raspberry Pi
2. **Connect power** - Pi will boot automatically
3. **Wait 1-2 minutes** for first boot and WiFi connection

## Step 3: Connect via SSH

### Find Pi IP Address

**Option A: Use hostname (easiest)**
```bash
ssh pi@raspberrypi.local
# Use the hostname you set earlier
```

**Option B: Find IP on router**
- Check your router's connected devices
- Look for "raspberrypi"

**Option C: Scan network**
```bash
# Install nmap if needed
sudo apt install nmap

# Scan your network (adjust subnet)
nmap -sn 192.168.1.0/24 | grep raspberry
```

### SSH Connection

```bash
ssh pi@raspberrypi.local
# Or: ssh pi@192.168.1.XXX

# Accept fingerprint (first time)
# Enter password you set
```

## Step 4: Initial Configuration

### Update System

```bash
# Update package lists
sudo apt update

# Upgrade all packages (takes 5-10 minutes)
sudo apt upgrade -y

# Install essential tools
sudo apt install -y git python3-pip vim
```

### Configure Pi Settings

```bash
sudo raspi-config
```

**Recommended settings:**
- Interface Options → Enable I2C (for some sensors)
- Interface Options → Enable SPI (for some sensors)
- Localization → Set timezone
- Advanced → Expand Filesystem (if not auto-expanded)

**Reboot after changes:**
```bash
sudo reboot
```

### Setup Git

```bash
# Configure git
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Generate SSH key for GitHub (optional)
ssh-keygen -t ed25519 -C "your@email.com"
cat ~/.ssh/id_ed25519.pub
# Copy and add to GitHub: Settings → SSH Keys
```

## Step 5: Security Hardening

### Change Default Password

```bash
passwd
# Enter current password
# Enter new password twice
```

### Create Swap File (for Pi Zero/Low RAM)

```bash
# Check current swap
free -h

# Create 1GB swap
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile
# Change CONF_SWAPSIZE=100 to CONF_SWAPSIZE=1024

sudo dphys-swapfile setup
sudo dphys-swapfile swapon
```

### Disable Unnecessary Services (optional)

```bash
# Disable Bluetooth if not needed
sudo systemctl disable bluetooth
sudo systemctl stop bluetooth

# Disable HDMI (saves power on headless)
sudo /usr/bin/tvservice -o
# Add to /etc/rc.local for persistent
```

## Step 6: Install Python Dependencies

### Update pip

```bash
# Upgrade pip
python3 -m pip install --upgrade pip

# Install common libraries
pip3 install RPi.GPIO
```

### Test GPIO

```python
# Test GPIO access
python3 << EOF
try:
    import RPi.GPIO as GPIO
    print("GPIO library working!")
    GPIO.setmode(GPIO.BCM)
    print("GPIO setup successful!")
except Exception as e:
    print(f"Error: {e}")
EOF
```

## Step 7: Project-Specific Setup

Now proceed to your specific project setup:

- [Plant Watering System Phase 1](../../projects/plant-watering/docs/phase1-setup.md)
- Other projects (coming soon)

## Common Issues

### Can't Connect via SSH

**Check:**
1. Pi is powered on (green LED should blink)
2. WiFi credentials are correct
3. Pi is on same network as your computer
4. SSH is enabled in advanced options
5. Try IP address instead of hostname

**Debug:**
```bash
# Ping the Pi
ping raspberrypi.local

# Check SSH service on Pi (need keyboard/monitor)
sudo systemctl status ssh
```

### WiFi Not Connecting

1. Check SSID and password are correct
2. Verify 2.4GHz network (Pi Zero W doesn't support 5GHz)
3. Check WiFi country code is set
4. Re-flash SD card with correct settings

### Permission Denied on GPIO

```bash
# Add user to gpio group
sudo usermod -a -G gpio $USER

# Logout and login
logout
```

### SD Card Corruption

**Prevention:**
- Always shutdown properly: `sudo shutdown now`
- Use quality SD card (SanDisk, Samsung)
- Enable read-only root (advanced)

**Recovery:**
- Reflash SD card
- Backup important files regularly

## Useful Commands

```bash
# System info
uname -a                    # Kernel version
cat /etc/os-release         # OS version
vcgencmd measure_temp       # CPU temperature
free -h                     # Memory usage
df -h                       # Disk usage

# Network
ifconfig                    # IP addresses
iwconfig                    # WiFi status
ping google.com            # Test internet

# GPIO
gpio readall               # GPIO pin status (requires wiringpi)

# Services
sudo systemctl status service_name    # Check service
sudo systemctl restart service_name   # Restart service
sudo journalctl -u service_name       # View logs

# Power
sudo shutdown now          # Shutdown
sudo reboot               # Restart
```

## Next Steps

✅ Pi is ready! Proceed to:
1. [Power Options Guide](../hardware/power-options.md)
2. [Plant Watering Phase 1 Setup](../../projects/plant-watering/docs/phase1-setup.md)
3. [Grafana Stack Integration](../projects/grafana-integration.md) (Phase 2)

## Resources

- [Official Documentation](https://www.raspberrypi.com/documentation/)
- [GPIO Pinout Reference](https://pinout.xyz)
- [Raspberry Pi Forums](https://forums.raspberrypi.com/)
