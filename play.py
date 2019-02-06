import wave
import sys
import glob, os


class Player(object):
    def __init__(self, channels=1, chunk=1024):
        self._chunk = chunk

    def play(self, dirname, pyaudio):
        self._pa = pyaudio.PyAudio()

        for file in os.listdir(dirname):
            if file.endswith('.wav'):
                wf = wave.open(dirname + '/' + file, 'rb')

                stream = self._pa.open(format=self._pa.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

                data = wf.readframes(self._chunk)

                while data != b'':
                    stream.write(data)
                    data = wf.readframes(self._chunk)
                    print(data)

                stream.stop_stream()
                stream.close()

        self._pa.terminate()
        print('done playing')
