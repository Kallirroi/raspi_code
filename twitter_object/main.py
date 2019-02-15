import RPi.GPIO as gpio
import pyaudio
import time
from record import Recorder
import random
import string


gpio.setmode(gpio.BCM)
gpio.setwarnings(False) # Ignore warning for now
gpio.setup(4, gpio.OUT)  # LED == 4 in BCM
gpio.output(4, False)  # Set output to off
gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)


def randomStringDigits(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


class ButtonRecorderPlayer(object):
    def __init__(self):
        self.isListening = True
        self.p = pyaudio
        self.rec = Recorder(channels=1)

    def on_button(self, channel):
        print('button')
        if recPlayBtn.isListening:
            recPlayBtn.start_recording()
            recPlayBtn.isListening = False
        else:
            recPlayBtn.stop_recording()
            recPlayBtn.isListening = True

    def start(self):
        gpio.add_event_detect(17, gpio.FALLING, callback=self.on_button, bouncetime=100)
        print ('listening')

    def start_recording(self, channel=1):
        print ('Recording, click to stop recording')
        timestr = time.strftime("%Y%m%d-%H%M%S")
        randomId = randomStringDigits(4)
        gpio.output(4, True) #LED on
        self.recfile = self.rec.open('twitter_recordings/' + randomId + '-' + timestr + '.wav', self.p, 'wb')
        self.recfile.start_recording()

    def stop_recording(self, channel=1):
        self.recfile.stop_recording()
        self.recfile.close()
        gpio.output(4, False) #LED on
        print ('Recording Stopped')
        print ('I should tweet now')


recPlayBtn = ButtonRecorderPlayer()
recPlayBtn.start()

try:
    input()
except KeyboardInterrupt:
    pass

#exit if invalid state
gpio.cleanup()
