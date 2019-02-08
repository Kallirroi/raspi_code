import os
from time import sleep
from os import listdir
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setup(7, GPIO.OUT)  # LED == 7
GPIO.output(7, False)  # Set output to off
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button == 11
playback_index = 0

# def updateFileList():
#     print("updating file list")
#     return [ f for f in listdir('./recordings' if f[-4:] == '.wav' ] # read files from the /audio/playback folder
# mp3_files = updateFileList()
# if not (len(mp3_files) > 0):
#     print("No mp3 files found!")

def buttonCallback(channel):
    if (GPIO.input(7) == False): # if the LED is not on, start recording
        print("started recording!")
        GPIO.output(7, True) #LED on
        # os.system('arecord -D plughw:1 -c 2 -f cd ./audio/playback/test.mp3')
    else:
        print("stopped recording!") # if the LED is on, then we were recording and have to stop.
        GPIO.output(7, False)
    # mp3_files = updateFileList()

GPIO.add_event_detect(11, GPIO.FALLING, callback=buttonCallback, bouncetime=100)

while True:
    # loop audio
    playback_index += 1
    # if playback_index >= len(mp3_files):
    #     playback_index = 0

    if GPIO.input(7) == False: #if not recording, you should be playing!
        print("playing: ")
        # os.system('omxplayer -o local ./audio/playback/'+mp3_files[playback_index] + ' &')
        sleep(1)
    else:
        print("recording")
        sleep(1)

    sleep(1)

GPIO.cleanup()
