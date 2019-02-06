import wave
import sys


class Player(object):
    def __init__(self, channels=1, chunk=1024):
        self._chunk = chunk

    def play(self, filename, pyaudio):
        self._pa = pyaudio.PyAudio()
        wf = wave.open(filename, 'rb')

        stream = self._pa.open(format=self._pa.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

        data = wf.readframes(self._chunk)

        while data != '':
            stream.write(data)
            data = wf.readframes(self._chunk)
            print('playing')

        stream.stop_stream()
        stream.close()
        self._pa.terminate()
        print('done playing')
