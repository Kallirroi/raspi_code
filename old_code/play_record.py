import os
import subprocess
from time import sleep
from os import listdir
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
playback_index = 0
recording_index = 0

def updateFileList():
    print("updating file list")
    return [ f for f in listdir('./audio/playback') if f[-4:] == '.mp3' ]
mp3_files = updateFileList()
print(mp3_files)
if not (len(mp3_files) > 0):
    print("No mp3 files found!")

def buttonCallback(recording_index):
    recording_index += 1
    print("recording message " + str(recording_index))
    os.system('omxplayer -o local ./audio/prompt.mp3 &')
    sleep(1)
    os.system('arecord -D plughw:1 --duration=10 -f cd -vv ./audio/playback/recording'+str(recording_index)+'.mp3')
    # os.system('arecord -D plughw:1 --duration=10 -f cd -vv ./audio/playback/recording.mp3')
    sleep(10)
    print("recorded successfully")
    mp3_files = updateFileList()

GPIO.add_event_detect(10, GPIO.RISING, callback=buttonCallback, bouncetime=100)


while True:
    # loop audio
    if playback_index >= len(mp3_files):
        playback_index = 0
    print("currently playing: "+mp3_files[playback_index])
    os.system('omxplayer -o local ./audio/playback/'+mp3_files[playback_index])
    sleep(10)
    playback_index += 1

GPIO.cleanup() # Clean up
