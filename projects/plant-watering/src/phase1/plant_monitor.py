#!/usr/bin/env python3
"""
Plant Monitor - Phase 1
Combined moisture monitoring and manual watering control
"""

import time
import json
from datetime import datetime
from pathlib import Path

from moisture_sensor import MoistureSensor
from pump_control import WaterPump


class PlantMonitor:
    """
    Monitor single plant and provide manual watering control

    Features:
    - Continuous moisture monitoring
    - Manual watering trigger
    - Data logging to file
    - Status display
    """

    def __init__(self, config_file='config.json'):
        """
        Initialize plant monitor

        Args:
            config_file: Path to configuration file
        """
        self.config = self.load_config(config_file)

        # Initialize hardware
        self.sensor = MoistureSensor(
            pin=self.config['sensor_pin'],
            mode=self.config.get('sensor_mode', 'digital')
        )

        self.pump = WaterPump(
            relay_pin=self.config['pump_pin'],
            max_runtime=self.config.get('max_pump_runtime', 30)
        )

        # Setup logging
        self.log_file = Path(self.config.get('log_file', 'plant_data.log'))

    def load_config(self, config_file):
        """Load configuration from JSON file"""
        config_path = Path(config_file)

        if config_path.exists():
            with open(config_path, 'r') as f:
                return json.load(f)
        else:
            # Default configuration
            print(f"Config file not found, using defaults")
            return {
                'sensor_pin': 17,
                'pump_pin': 27,
                'sensor_mode': 'digital',
                'max_pump_runtime': 30,
                'log_file': 'plant_data.log'
            }

    def read_moisture(self):
        """Read current moisture level"""
        return self.sensor.get_status()

    def water_plant(self, duration=5):
        """
        Manually water the plant

        Args:
            duration: Watering duration in seconds
        """
        print(f"\n💧 Watering plant for {duration} seconds...")
        self.pump.water(duration)
        self.log_event('watering', duration)

    def log_event(self, event_type, value=None):
        """
        Log event to file

        Args:
            event_type: 'moisture' or 'watering'
            value: Event value (moisture status or duration)
        """
        timestamp = datetime.now().isoformat()
        log_entry = {
            'timestamp': timestamp,
            'type': event_type,
            'value': value
        }

        with open(self.log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')

    def monitor_loop(self, interval=300):
        """
        Main monitoring loop

        Args:
            interval: Seconds between readings (default: 5 minutes)
        """
        print("=" * 50)
        print("🌱 Plant Monitor - Phase 1")
        print("=" * 50)
        print(f"Sensor pin: GPIO {self.config['sensor_pin']}")
        print(f"Pump pin: GPIO {self.config['pump_pin']}")
        print(f"Log file: {self.log_file}")
        print(f"Reading interval: {interval}s")
        print("\nCommands:")
        print("  w <duration> - Water plant (e.g., 'w 5' for 5 seconds)")
        print("  Ctrl+C - Exit")
        print("=" * 50)
        print()

        try:
            while True:
                # Read moisture
                moisture = self.read_moisture()
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Display status
                status_emoji = {
                    'wet': '💧',
                    'moist': '✓',
                    'dry': '⚠️'
                }.get(moisture, '?')

                print(f"[{timestamp}] Moisture: {status_emoji} {moisture.upper()}")

                # Log reading
                self.log_event('moisture', moisture)

                # Wait for next reading
                time.sleep(interval)

        except KeyboardInterrupt:
            print("\n\nShutting down...")

        finally:
            self.cleanup()

    def cleanup(self):
        """Clean up resources"""
        print("Cleaning up GPIO...")
        self.sensor.cleanup()
        self.pump.cleanup()
        print("Goodbye!")


def main():
    """Main entry point"""
    monitor = PlantMonitor()

    # Run monitoring loop (check every 5 minutes)
    monitor.monitor_loop(interval=300)


if __name__ == '__main__':
    main()
