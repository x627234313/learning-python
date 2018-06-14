#!/usr/bin/env python
# encoding: utf-8

def application(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']


####
class application:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Hello world!\n"


####
def __iter__(self):
    path = self.environ['PATH_INFO']
    if path == "/":
        return self.GET_index()
    elif path == "/hello":
        return self.GET_hello()
    else:
        return self.notfound()

    def GET_index(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Welcome!\n"

    def GET_hello(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Hello world!\n"

    def notfound(self):
        status = '404 Not Found'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Not Found!\n"


####
urls = [("/", "index"),
        ("/hello", "hello")]
    def __iter__(self):
        path_info = self.environ['PATH_INFO']
        method = self.environ['REQUEST_METHOD']

        for path, name in self.urls:
            if path == path_info:
                funcname = method.upper() + "_" + name
                func = getattr(self, funcname)
                return func()
        return self.notfound()



####
urls = [("/“, "index"),
         ("/hello/(.*)", "hello")]

    def __iter__(self):
         path = self.environ["PATH_INFO"]
         method = self.environ['REQUEST_METHOD']

         for pattern, name in self.urls:
             m = re.match('^' + pattern + '$', path)
             if m:
                 # pass the matched groups as arguments to the function
                 args = m.groups()
                 funcname = method.upper() + '_' + name
                 func = getattr(self, funcname)
                 return func(*args)
         return self.notfound()

    def GET_hello(self, name):
         status = '200 OK'
         response_headers = [('Content-type', 'text/plain')]
         self.start(status, response_headers)
         yield "Hello %s!\n" % name


####
def __iter__(self):
    return self.delegate()

def delegate(self):
    path = self.environ['PATH_INFO']
    method = self.environ['REQUEST_METHOD']

    for pattern, name in self.urls:
        m = re.match('^' + pattern + '$', path)
        if m:
            # pass the matched groups as arguments to the function
            args = m.groups()
            funcname = method.upper() + '_' + name
            func = getattr(self, funcname)
            return func(*args)

    return self.notfound()


####
class wsgiapp:
    """Base class for wsgi application."""
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        return self.delegate()

    def delegate(self):
        path = self.environ['PATH_INFO']
        method = self.environ['REQUEST_METHOD']

        for pattern, name in self.urls:
            m = re.match('^' + pattern + '$', path)
            if m:
                # pass the matched groups as arguments to the function
                args = m.groups()
                funcname = method.upper() + "_" + name
                func = getattr(self, funcname)
                return func(*args)

        return self.notfound()


class application(wsgiapp):
    urls = [("/", "index"),
            ("/hello/(.*)", "index")]

    def GET_index(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield ”Welcome!\n"

    def GET_hello(self, name):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Hello %s!\n" % name


####
class wsgiapp:
    """Base class for my wsgi application."""
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response
        self.status = '200 OK'
        self._headers = []

    def header(self, name value):
        self._headers.append((name, value))

    def __iter__(self):
        x = self.delegate()
        self.start(self.status, self._headers)

        # return value can be a string or a list. we should be able to
        # return an iter in both the cases.
        if isinstance(x, str):
            return iter([x])
        else:
            return iter(x)


class application(wsgiapp):
    urls = [("/", "index"),
            ("/hello/(.*)", "index")]

    def GET_index(self):
        self.header('content-type': 'text/plain')
        return "Welcome!\n"

    def GET_hello(self, name):
        self.header("content-type": "text/plain")
        return "Hello %s!\n" % name

def __iter__(self):
    try:
        x = self.delegate()
        self.start(self.status, self._headers)
    except:
        headers = [("Content-Type": "text/plain")]
        self.start("500 Internal Error", headers)
        x = "Internal Error:\n\n" + traceback.format_exc()

    # return value can be a  string or a list. we should be able to
    # return an iter in both the cases.
    if isinstance(x, str):
        return iter([x])
    else:
        return iter(x)


####
import re
import traceback


class wsgiapp:
    """The most beatiful micro web framwork.

    How to use:

    class application(wsgiapp):
        urls = [("/(.*)", "index"),]
        def GET_hello(self, name):
            self.header("Content-Type", "text/plain")
            return "Hello, %s!" % name
    """

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response
        self.status = '200 OK'
        self._headers = []

    def header(self, name, value):
        self._headers.append((name, value))

    def __iter__(self):
        try:
            x = self.delegate()
            self.start(self.status, self._headers)
        except:
            headers = [("Content_Type", "text/plain")]
            self.start("500 Internal Error", headers)
            x = "Internal Error:\n\n + traceback.format_exc()"
        # return value can be a string or a list. we should be able to
        # return an iter in both the cases.
        if isinstance(x, str):
            return iter([x])
        else:
            return iter(x)

    def delegate(self):
        path = self.environ['PATH_INFO']
        method = self.environ['REQUEST_METHOD']

        for pattern, name in self.urls:
            m = re.match('^' + pattern + '$', path)
            if m :
                # pass the matched groups as arguments to the function
                args = m.groups()
                funcname = method.upper() + "_" + name
                func = getattr(self, funcname)
                return func(*args)

        return self.notfound()
