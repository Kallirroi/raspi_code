import RPi.GPIO as gpio
import pyaudio
import time
from record import Recorder
from play_thread import Player
# from pynput import mouse
import threading

gpio.setmode(gpio.BCM)
gpio.setwarnings(False) # Ignore warning for now
gpio.setup(4, gpio.OUT)  # LED == 4 in BCM
gpio.output(4, False)  # Set output to off
gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)

class ButtonRecorderPlayer(object):
    def __init__(self):
        self.isPlaying = True
        self.p = pyaudio
        self.rec = Recorder(channels=1)
        self.play = None
        self.playback_thread = threading.Thread(name='button_listener', target=self.button_listener)

    def on_button(self, channel):  # Called by inbuilt threaded interrupt
        print('button')
        if recPlayBtn.isPlaying:
            # print('stoping playback and starting recording')
            recPlayBtn.stop_playback()
            recPlayBtn.isPlaying = False
            recPlayBtn.start_recording()
        else:
            # print('stoping recording and starting playback')
            recPlayBtn.stop_recording()
            recPlayBtn.isPlaying = True
            recPlayBtn.start_playback()

    def button_listener(self):
        # with mouse.Listener( on_click = self.on_click) as listener:
        with gpio.add_event_detect(17, gpio.FALLING, callback=self.on_button, bouncetime=300) as listener:
            listener.join()
            print ('listener started')

    def start(self):
        self.playback_thread.start()
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
        print("click to start recording...")
        self.play = Player('recordings', self.p)
        self.play.start()

    def stop_playback(self):
        self.play.stopper()
        print ('playback stopped')


recPlayBtn = ButtonRecorderPlayer()
recPlayBtn.start()


try:
    input()
except KeyboardInterrupt:
    pass

#exit if invalid state
gpio.cleanup()
