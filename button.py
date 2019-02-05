import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

def buttonCallback(channel):
    if (GPIO.input(10) == True):
        print("button click!")

# detects rising edge on button. ignores multiple rising edges in 100ms
GPIO.add_event_detect(10, GPIO.RISING, callback=buttonCallback, bouncetime=100)

while 1:
    # do some other stuff
    print("la la")
    sleep(1)

GPIO.cleanup()
