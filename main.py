import RPi.GPIO as gpio
import pyaudio
import time
from record import Recorder
from play import Player

gpio.setmode(gpio.BCM)
gpio.setwarnings(False) # Ignore warning for now
gpio.setup(4, gpio.OUT)  # LED == 4 in BCM
gpio.output(4, False)  # Set output to off
gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)

class ButtonRecorderPlayer(object):
    def __init__(self):
        self.rec = Recorder(channels=1)
        self.play = Player()
        self.p = pyaudio

    def start_recording(self, channel=1):
        print ('Recording')
        gpio.output(4, True) #LED on
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.recfile = self.rec.open('recordings/' + timestr + '.wav', self.p, 'wb')
        # self.recfile.start_recording() # non blocking mode
        self.recfile.record(duration = 10.0) # blocking mode
        time.sleep(0.5)


    def stop_recording(self, channel=1): # this should automatically break to "start playback"
        print ('Stopped recording')
        gpio.output(4, False) # LED is OFF when playing
        self.recfile.stop_recording()
        self.recfile.close()
        time.sleep(0.5)

    def start_playback(self, channel=1):
        gpio.output(4, False) # LED is OFF when playing
        print ('Playing')
        self.play.play('recordings', self.p)
        time.sleep(0.5)

recPlayBtn = ButtonRecorderPlayer()
state = False
def getState(state):
    if (gpio.input(17)==1):
        print ('button!')
        state = not state
    return state


while True:
    prevState = state
    state = getState(prevState)

    if ( state == False ): # playing
        print('playing')
        # recPlayBtn.start_playback()
    elif ( prevState == False and state == True):
        # recPlayBtn.start_recording()
        print ('started recording') # recording
    elif (prevState == True and state == False):
        # recPlayBtn.stop_recording()
        print ('stopped recording') # stopped recording

    # Now wait a while
    time.sleep(0.25)

#exit if invalid state
gpio.cleanup()
