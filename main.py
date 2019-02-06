# import RPi.GPIO as gpio
import pyaudio
from record import Recorder
from play import Player
# gpio.setmode(gpio.BCM)

class ButtonRecorderPlayer(object):
    def __init__(self):
        # gpio.setup(23, gpio.IN, pull_up_down=gpio.PUD_UP)
        self.rec = Recorder(channels=1)
        self.play = Player()
        self.p = pyaudio

    def start(self):
        input("Press Enter to start recording...")
        self.start_recording()
        # gpio.add_event_detect(23, gpio.FALLING, callback=self.falling, bouncetime=10)

    def start_recording(self, channel=1):
        # gpio.remove_event_detect(23)
        print ('Recording')
        # gpio.add_event_detect(23, gpio.RISING, callback=self.rising, bouncetime=10)
        self.recfile = self.rec.open('recordings/test.wav', self.p, 'wb')
        self.recfile.start_recording()

        input("Press Enter to stop recording...")
        self.stop_recording()

    def stop_recording(self, channel=1):
        # gpio.remove_event_detect(23)
        print ('Recording Stopped')
        # gpio.add_event_detect(23, gpio.FALLING, callback=self.falling, bouncetime=10)
        self.recfile.stop_recording()
        self.recfile.close()

        self.start_playback()

    def start_playback(self, channel=1):
        print ('playback starting')
        self.play.play('recordings/test.wav', self.p)


recPlayBtn = ButtonRecorderPlayer()
recPlayBtn.start()

# gpio.cleanup()
