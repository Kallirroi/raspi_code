
import wave
import sys
import os


class Player(object):
    def __init__(self, channels=1, chunk=1024):
        self._chunk = chunk
        self._looping = True
        self._stream = None

    def play(self, dirname, pyaudio):
        self._pa = pyaudio.PyAudio()
        self._looping = True

        while self._looping:
            for file in os.listdir(dirname):
                if file.endswith('.wav'):
                    wf = wave.open(dirname + '/' + file, 'rb')

                    self._stream = self._pa.open(format=self._pa.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

                    data = wf.readframes(self._chunk)

                    while data != b'' and self._looping:
                        self._stream.write(data)
                        data = wf.readframes(self._chunk)

                    self._stream.stop_stream()
                    self._stream.close()

        self._pa.terminate()
        print('done playing')

    def stop(self):
        print('STOP')
        self._looping = False
