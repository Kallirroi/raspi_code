# import RPi.GPIO as gpio
import pyaudio
import time
from record import Recorder
from play import Player
from pynput import mouse
import threading
# gpio.setmode(gpio.BCM)

class ButtonRecorderPlayer(object):
    def __init__(self):
        # gpio.setup(23, gpio.IN, pull_up_down=gpio.PUD_UP)
        self.rec = Recorder(channels=1)
        self.play = Player()
        self.isPlaying = True
        self.p = pyaudio
        self.listener_thread = threading.Thread(name='mouse_listener',
                                                  target=self.mouse_listener)

    def on_click(self, x, y, button, pressed):
        if pressed:
            if self.isPlaying:
                print('stoping playback and starting recording')
                self.stop_playback()
                self.start_recording()
                self.isPlaying = False
            else:
                print('stoping recording and starting playback')
                self.stop_recording()
                self.start_playback()
                self.isPlaying = True

    def mouse_listener(self):
        with mouse.Listener(
        on_click=self.on_click) as listener:
            listener.join()

    def start(self):
        self.listener_thread.start()
        self.start_playback()
        # gpio.add_event_detect(23, gpio.FALLING, callback=self.falling, bouncetime=10)

    def start_recording(self, channel=1):
        # gpio.remove_event_detect(23)
        # gpio.add_event_detect(23, gpio.RISING, callback=self.rising, bouncetime=10)
        print ('Recording, click to stop recording')
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.recfile = self.rec.open('recordings/' + timestr + '.wav', self.p, 'wb')
        self.recfile.start_recording()

    def stop_recording(self, channel=1):
        # gpio.remove_event_detect(23)
        # gpio.add_event_detect(23, gpio.FALLING, callback=self.falling, bouncetime=10)
        self.recfile.stop_recording()
        self.recfile.close()
        print ('Recording Stopped')


    def start_playback(self, channel=1):
        print ('playback starting')
        print("click to start recording...")
        self.play.play('recordings', self.p)

    def stop_playback(self):
        self.play.stop()
        print ('playback stoped')

recPlayBtn = ButtonRecorderPlayer()
recPlayBtn.start()

# gpio.cleanup()
