import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class MyHandler(PatternMatchingEventHandler):
    patterns=["*.wav"]

    def process(self, event):
        print(event)
        print('I should tweet')

    def on_created(self, event):
        self.process(event)

if __name__ == '__main__':

    observer = Observer()
    observer.schedule(MyHandler(), './twitter_recordings')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
