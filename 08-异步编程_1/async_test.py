#!/usr/bin/env python
# encoding: utf-8

import socket
import time


def nonblocking_way():
    sock = socket.socket()
    sock.setblocking(False)
    try:
        sock.connect(('spzl.miit.gov.cn', 80))
    except BlockingIOError:
        pass
    request = 'GET / HTTP/1.0\r\nHost: localhost\r\n\r\n'
    data = request.encode('ascii')
    while True:
        try:
            sock.send(data)
            break
        except OSError:
            pass

    response = b''
    while True:
        try:
            chunk = sock.recv(4096)
            while chunk:
                response += chunk
                chunk = sock.recv(4096)
            break
        except OSError:
            pass
    return response


def sync_way():
    start = time.time()
    res = []
    for i in range(10):
        res.append(nonblocking_way())
    end = time.time()
    print(end - start)
    return len(res)
result = sync_way()    # 执行时间平均2s左右
