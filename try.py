from __future__ import print_function
import os
import sys
import time
import shutil
from watchdog.observers.polling import PollingObserverVFS
from watchdog.events import PatternMatchingEventHandler

import module
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
        '''if not event.is_directory:
            # the file will be processed there
            print('{} {} --> {}'.format(event.src_path,
                                        event.event_type,
                                        self._target_dir))
            shutil.copy(event.src_path, self._target_dir)
        '''
        if event.event_type == 'modified':
            print ('!!!!!')
            print (event.src_path)
            module.main_function(event.src_path)

    def on_modified(self, event):
        self.process(event)

if __name__ == '__main__':
    args = sys.argv[1:]
    source_dir = args[0]

    observer = PollingObserverVFS(stat=os.stat, listdir=os.listdir, polling_interval=5)
    observer.schedule(MyHandler(patterns=['*.RESULT']),
                      path=source_dir)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
