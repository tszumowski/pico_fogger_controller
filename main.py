"""
micropython application for pi pico.
This application sets the on board LED high and activates a relay for X seconds.
It then sets it low and then sleeps for Y seconds.
Then it wakes up and repeats.

It also includes an interrupt on the sleep when the LED/relay is off. This is useful
for an external sensor
For example: a PIR body/motion sensor to activate it while sleeping.

"""
from machine import Pin
from machine import lightsleep
from time import sleep

"""
USER CONFIGURATION
"""
# How long to keep output enabled for, in seconds
ACTIVE_TIME = 5
# How long to deep sleep for, in seconds
SLEEP_TIME = 5

"""
STATIC CONFIGURATION
"""
RELAY_PIN = 0
INTERRUPT_PIN = 3
ON_BOARD_LED = 25

"""
CALLBACKS
"""
def callback(pin):
    print(f"Interrupted: {pin}")

"""
INITIALIZATION
"""
led = Pin(25, Pin.OUT)
relay_pin = Pin(RELAY_PIN, Pin.OUT)

# Initialize interrupt pin
interrupt_pin = Pin(INTERRUPT_PIN, Pin.IN, Pin.PULL_UP)
interrupt_pin.irq(trigger=Pin.IRQ_FALLING, handler=callback)

"""
MAIN LOOP
"""
while True:
    led.high()  # Turn on LED
    relay_pin.high()  # Turn on relay
    # Sleep for ACTIVE_TIME seconds. This sleep isn't interrupted by the interrupt pin.
    sleep(ACTIVE_TIME)
    led.low()  # Turn off LED
    relay_pin.low()  # Turn off relay
    # sleep for SLEEP_TIME seconds, allowing for interrupt to wake it up to loop early.
    lightsleep(SLEEP_TIME * 1000)
