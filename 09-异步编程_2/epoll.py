#!/usr/bin/env python
# encoding: utf-8

import fcntl
import os
from selectors import SelectSelector, EVENT_WRITE, EVENT_READ

selector = SelectSelector()
STOP = False
file_list = ['1.txt', '2.txt', '3.txt', '4.txt']

class BackUp(object):
    def __init__(self, filename):
        self.filename = filename
        self.fd = None
        self.content = b''

    def file_open(self):
        #self.fd = os.open(self.filename, os.O_RDWR)
        #fo = os.fdopen(self.fd,'rb')
        #selector.register(fo, EVENT_READ, self.file_read)

        self.fd = open(self.filename, 'rb')
        flag = fcntl.fcntl(self.fd, fcntl.F_GETFL)
        print(flag)
        fcntl.fcntl(self.fd, fcntl.F_SETFL, flag | os.O_NONBLOCK)
        flag = fcntl.fcntl(self.fd, fcntl.F_GETFL)
        print(flag)
        if flag & os.O_NONBLOCK:
            print('O_NONBLOCK!')
        selector.register(self.fd.fileno(), EVENT_READ, self.file_read)

        #with open(self.filename, 'rb') as f:
        #    self.fd = f.fileno()
        #    flag = fcntl.fcntl(self.fd, fcntl.F_GETFL)
        #    fcntl.fcntl(self.fd, fcntl.F_SETFL, flag | os.O_NONBLOCK)
        #    flag = fcntl.fcntl(self.fd, fcntl.F_GETFL)
        #    if flag & os.O_NONBLOCK:
        #        print('O_NONBLOCK!')
        #    selector.register(self.fd, EVENT_READ, self.file_read)

        #selector.register(self.fd, EVENT_READ, self.file_read)

    def file_read(self, key, mask):
        global STOP
        chunk = self.fd.read()
        if chunk:
            self.content += chunk
        else:
            selector.unregister(key.fd)
            self.fd.close()
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
    for filename in file_list:
        backup=BackUp('/tmp/' + filename)
        backup.file_open()
    #backup = BackUp('/tmp/2.txt')
    #backup.file_open()
    loop()
    end = time.time()
    print(end - start)
