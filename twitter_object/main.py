import RPi.GPIO as gpio
import pyaudio
import time
from record import Recorder
import string
import urllib
import datetime
import speech_recognition as sr
import tweepy
import re
from tweet import TweetThis


gpio.setmode(gpio.BCM)
gpio.setwarnings(False) # Ignore warning for now
gpio.setup(4, gpio.OUT)  # LED == 4 in BCM
gpio.output(4, False)  # Set output to off
gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)


class ButtonRecorderPlayer(object):
    def __init__(self):
        self.isRecording = False
        self.p = pyaudio
        self.rec = Recorder(channels=1)
        self.filename = ''
        self.t = TweetThis(filename = self.filename)

    def on_button(self, channel):
        print('button')
        if not recPlayBtn.isRecording:
            recPlayBtn.start_recording()
            recPlayBtn.isRecording = True
            time.sleep(1);
        else:
            recPlayBtn.stop_recording()
            recPlayBtn.isRecording = False
            gpio.remove_event_detect(17)
            recPlayBtn.listen();
            time.sleep(1);

    def listen(self):
        gpio.add_event_detect(17, gpio.FALLING, callback=recPlayBtn.on_button, bouncetime=100)
        print ('listening')

    def start_recording(self, channel=1):
        print ('recording, click to stop recording')
        timestr = time.strftime("%Y%m%d-%H%M%S")
        gpio.output(4, True) #LED on
        self.filename = 'twitter_recordings/' + timestr + '.wav'
        self.recfile = self.rec.open(self.filename, self.p, 'wb')
        self.recfile.start_recording()

    def stop_recording(self, channel=1):
        self.recfile.stop_recording()
        self.recfile.close()
        gpio.output(4, False) #LED on
        print ('recording stopped')
        print ('tweeting', self.filename)
        self.t.start(self.filename);
        time.sleep(1);

recPlayBtn = ButtonRecorderPlayer()
recPlayBtn.listen();

try:
    input()
except KeyboardInterrupt:
    pass

#exit if invalid state
gpio.cleanup()
