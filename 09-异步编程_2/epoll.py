#!/usr/bin/env python
# encoding: utf-8

import fcntl
import os
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

selector = DefaultSelector()


class BackUp(object):
    def __init__(self, filename):
        self.filename = filename
        self.content = None
        self.file_write = None

    def file_read(self):
        with open(self.file, 'rb') as f:
            fd = f.fileno()
            fcntl.fcntl(fd, fcntl.F_SETFL, flag | os.O_NONBLOCK)
            self.content = fd.read(4096)
        selector.register(fd, EVENT_READ, self.file_write)

    def file_write(self, key, mask):
        selector.unregister(key.id)
        with open(self.file, 'wb') as f:
            f.write(self.content)


def loop():
    events = selector.select()
    for enent_key, event_mask in events:
        callback = event_key.data
        callback(event_key, event_mask)


if __name__ == '__main__':
    import time
    start = time.time()
    backup = BackUp()
    backup.file_read()
    loop()
    end = time.time()
    print(end - start)
