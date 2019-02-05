import os
from time import sleep
from os import listdir
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setup(7, GPIO.OUT)  # LED == 7
GPIO.output(7, False)  # Set output to off
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Button == 11
playback_index = 0

def updateFileList():
    print("updating file list")
    return [ f for f in listdir('./audio/playback/') if f[-4:] == '.mp3' ]
mp3_files = updateFileList()
if not (len(mp3_files) > 0):
    print("No mp3 files found!")

def buttonCallback(channel):
    if (GPIO.input(7) == False):
        print("started recording!")
        # os.system('arecord -D plughw:1 --duration=10 -c 2 -f cd  ./audio/playback/testLED.mp3')
        os.system('arecord -D plughw:1 -c 2 -f cd ./audio/playback/testLED.mp3')
        GPIO.output(7, True) #LED on
        #kill omxplayer
    else:
        print("stopped recording!")
        GPIO.output(7, False)

    mp3_files = updateFileList()

GPIO.add_event_detect(11, GPIO.RISING, callback=buttonCallback, bouncetime=100)

while True:
    # loop audio
    playback_index += 1
    if playback_index >= len(mp3_files):
        playback_index = 0

    if not GPIO.input(11): #if button hasn't been pressed
        print("currently playing: "+mp3_files[playback_index])
        os.system('omxplayer -o local ./audio/playback/'+mp3_files[playback_index] + ' &')
        sleep(1)

GPIO.cleanup()
