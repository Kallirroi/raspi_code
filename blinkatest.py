# This script requires a Raspberry Pi 2, 3 or Zero. Circuit Python must
# be installed and it is strongly recommended that you use the latest
# release of Raspbian.

import time
import os
import board
import digitalio

button1 = digitalio.DigitalInOut(board.D17)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.D4)
led.direction = digitalio.Direction.OUTPUT

while True:
    if not button1.value:
        led.value = False
        print(led.value)
    else:
        led.value = True
        print(led.value)
    time.sleep(1)
