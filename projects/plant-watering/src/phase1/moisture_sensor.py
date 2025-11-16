#!/usr/bin/env python3
"""
Moisture Sensor Module - Phase 1
Reads data from capacitive soil moisture sensor
"""

import time
try:
    import RPi.GPIO as GPIO
except ImportError:
    print("Warning: RPi.GPIO not available (running on non-Pi system?)")
    GPIO = None


class MoistureSensor:
    """
    Interface for capacitive soil moisture sensor

    The sensor outputs analog voltage (0-3.3V) that needs to be read
    via ADC (MCP3008) or digital pin if using comparator.
    """

    def __init__(self, pin, mode='digital'):
        """
        Initialize moisture sensor

        Args:
            pin: GPIO pin number (BCM numbering)
            mode: 'digital' or 'analog' (requires ADC for analog)
        """
        self.pin = pin
        self.mode = mode

        if GPIO:
            GPIO.setmode(GPIO.BCM)
            if mode == 'digital':
                GPIO.setup(pin, GPIO.IN)

    def read_digital(self):
        """
        Read digital moisture value (wet/dry)

        Returns:
            bool: True if wet, False if dry
        """
        if not GPIO:
            # Return dummy value for testing on non-Pi
            return True

        return GPIO.input(self.pin) == GPIO.HIGH

    def read_analog(self):
        """
        Read analog moisture value (0-100%)
        Requires MCP3008 ADC - see docs for wiring

        Returns:
            int: Moisture percentage (0-100)
        """
        # TODO: Implement MCP3008 ADC reading
        # For now, return placeholder
        raise NotImplementedError("Analog reading requires MCP3008 ADC setup")

    def get_status(self):
        """
        Get human-readable moisture status

        Returns:
            str: 'wet', 'moist', or 'dry'
        """
        if self.mode == 'digital':
            is_wet = self.read_digital()
            return 'wet' if is_wet else 'dry'
        else:
            moisture = self.read_analog()
            if moisture > 70:
                return 'wet'
            elif moisture > 30:
                return 'moist'
            else:
                return 'dry'

    def cleanup(self):
        """Clean up GPIO resources"""
        if GPIO:
            GPIO.cleanup(self.pin)


def main():
    """Test the moisture sensor"""
    # Example: Sensor connected to GPIO 17
    SENSOR_PIN = 17

    print("Moisture Sensor Test")
    print("=" * 40)
    print(f"Sensor pin: GPIO {SENSOR_PIN}")
    print("Press Ctrl+C to exit\n")

    sensor = MoistureSensor(SENSOR_PIN, mode='digital')

    try:
        while True:
            status = sensor.get_status()
            print(f"Moisture: {status}")
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nExiting...")

    finally:
        sensor.cleanup()


if __name__ == '__main__':
    main()
