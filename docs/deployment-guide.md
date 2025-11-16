# Code Deployment Guide

Complete guide for deploying code to your Raspberry Pi IoT devices from development to production.

## Deployment Overview

### Phase 1: Single Device Manual Deployment
- SSH + Git clone
- Manual testing
- Run scripts directly

### Phase 2: Automated Deployment
- Git pull updates
- Systemd services
- Auto-start on boot

### Phase 3: Multi-Device Fleet Management
- Ansible deployment
- Centralized updates
- Configuration management

---

## Prerequisites

Before deploying code:

- [ ] Raspberry Pi with OS installed ([Setup Guide](./getting-started/raspberry-pi-setup.md))
- [ ] SSH access configured
- [ ] WiFi connected
- [ ] Git installed on Pi
- [ ] GitHub access configured (optional but recommended)

---

## Phase 1: Manual Deployment (Single Device)

**Use for:** Initial testing, Phase 1 learning, quick iterations

### Step 1: Prepare Your Development Machine

```bash
# Clone the repository locally (if not already done)
git clone https://github.com/austinkloske22/RasPi.git
cd RasPi

# Make changes and test locally
# Edit files in projects/plant-watering/src/phase1/

# Commit your changes
git add .
git commit -m "Update plant monitoring code"
git push origin main
```

### Step 2: Deploy to Raspberry Pi

**Method A: Git Clone (First Time)**

```bash
# SSH into your Raspberry Pi
ssh pi@raspberrypi.local
# Or: ssh pi@192.168.1.XXX

# Clone the repository
cd ~
git clone https://github.com/austinkloske22/RasPi.git

# Navigate to project
cd RasPi/projects/plant-watering

# Install dependencies
pip3 install -r requirements.txt

# Configure settings
cd config
cp config.example.json config.json
nano config.json
# Edit GPIO pins to match your wiring

# Test the code
cd ../src/phase1
python3 moisture_sensor.py
```

**Method B: Git Pull (Updates)**

```bash
# SSH into Pi
ssh pi@raspberrypi.local

# Pull latest changes
cd ~/RasPi
git pull origin main

# Test updated code
cd projects/plant-watering/src/phase1
python3 plant_monitor.py
```

---

## Phase 1: Quick Deploy Script

Create a script to streamline deployment:

### On Your Development Machine

Create `deploy-phase1.sh`:

```bash
#!/bin/bash
# Quick deployment script for Phase 1

PI_HOST="pi@raspberrypi.local"
REPO_PATH="~/RasPi"

echo "Deploying to $PI_HOST..."

# Push latest code to GitHub
git push origin main

# SSH and pull on Pi
ssh $PI_HOST << 'EOF'
  cd ~/RasPi
  echo "Pulling latest code..."
  git pull origin main

  echo "Installing dependencies..."
  cd projects/plant-watering
  pip3 install -r requirements.txt

  echo "Restarting service (if running)..."
  sudo systemctl restart plant-monitor || echo "Service not configured yet"

  echo "Deployment complete!"
EOF

echo "Done! Checking status..."
ssh $PI_HOST "cd ~/RasPi/projects/plant-watering/src/phase1 && python3 -c 'import moisture_sensor; import pump_control; print(\"✓ Modules imported successfully\")'"
```

Make it executable:
```bash
chmod +x deploy-phase1.sh
```

Run deployment:
```bash
./deploy-phase1.sh
```

---

## Phase 2: Systemd Service Deployment

**Use for:** Production deployment, auto-start on boot, Phase 2-3

### Step 1: Create Systemd Service File

On the Raspberry Pi:

```bash
# Create service file
sudo nano /etc/systemd/system/plant-monitor.service
```

Add this content:

```ini
[Unit]
Description=Plant Watering Monitor
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/RasPi/projects/plant-watering/src/phase1
ExecStart=/usr/bin/python3 plant_monitor.py
Restart=always
RestartSec=10
StandardOutput=append:/var/log/plant-monitor.log
StandardError=append:/var/log/plant-monitor-error.log

# Environment variables (if needed)
Environment="PYTHONUNBUFFERED=1"

[Install]
WantedBy=multi-user.target
```

### Step 2: Enable and Start Service

```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable service (start on boot)
sudo systemctl enable plant-monitor

# Start service now
sudo systemctl start plant-monitor

# Check status
sudo systemctl status plant-monitor
```

### Step 3: Service Management Commands

```bash
# View logs
sudo journalctl -u plant-monitor -f

# Restart service
sudo systemctl restart plant-monitor

# Stop service
sudo systemctl stop plant-monitor

# Disable auto-start
sudo systemctl disable plant-monitor

# View latest logs
tail -f /var/log/plant-monitor.log
```

---

## Phase 2: Automated Deployment Script

Create `deploy-phase2.sh` for service-based deployment:

```bash
#!/bin/bash
# Automated deployment with service restart

PI_HOST="pi@raspberrypi.local"
SERVICE_NAME="plant-monitor"

echo "=== Phase 2 Deployment ==="
echo "Target: $PI_HOST"
echo "Service: $SERVICE_NAME"
echo ""

# 1. Push code to GitHub
echo "[1/5] Pushing code to GitHub..."
git add .
git commit -m "Deploy $(date +%Y-%m-%d_%H:%M:%S)" || echo "No changes to commit"
git push origin main

# 2. Pull on Pi
echo "[2/5] Pulling code on Pi..."
ssh $PI_HOST "cd ~/RasPi && git pull origin main"

# 3. Install dependencies
echo "[3/5] Installing dependencies..."
ssh $PI_HOST "cd ~/RasPi/projects/plant-watering && pip3 install -r requirements.txt"

# 4. Restart service
echo "[4/5] Restarting service..."
ssh $PI_HOST "sudo systemctl restart $SERVICE_NAME"

# 5. Verify deployment
echo "[5/5] Verifying deployment..."
sleep 3
ssh $PI_HOST "sudo systemctl is-active $SERVICE_NAME && echo '✓ Service running' || echo '✗ Service failed!'"

echo ""
echo "=== Deployment Complete ==="
echo "View logs: ssh $PI_HOST 'sudo journalctl -u $SERVICE_NAME -f'"
```

---

## Phase 3: Multi-Device Fleet Deployment

**Use for:** Managing 3+ Raspberry Pi devices, Phase 3 multi-node

### Option 1: Simple SSH Loop

Create `deploy-fleet.sh`:

```bash
#!/bin/bash
# Deploy to multiple Raspberry Pi devices

# Define your Pi hostnames/IPs
FLEET=(
  "pi@plant-station-1.local"
  "pi@plant-station-2.local"
  "pi@plant-station-3.local"
)

# Push code to GitHub once
echo "Pushing code to GitHub..."
git push origin main

# Deploy to each Pi
for PI in "${FLEET[@]}"; do
  echo ""
  echo "======================================"
  echo "Deploying to: $PI"
  echo "======================================"

  ssh $PI << 'EOF'
    cd ~/RasPi
    git pull origin main
    cd projects/plant-watering
    pip3 install -r requirements.txt
    sudo systemctl restart plant-monitor
    sudo systemctl is-active plant-monitor && echo "✓ $HOSTNAME: Success" || echo "✗ $HOSTNAME: Failed"
EOF
done

echo ""
echo "Fleet deployment complete!"
```

### Option 2: Ansible Deployment (Advanced)

**Install Ansible:**
```bash
# On your development machine
pip3 install ansible
```

**Create inventory file** (`ansible/inventory.yml`):

```yaml
all:
  children:
    plant_stations:
      hosts:
        station1:
          ansible_host: plant-station-1.local
          ansible_user: pi
          plant_name: "Living Room Pothos"
        station2:
          ansible_host: plant-station-2.local
          ansible_user: pi
          plant_name: "Kitchen Fern"
        station3:
          ansible_host: plant-station-3.local
          ansible_user: pi
          plant_name: "Bedroom Snake Plant"
```

**Create playbook** (`ansible/deploy.yml`):

```yaml
---
- name: Deploy Plant Watering System
  hosts: plant_stations
  become: false

  tasks:
    - name: Update repository
      git:
        repo: https://github.com/austinkloske22/RasPi.git
        dest: ~/RasPi
        version: main
        update: yes

    - name: Install Python dependencies
      pip:
        requirements: ~/RasPi/projects/plant-watering/requirements.txt
        executable: pip3

    - name: Copy configuration
      template:
        src: config.json.j2
        dest: ~/RasPi/projects/plant-watering/config/config.json

    - name: Restart service
      systemd:
        name: plant-monitor
        state: restarted
        enabled: yes
      become: yes

    - name: Wait for service to start
      wait_for:
        timeout: 5

    - name: Check service status
      systemd:
        name: plant-monitor
      register: service_status
      become: yes

    - name: Display status
      debug:
        msg: "{{ inventory_hostname }}: {{ 'Running' if service_status.status.ActiveState == 'active' else 'Failed' }}"
```

**Run Ansible deployment:**

```bash
# Deploy to all stations
ansible-playbook -i ansible/inventory.yml ansible/deploy.yml

# Deploy to specific station
ansible-playbook -i ansible/inventory.yml ansible/deploy.yml --limit station1

# Check status of all stations
ansible plant_stations -i ansible/inventory.yml -m shell -a "systemctl status plant-monitor"
```

---

## Configuration Management

### Environment-Specific Configs

**Structure:**
```
config/
├── config.example.json       # Template
├── station1-config.json      # Living room
├── station2-config.json      # Kitchen
├── station3-config.json      # Bedroom
└── production-config.json    # Central controller
```

### Deployment with Config Selection

```bash
# Deploy specific config to specific Pi
scp config/station1-config.json pi@plant-station-1.local:~/RasPi/projects/plant-watering/config/config.json

# Or use deployment script with config parameter
./deploy.sh station1 config/station1-config.json
```

---

## Rollback Strategy

### Quick Rollback

```bash
# On Pi, rollback to previous commit
ssh pi@raspberrypi.local << 'EOF'
  cd ~/RasPi
  git log --oneline -5  # View recent commits
  git checkout HEAD~1   # Go back 1 commit
  sudo systemctl restart plant-monitor
EOF
```

### Tagged Releases

```bash
# On development machine, create release
git tag -a v1.0.0 -m "Phase 1 stable release"
git push origin v1.0.0

# On Pi, deploy specific version
cd ~/RasPi
git fetch --tags
git checkout v1.0.0
sudo systemctl restart plant-monitor
```

---

## Deployment Checklist

### Pre-Deployment

- [ ] Code tested locally (if possible)
- [ ] Changes committed to git
- [ ] Config files updated
- [ ] Dependencies documented in requirements.txt
- [ ] Backup of current working code (git tag)

### Deployment

- [ ] Push code to GitHub
- [ ] Pull code on Pi(s)
- [ ] Install/update dependencies
- [ ] Update configuration files
- [ ] Restart services
- [ ] Verify service status

### Post-Deployment

- [ ] Monitor logs for errors (first 5 minutes)
- [ ] Test basic functionality (sensor reading, pump control)
- [ ] Check Grafana dashboard (Phase 2+)
- [ ] Document any issues
- [ ] Update deployment log

---

## Monitoring Deployments

### Check Service Health

```bash
# Quick health check
ssh pi@raspberrypi.local 'systemctl is-active plant-monitor && echo "OK" || echo "FAILED"'

# Detailed status
ssh pi@raspberrypi.local 'systemctl status plant-monitor'

# Recent logs
ssh pi@raspberrypi.local 'journalctl -u plant-monitor --since "5 minutes ago"'

# Resource usage
ssh pi@raspberrypi.local 'top -b -n 1 | grep python3'
```

### Deployment Dashboard (Phase 3)

Create simple status script:

```bash
#!/bin/bash
# fleet-status.sh - Check all stations

STATIONS=("station1.local" "station2.local" "station3.local")

echo "=== Fleet Status ==="
echo ""

for STATION in "${STATIONS[@]}"; do
  echo -n "$STATION: "
  ssh pi@$STATION 'systemctl is-active plant-monitor' 2>/dev/null || echo "UNREACHABLE"
done
```

---

## Troubleshooting Deployments

### Common Issues

**1. Service Won't Start**
```bash
# Check logs for errors
sudo journalctl -u plant-monitor -n 50

# Test script manually
cd ~/RasPi/projects/plant-watering/src/phase1
python3 plant_monitor.py

# Check permissions
ls -la plant_monitor.py
```

**2. Git Pull Fails**
```bash
# Check git status
cd ~/RasPi
git status

# Stash local changes
git stash
git pull origin main
git stash pop

# Or reset to remote (CAUTION: loses local changes)
git fetch origin
git reset --hard origin/main
```

**3. Dependencies Missing**
```bash
# Reinstall all dependencies
pip3 install --force-reinstall -r requirements.txt

# Check Python version
python3 --version  # Should be 3.7+

# Verify specific package
pip3 show RPi.GPIO
```

**4. Permission Denied (GPIO)**
```bash
# Add user to gpio group
sudo usermod -a -G gpio pi

# Logout and login
logout
# Then SSH back in
```

---

## Best Practices

### 1. Version Control
- Always commit before deploying
- Use meaningful commit messages
- Tag stable releases
- Never edit code directly on Pi

### 2. Testing
- Test changes locally when possible
- Deploy to one station first (canary)
- Monitor for 10-15 minutes before fleet deployment
- Keep previous version accessible

### 3. Configuration
- Never commit secrets to git
- Use environment variables for sensitive data
- Keep config templates in repo
- Document all configuration options

### 4. Logging
- Always log important events
- Use systemd for service management
- Rotate logs to prevent disk fill
- Monitor logs actively after deployment

### 5. Backup
- Backup working SD card image
- Keep deployment log/changelog
- Document all manual changes
- Test restore procedure

---

## Deployment Automation Levels

| Level | Method | Complexity | Best For |
|-------|--------|------------|----------|
| **1 - Manual** | SSH + git pull | Low | Phase 1, learning |
| **2 - Script** | Bash script | Low-Med | Phase 1-2, single device |
| **3 - Service** | Systemd + script | Medium | Phase 2, production |
| **4 - Fleet** | Multi-SSH script | Medium | Phase 3, 2-5 devices |
| **5 - Ansible** | Ansible playbook | High | Phase 3, 5+ devices |
| **6 - CI/CD** | GitHub Actions | Very High | Production fleet |

**Recommendation:**
- **Phase 1:** Start with Level 1 (Manual)
- **Phase 2:** Move to Level 3 (Service)
- **Phase 3:** Use Level 4 (Fleet) or 5 (Ansible)

---

## Next Steps

1. **Set up first deployment:** Use Manual method for Phase 1
2. **Create systemd service:** When moving to Phase 2
3. **Write deployment script:** Save time on iterations
4. **Plan fleet deployment:** Before adding station 2 and 3

## Related Documentation

- [Raspberry Pi Setup](./getting-started/raspberry-pi-setup.md)
- [Phase 1 Setup Guide](../projects/plant-watering/docs/phase1-setup.md)
- [Grafana Integration](./projects/grafana-integration.md)
