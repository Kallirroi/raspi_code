import RPi.GPIO as gpio
import pyaudio
import time
from record import Recorder
from play import Player
# from pynput import mouse
# import threading

gpio.setmode(gpio.BCM)
gpio.setwarnings(False) # Ignore warning for now
gpio.setup(4, gpio.OUT)  # LED == 4 in BCM
gpio.output(4, False)  # Set output to off
gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)

class ButtonRecorderPlayer(object):
    def __init__(self):
        self.rec = Recorder(channels=1)
        self.play = Player()
        self.isPlaying = True
        self.p = pyaudio

    def on_click(self, channel):
        if self.isPlaying:
            # print('stoping playback and starting recording')
            self.stop_playback()
            self.start_recording()
            self.isPlaying = False
        else:
            # print('stoping recording and starting playback')
            self.stop_recording()
            self.start_playback()
            self.isPlaying = True

    def start(self):
        gpio.add_event_detect(17, gpio.FALLING, callback=recPlayBtn.on_click, bouncetime=10)
        self.start_playback()

    def start_recording(self, channel=1):
        print ('Recording, click to stop recording')
        timestr = time.strftime("%Y%m%d-%H%M%S")
        gpio.output(4, True) #LED on
        self.recfile = self.rec.open('recordings/' + timestr + '.wav', self.p, 'wb')
        self.recfile.start_recording()

    def stop_recording(self, channel=1):
        self.recfile.stop_recording()
        self.recfile.close()
        gpio.output(4, False) #LED on
        print ('Recording Stopped')


    def start_playback(self, channel=1):
        print ('playback starting')
        self.play.play('recordings', self.p)

    def stop_playback(self):
        self.play.stop()
        print ('playback stoped')

recPlayBtn = ButtonRecorderPlayer()
recPlayBtn.start()

try:
    input()
except KeyboardInterrupt:
    pass

#exit if invalid state
gpio.cleanup()
