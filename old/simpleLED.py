import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False) # Ignore warning for now
gpio.setup(4, gpio.OUT)  # LED == 4 in BCM
gpio.output(4, False)  # Set output to off

while True:
    time.sleep(2)
    gpio.output(4, True) #LED on
    time.sleep(2)
    gpio.output(4, False) #LED off

#exit if invalid state
gpio.cleanup()
