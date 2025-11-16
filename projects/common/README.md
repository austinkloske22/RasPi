# Common Libraries

Shared utilities and modules used across multiple projects.

## Structure

```
common/
├── sensors/          # Reusable sensor interfaces
├── communication/    # MQTT, HTTP, etc.
└── utils/           # Helper functions
```

## Planned Modules

### Sensors (Phase 2+)
- `moisture_sensor.py` - Generic moisture sensor interface
- `temperature.py` - DHT22, DS18B20 support
- `water_level.py` - Float switch, ultrasonic

### Communication (Phase 3+)
- `mqtt_client.py` - MQTT pub/sub wrapper
- `influx_logger.py` - InfluxDB time-series logging
- `api_client.py` - REST API communication

### Utils (Phase 2+)
- `gpio_helper.py` - GPIO setup/cleanup utilities
- `config_loader.py` - JSON/YAML config management
- `logger.py` - Standardized logging

## Usage

Phase 1 doesn't use common libraries (self-contained learning).

Phase 2+ will refactor shared code here:

```python
# Example future usage
from common.sensors import MoistureSensor
from common.communication import InfluxLogger

sensor = MoistureSensor(pin=17)
logger = InfluxLogger(config)
```

## Contributing

When adding to common:
1. Make modules generic and reusable
2. Include docstrings and examples
3. Add tests (Phase 3+)
4. Update this README
