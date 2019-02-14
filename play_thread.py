import wave
import sys
import os
from threading import Thread,Event
from time import sleep

class Player(Thread):
    def __init__(self, dirname, pyaudio, channels=1, chunk=200):
        Thread.__init__(self)
        self._stopper = Event()
        self._chunk = chunk
        self._stream = None
        self._pa = pyaudio.PyAudio()
        self._dirname = dirname

    def run(self):
        self._stopper.clear()

        # loop until the stop event is set
        while not self._stopper.is_set():
            for file in os.listdir(self._dirname):

                fileSize = os.path.getsize(self._dirname + '/' + file)
                print (fileSize)

                if file.endswith('.wav') and fileSize > 0:
                    wf = wave.open(self._dirname + '/' + file, 'rb')

                    self._stream = self._pa.open(format=self._pa.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

                    data = wf.readframes(self._chunk)

                    while data != b'' and not self._stopper.is_set(): # loop until the stop event is set or no more audio data
                        self._stream.write(data)
                        data = wf.readframes(self._chunk)

                    self._stream.stop_stream()
                    self._stream.close()

        self._pa.terminate()
        print('done playing')


    def stopper(self):
        self._stopper.set()
