# Grafana Stack Integration

Using Grafana stack for plant monitoring dashboards and alerting.

## Stack Components

### Phase 2: Basic Monitoring
```
Raspberry Pi → InfluxDB → Grafana
                    ↓
              Alertmanager
```

### Phase 3: Multi-Node
```
Sensor Nodes (3x Pi Zero)
    ↓ (MQTT)
Central Controller (Pi 4)
    ├→ Mosquitto MQTT Broker
    ├→ MQTT → InfluxDB Bridge
    ├→ InfluxDB (time-series DB)
    ├→ Grafana (dashboards)
    └→ Alertmanager (notifications)
```

---

## Phase 2: Single Plant Grafana Setup

### Components:
- **InfluxDB 2.x** - Time-series database for sensor data
- **Grafana** - Visualization and dashboards
- **Telegraf** (optional) - Metrics collection agent

### Installation on Raspberry Pi

#### 1. Install InfluxDB

```bash
# Add InfluxDB repository
wget -q https://repos.influxdata.com/influxdata-archive_compat.key
echo '23a1c8836f0afc5ed24e0486339d7cc8f6790b83886c4c96995b88a061c5bb5d influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null
echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list

# Install
sudo apt update
sudo apt install influxdb2 -y

# Start service
sudo systemctl start influxdb
sudo systemctl enable influxdb

# Initial setup
influx setup
# Creates: org, bucket, token
```

#### 2. Install Grafana

```bash
# Add Grafana repository
sudo apt-get install -y software-properties-common
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list

# Install
sudo apt update
sudo apt install grafana -y

# Start service
sudo systemctl start grafana-server
sudo systemctl enable grafana-server

# Access: http://raspberrypi.local:3000
# Default login: admin/admin
```

#### 3. Configure Data Source

In Grafana UI:
1. Configuration → Data Sources → Add InfluxDB
2. Configure:
   - **Query Language:** Flux
   - **URL:** http://localhost:8086
   - **Organization:** (from influx setup)
   - **Token:** (from influx setup)
   - **Default Bucket:** plant_data

---

## Python Integration

### Updated Code Structure

```python
# src/phase2/influx_logger.py
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

class InfluxLogger:
    def __init__(self, url, token, org, bucket):
        self.client = InfluxDBClient(url=url, token=token, org=org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.bucket = bucket
        self.org = org

    def log_moisture(self, value, status, plant_name="plant1"):
        """Log moisture reading to InfluxDB"""
        point = Point("moisture") \
            .tag("plant", plant_name) \
            .field("value", value) \
            .field("status", status)

        self.write_api.write(bucket=self.bucket, org=self.org, record=point)

    def log_watering(self, duration, plant_name="plant1"):
        """Log watering event"""
        point = Point("watering") \
            .tag("plant", plant_name) \
            .field("duration", duration)

        self.write_api.write(bucket=self.bucket, org=self.org, record=point)

    def log_system(self, cpu_temp, memory_used, plant_name="plant1"):
        """Log system metrics"""
        point = Point("system") \
            .tag("plant", plant_name) \
            .field("cpu_temp", cpu_temp) \
            .field("memory_used", memory_used)

        self.write_api.write(bucket=self.bucket, org=self.org, record=point)
```

### Updated Requirements

```txt
influxdb-client>=1.36.0
python-dotenv>=1.0.0  # For credentials
```

---

## Grafana Dashboards

### Dashboard 1: Plant Health Overview

**Panels:**
1. **Current Moisture Level** (Gauge)
   - Shows real-time moisture %
   - Color thresholds: <30% red, 30-70% yellow, >70% green

2. **Moisture History** (Time Series)
   - Last 24 hours / 7 days / 30 days
   - Line graph with threshold markers

3. **Watering Events** (Bar Chart)
   - Show when plant was watered
   - Duration of each watering

4. **System Health** (Stat panels)
   - Pi CPU temperature
   - Memory usage
   - Uptime

**Flux Query Example:**
```flux
from(bucket: "plant_data")
  |> range(start: -24h)
  |> filter(fn: (r) => r["_measurement"] == "moisture")
  |> filter(fn: (r) => r["plant"] == "plant1")
  |> aggregateWindow(every: 5m, fn: mean)
```

---

### Dashboard 2: Multi-Plant Overview (Phase 3)

**Panels:**
1. **All Plants Status** (Table)
   - Plant name, current moisture, last watered, status

2. **Moisture Comparison** (Multi-line Time Series)
   - All plants on same graph
   - Color-coded by plant

3. **Watering Schedule** (Heatmap)
   - When each plant was watered
   - Identify patterns

---

## Alerting

### Alertmanager Setup (Phase 2)

```bash
# Install Alertmanager
sudo apt install prometheus-alertmanager -y

# Start service
sudo systemctl start prometheus-alertmanager
sudo systemctl enable prometheus-alertmanager
```

### Configure Grafana Alerts

**Alert Rule: Soil Too Dry**

```yaml
# In Grafana UI: Alerting → Alert Rules → New Alert

# Condition:
# WHEN avg() OF moisture
# IS BELOW 30
# FOR 30 minutes

# Notification:
# Send to: Email / Slack / Discord / Telegram
```

**Alert Rule: Water Reservoir Low**

```yaml
# WHEN avg() OF water_level
# IS BELOW 20
# FOR 5 minutes
```

**Alert Rule: System Offline**

```yaml
# WHEN last() OF system.uptime
# HAS NO DATA FOR 10 minutes
```

---

## Notification Channels

### Email Notifications

```bash
# In Grafana UI:
# Alerting → Contact Points → New Contact Point

# Type: Email
# Addresses: your@email.com
# Test and save
```

### Telegram Bot (Recommended)

```bash
# 1. Create bot with @BotFather on Telegram
# 2. Get bot token
# 3. Get your chat ID

# In Grafana:
# Contact Point → Telegram
# Bot Token: YOUR_BOT_TOKEN
# Chat ID: YOUR_CHAT_ID
```

### Discord Webhook

```bash
# 1. Create Discord webhook in server settings
# 2. Copy webhook URL

# In Grafana:
# Contact Point → Discord
# Webhook URL: YOUR_WEBHOOK_URL
```

---

## Phase 3: Multi-Node Architecture

### Data Flow

```
Sensor Node 1 (Pi Zero W)
├─ Read moisture every 5 min
├─ Publish to MQTT: plant/1/moisture
└─ Subscribe to: plant/1/water

Sensor Node 2, 3... (same pattern)

Central Controller (Pi 4)
├─ Mosquitto MQTT Broker
├─ MQTT → InfluxDB Bridge
│   └─ Subscribe to: plant/+/moisture
│       plant/+/watering
├─ InfluxDB (store all data)
└─ Grafana (visualize all plants)
```

### MQTT to InfluxDB Bridge

```python
# src/phase3/mqtt_influx_bridge.py
import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point

class MQTTInfluxBridge:
    def __init__(self, mqtt_broker, influx_url, influx_token, influx_org, influx_bucket):
        # MQTT setup
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect(mqtt_broker, 1883, 60)

        # InfluxDB setup
        self.influx_client = InfluxDBClient(url=influx_url, token=influx_token, org=influx_org)
        self.write_api = self.influx_client.write_api(write_options=SYNCHRONOUS)
        self.bucket = influx_bucket
        self.org = influx_org

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected to MQTT broker with code {rc}")
        # Subscribe to all plant topics
        client.subscribe("plant/+/moisture")
        client.subscribe("plant/+/watering")
        client.subscribe("plant/+/system")

    def on_message(self, client, userdata, msg):
        # Parse topic: plant/1/moisture
        parts = msg.topic.split('/')
        plant_id = parts[1]
        metric = parts[2]

        # Parse payload
        value = float(msg.payload.decode())

        # Write to InfluxDB
        point = Point(metric) \
            .tag("plant_id", plant_id) \
            .field("value", value)

        self.write_api.write(bucket=self.bucket, org=self.org, record=point)
        print(f"Logged {metric} for plant {plant_id}: {value}")

    def run(self):
        self.mqtt_client.loop_forever()
```

---

## Learning Resources

### Grafana Mastery Path:
1. **Basics:**
   - InfluxDB fundamentals
   - Flux query language
   - Panel creation

2. **Intermediate:**
   - Alert rules
   - Notification channels
   - Variables and templating

3. **Advanced:**
   - Custom plugins
   - Provisioning (config as code)
   - High availability setup

### Useful Docs:
- [Grafana Documentation](https://grafana.com/docs/grafana/latest/)
- [InfluxDB Flux Language](https://docs.influxdata.com/flux/)
- [Grafana Alerting](https://grafana.com/docs/grafana/latest/alerting/)

---

## Cost Analysis

All components are **free and open source**:
- ✅ InfluxDB OSS (unlimited data retention)
- ✅ Grafana OSS (unlimited dashboards)
- ✅ Mosquitto MQTT (unlimited connections)
- ✅ Alertmanager (unlimited alerts)

**Resource Usage on Pi 4:**
- InfluxDB: ~200MB RAM
- Grafana: ~150MB RAM
- Mosquitto: ~10MB RAM
- **Total: ~360MB** (fine for 2GB+ Pi)

**Not recommended for Pi Zero** (use central Pi 4 for stack)

---

## Implementation Timeline

### Phase 2 (Current plant + Grafana):
- Week 1: Install InfluxDB + Grafana
- Week 2: Migrate logging to InfluxDB
- Week 3: Build dashboards
- Week 4: Setup alerts

### Phase 3 (3 plants + MQTT):
- Week 1: Setup MQTT broker
- Week 2: Convert nodes to MQTT
- Week 3: Build MQTT→InfluxDB bridge
- Week 4: Multi-plant dashboard

---

## Next Steps

1. Complete Phase 1 hardware testing
2. Install Grafana stack on Pi
3. Create first InfluxDB bucket
4. Build basic dashboard
5. Setup first alert (dry soil)

See [Phase 2 Setup Guide](../../projects/plant-watering/docs/phase2-setup.md) for detailed steps.
