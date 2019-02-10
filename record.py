import wave

class Recorder(object):
    '''A recorder class for recording audio to a WAV file.
    Records in mono by default.
    '''

    def __init__(self, channels=1, rate=44100, frames_per_buffer=1024, chunk = 200):
        self.channels = channels
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer
        self.chunk = chunk

    def open(self, fname, pyaudio, mode='wb'):
        return RecordingFile(fname, pyaudio, mode, self.channels, self.rate,
                            self.frames_per_buffer, self.chunk)

class RecordingFile(object):
    def __init__(self, fname, pyaudio, mode, channels,
                rate, frames_per_buffer, chunk):
        self.fname = fname
        self.p = pyaudio
        self._pa = pyaudio.PyAudio()
        self.mode = mode
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.frames_per_buffer = frames_per_buffer
        self.wavefile = self._prepare_file(self.fname, self.mode)
        self._stream = None

    def __enter__(self):
        return self

    def __exit__(self, exception, value, traceback):
        self.close()

    def record(self, duration):
        # Use a stream with no callback function in blocking mode
        self._stream = self._pa.open(format=self.p.paInt16,
                                        channels=self.channels,
                                        rate=self.rate,
                                        input=True,
                                        frames_per_buffer=self.chunk)
        for _ in range(int(self.rate / self.chunk * duration)):
            audio = self._stream.read(self.chunk, exception_on_overflow = False)
            self.wavefile.writeframes(audio)
        return None

    def start_recording(self):
        # Use a stream with a callback in non-blocking mode
        self._stream = self._pa.open(format=self.p.paInt16,
                                        channels=self.channels,
                                        rate=self.rate,
                                        input=True,
                                        frames_per_buffer=self.chunk,
                                        stream_callback=self.get_callback())
        self._stream.start_stream()
        return self

    def stop_recording(self):
        self._stream.stop_stream()
        return self

    def get_callback(self):
        def callback(in_data, frame_count, time_info, status):
            self.wavefile.writeframes(in_data)
            return in_data, self.p.paContinue
        return callback


    def close(self):
        self._stream.close()
        self._pa.terminate()
        self.wavefile.close()

    def _prepare_file(self, fname, mode='wb'):
        wavefile = wave.open(fname, mode)
        wavefile.setnchannels(self.channels)
        wavefile.setsampwidth(self._pa.get_sample_size(self.p.paInt16))
        wavefile.setframerate(self.rate)
        return wavefile
