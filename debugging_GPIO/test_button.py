import os
from time import sleep
from os import listdir
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setup(7, GPIO.OUT)  # LED == 7
GPIO.output(7, False)  # Set output to off
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button == 11

def buttonCallback(channel):
    print('button!')
    ledstatus = GPIO.input(7)
    GPIO.output(7, not ledstatus)
    sleep(0.25)

GPIO.add_event_detect(11, GPIO.FALLING, callback=buttonCallback, bouncetime=100)

while True:
    print('do you want to press the button?')
    sleep(0.25)

GPIO.cleanup()
