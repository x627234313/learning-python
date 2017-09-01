#!/usr/bin/evn python
# encoding: utf-8


# 使用多个装饰器
def decorator1(func):
	print('A')
	def wrapper1():
		print('B')
		func()
	return wrapper1

def decorator2(func):
	print('C')
	def wrapper2():
		print('D')
		func()
	return wrapper2

def decorator3(func):
	print('E')
	def wrapper3():
		print('F')
		func()
	return wrapper3

@decorator1
@decorator2
@decorator3
def decorated():
	print('001')

decorated()


# 把装饰器定义为类
from functools import wraps

class Decorator(object):
	def __init__(self,func):
		self.func = func

	def __call__(self):
		result = self.func()
		result *= 2
		return result

@Decorator
def decorated():
	x = 2
	y = 3
	return x * y

print(decorated()) # 12


# 使用类作装饰器，带参数
from functools import wraps
class Decorator(object):
	def __init__(self, name):
		self.name = name
		print('Inside __init__()')

	def __call__(self, func):
		print('Inside __call__()')
		def wrapper():
			print('Inside wrapper()')
			print('Decorator arguments:', self.name)
			print(func.__name__)
		return wrapper

@Decorator('chai')
def test():
	print('Inside test()')

test()


# 使用类方法作装饰器
class Decorator(object):
	def __init__(self):
		pass

	@classmethod
	def operator(cls, func):
		def wrapper():
			print('Inside wrapper()')
			func()
		return wrapper

@Decorator.operator
def test():
	print('Inside test()')

test()


# 使用带参数的类方法作为装饰器
class Decorator(object):
	def __init__(self):
		pass

	@classmethod
	def operator(cls, *args, **kwargs):
		print('Inside operator()')
		def wrapper(func):
			print('Inside wrapper()')
			def _wrapper():
				print('Inside _wrapper()')
				func()
				print('Decorator arguements:', args, kwargs)
			return _wrapper
		return wrapper

@Decorator.operator('haha...', 'hehe...', name='chai')
def test():
	print('Inside test()')

test()


# 使用类的对象作为装饰器
class Decorator(object):
	def __init__(self):
		print('Inside __init__()')

	def __call__(self, func):
		print('Inside __call__()')
		def wrapper():
			print('Inside wrapper()')
			func()
		return wrapper

d = Decorator()

@d
def test():
	print('Inside test()')

test()


# 使用带参数的类的对象作为装饰器
class Decorator(object):
	def __init__(self):
		pass

	def __call__(self, name):
		def wrapper(func):
			def _wrapper():
				print('Decorator arguements:', name)
				print('Inside _wrapper()')
				func()
			return _wrapper
		return wrapper

d = Decorator()
@d('chai')
def test():
	print('Inside test()')

test()


# 使用实例方法作为装饰器
class Decorator(object):
	def __init__(self):
		pass

	def operator(self, func):
		print('Inside operator()')
		def wrapper():
			print('Inside wrapper()')
			func()
		return wrapper

d = Decorator()
@d.operator
def test():
	print('Inside test()')

test()


# 使用带参数的实例方法作为装饰器
class Decorator(object):
	def __init__(self):
		pass

	def operator(self, name):
		print('Inside operator()')
		def wrapper(func):
			print('Inside wrapper()')
			def _wrapper():
				print('Inside _wrapper()')
				func()
				print('Decorator arguements:', name)
			return _wrapper
		return wrapper

d = Decorator()
@d.operator('chai')
def test():
	print('Inside test()')

test()
