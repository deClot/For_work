from __future__ import print_function
import os
import sys
import time
import shutil
from watchdog.observers.polling import PollingObserverVFS  
from watchdog.events import PatternMatchingEventHandler 

class MyHandler(PatternMatchingEventHandler):
    #patterns = ["*.*", ".*"]

    def __init__(self, **kwargs):
        PatternMatchingEventHandler.__init__(self, **kwargs)

    def process(self, event):
        """
        event.event_type 
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """

        print ('!!!!!!')
        print (event.event_type)

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)


if __name__ == '__main__':
    args = sys.argv[1:]
    source_dir = args[0]
    #target_dir = args[1]

    observer = PollingObserverVFS(stat=os.stat, listdir=os.listdir, polling_interval=30)
    observer.schedule(MyHandler(patterns=['*.RESULT']),
                      path=source_dir)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
