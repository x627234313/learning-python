#!/usr/bin/env python
# encoding: utf-8

import socket
import time


# 同步阻塞方式
def blocking_way():
    sock = socket.socket()
    sock.connect(('localhost', 8080))
    request = 'GET / HTTP/1.0\r\nHost: localhost\r\n\r\n'
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)
    return response


def sync_way():
    start = time.time()
    res = []
    for i in range(10):
        res.append(blocking_way())
    end = time.time()
    print(end - start)
    return len(res)

result = sync_way()    # 0.063


# 多进程方式
from concurrent import futures


def blocking_way1():
    sock = socket.socket()
    # blcoking
    sock.connect(('localhost', 8080))
    request = 'GET / HTTP/1.0\r\nHost: localhost\r\n\r\n'
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        # blocking
        chunk = sock.recv(4096)
    return response


def process_way():
    start = time.time()
    workers = 10
    with futures.ProcessPoolExecutor(workers) as executor:
        futs = {executor.submit(blocking_way1) for i in range(10)}
    end = time.time()
    print(end - start)
    return len([fut.result() for fut in futs])

result = process_way()    # 0.066


# 多线程方式
def blocking_way2():
    sock = socket.socket()
    sock.connect(('localhost', 8080))
    request = 'GET / HTTP/1.0\r\nHost: localhost\r\n\r\n'
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)
    return response


def thread_way():
    start = time.time()
    workers = 10
    with  futures.ThreadPoolExecutor(workers) as executor:
        futs = {executor.submit(blocking_way2) for i in range(10)}
    end = time.time()
    print(end - start)
    return len([fut.result() for fut in futs])

result = thread_way()
