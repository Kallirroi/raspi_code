import RPi.GPIO as gpio
import pyaudio
import wave
from time import sleep
from recorder import Recorder

gpio.setmode(gpio.BCM)

class ButtonRecorder(object):
    def __init__(self, filename):
        self.filename = filename
        gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)
        self.rec = Recorder(channels=1)

    def play(self, channel):
        CHUNK = 1024
        sleep(3)
        wf = wave.open("output.wav", 'rb')
        p = pyaudio.PyAudio() # take his code and build it into here
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=1,
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(CHUNK)
        while data != '':
            stream.write(data)
            print 'Playing'
            data = wf.readframes(CHUNK)
        print 'done with playing'
        stream.stop_stream()
        stream.close()
        p.terminate() #this should not be destroyed

    def start(self):
        gpio.add_event_detect(17, gpio.FALLING, callback=self.record, bouncetime=10)

    def stop_record(self, channel):
        gpio.remove_event_detect(17)
        print 'Stop recording'
        self.recfile.stop_recording()
        self.recfile.close()
        gpio.add_event_detect(17, gpio.FALLING, callback=self.record, bouncetime=10)

        self.play(channel)

    def record(self, channel):
        gpio.remove_event_detect(17)
        print 'Start recording'
        self.recfile = self.rec.open(self.filename, 'wb')
        self.recfile.start_recording()
        gpio.add_event_detect(17, gpio.FALLING, callback=self.stop_record, bouncetime=10)

rec = ButtonRecorder('output.wav')
rec.start()

try:
    raw_input()

except KeyboardInterrupt:
    pass

gpio.cleanup()


# """PyAudio example: Record a few seconds of audio and save to a WAVE file."""
#
# import pyaudio
# import wave
#
# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 44100
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "output.wav"
#
# p = pyaudio.PyAudio()
#
# stream = p.open(format=FORMAT,
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 frames_per_buffer=CHUNK)
#
# print("* recording")
#
# frames = []
#
# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK, exception_on_overflow = False)
#     frames.append(data)
#
# print("* done recording")
#
# stream.stop_stream()
# stream.close()
# p.terminate()
#
# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()
