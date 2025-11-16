#!/usr/bin/env python3
"""
Water Pump Control Module - Phase 1
Controls water pump via relay or MOSFET
"""

import time
try:
    import RPi.GPIO as GPIO
except ImportError:
    print("Warning: RPi.GPIO not available (running on non-Pi system?)")
    GPIO = None


class WaterPump:
    """
    Control water pump via relay module

    Safety features:
    - Maximum runtime limit (prevent overflow)
    - Automatic shutoff
    - State tracking
    """

    def __init__(self, relay_pin, max_runtime=30):
        """
        Initialize water pump controller

        Args:
            relay_pin: GPIO pin number (BCM) connected to relay IN pin
            max_runtime: Maximum pump runtime in seconds (safety limit)
        """
        self.relay_pin = relay_pin
        self.max_runtime = max_runtime
        self.is_running = False

        if GPIO:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(relay_pin, GPIO.OUT)
            # Relay is active LOW (GPIO.LOW = ON, GPIO.HIGH = OFF)
            # Start with pump OFF
            GPIO.output(relay_pin, GPIO.HIGH)

    def turn_on(self):
        """Turn pump ON"""
        if not GPIO:
            print("[SIMULATION] Pump turned ON")
            self.is_running = True
            return

        print("Pump ON")
        GPIO.output(self.relay_pin, GPIO.LOW)  # Active LOW
        self.is_running = True

    def turn_off(self):
        """Turn pump OFF"""
        if not GPIO:
            print("[SIMULATION] Pump turned OFF")
            self.is_running = False
            return

        print("Pump OFF")
        GPIO.output(self.relay_pin, GPIO.HIGH)  # Active LOW
        self.is_running = False

    def water(self, duration):
        """
        Run pump for specified duration

        Args:
            duration: Runtime in seconds

        Raises:
            ValueError: If duration exceeds max_runtime
        """
        if duration > self.max_runtime:
            raise ValueError(
                f"Duration {duration}s exceeds safety limit {self.max_runtime}s"
            )

        print(f"Watering for {duration} seconds...")
        self.turn_on()
        time.sleep(duration)
        self.turn_off()
        print("Watering complete")

    def cleanup(self):
        """Ensure pump is off and clean up GPIO"""
        self.turn_off()
        if GPIO:
            GPIO.cleanup(self.relay_pin)


def main():
    """Test the water pump"""
    # Example: Relay connected to GPIO 27
    RELAY_PIN = 27

    print("Water Pump Control Test")
    print("=" * 40)
    print(f"Relay pin: GPIO {RELAY_PIN}")
    print("WARNING: Ensure pump is in water/bucket!")
    print()

    pump = WaterPump(RELAY_PIN, max_runtime=30)

    try:
        # Test 1: Short burst
        print("Test 1: 3-second watering")
        input("Press Enter to start...")
        pump.water(3)

        time.sleep(2)

        # Test 2: Longer watering
        print("\nTest 2: 5-second watering")
        input("Press Enter to start...")
        pump.water(5)

        print("\nTests complete!")

    except KeyboardInterrupt:
        print("\nInterrupted!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        pump.cleanup()


if __name__ == '__main__':
    main()
