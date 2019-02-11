#!/usr/bin/env python3
import sys
import os
import speech_recognition as sr

dirname = 'recordings'
for AUDIO_FILE in os.listdir(dirname):
    if AUDIO_FILE.endswith('.wav'):

        # use the audio file as the audio source
        r = sr.Recognizer()
        with sr.AudioFile(dirname + '/' + AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file

        # recognize speech using Sphinx
        try:
            print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
