
#!/usr/bin/evn python
# encoding: utf-8


# 使用多个装饰器
def decorator1(func):
	print('A')
	def wrapper():
		pass
	print('B')
	return wrapper

def decorator2(func):
	print('C')
	def wrapper():
		pass
	print('D')
	return wrapper

def decorator3(func):
	print('E')
	def wrapper():
		pass
	print('F')
	return wrapper

@decorator1
@decorator2
@decorator3
def decorated():
	return '1024'

d = decorated()    # E F C D A B


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
class Decorator(object):
	def __init__(self,func):
		self.func = func

	def __call__(self, x, y):
		pass

@Decorator
def decorated():
	pass
