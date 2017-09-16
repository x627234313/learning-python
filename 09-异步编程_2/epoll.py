#!/usr/bin/env python
# encoding: utf-8

import fcntl
import os
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

selector = DefaultSelector()
STOP = False

class BackUp(object):
    def __init__(self, filename):
        self.filename = filename
        self.fd = None
        self.content = b''

    def file_open(self):
        with open(self.filename, 'rb') as f:
            self.fd = f.fileno()
            flag = fcntl.fcntl(self.fd, fcntl.F_GETFL)
            fcntl.fcntl(self.fd, fcntl.F_SETFL, flag | os.O_NONBLOCK)
            flag = fcntl.fcntl(self.fd, fcntl.F_GETFL)
            if flag & os.O_NONBLOCK:
                print('O_NONBLOCK!')
            selector.register(self.fd, EVENT_READ, self.file_read)
        #selector.register(self.fd, EVENT_READ, self.file_read)

    def file_read(self, key, mask):
        global STOP
        chunk = self.fd.read(1024)
        if chunk:
            self.content += chunk
        else:
            selector.unregister(key.fd)
            STOP = True


def loop():
    while not STOP:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback(event_key, event_mask)


if __name__ == '__main__':
    import time
    start = time.time()
    backup = BackUp('/tmp/1.txt')
    backup.file_open()
    loop()
    end = time.time()
    print(end - start)
