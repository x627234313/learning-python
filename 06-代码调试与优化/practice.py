#!/usr/bin/env python
# encoding: utf-8

# 使用字典代替 if...elif
def func():	
	if x == 'a':
		handle_a()
	elif x == 'b':
		handle_b()
	else:
		pass


handle_map = {'a' : handle_a, 'b' : handle_b, 'c' : handle_c}
handle_map[x]()


# and:条件为假在前  or:条件为真在前
if False and True:
	pass
elif True or False:
	pass


# 使用in或not in判断元素是否在容器中
str = 'Life is short, I use Python'
print('c' in str)
print('Python' in str)


# 排序方法，sort()和sorted()
list1 = [1, 3, 9, 7, 12, 0]
print(list1.sort())    # None
print(list1)    # [0, 1, 3, 7, 9, 12]

str1 = 'Life is short'
str2 = sorted(str1)
print(str2)    # [' ', ' ', 'L', 'e', 'f', 'h', 'i', 'i', 'o', 'r', 's', 's', 't']
print(str1)    # Life is short


# list、tuple、set选择
l = list('acdd')
t = tuple('acdd')
s = set('acdd')
print(l)    # ['a', 'c', 'd', 'd']
print(t)    # ('a', 'c', 'd', 'd')
print(s)    # {'d', 'a', 'c'}

l.append('b')
s.add('b')
print(l)    # ['a', 'c', 'd', 'd', 'b']
print(s)    # {'d', 'a', 'c', 'b'}


# 避免命名空间污染
from time import time

def time():    # time() 自定义的函数会覆盖导入的函数
	pass


# 变量交换 True和False
def func():
	x = 3
	y = 5
	if x < y:
		x, y = y, x    # 变量和值是绑定的关系,不需要中间变量

print(1 == True)    # True


# 字符串连接,'+'和join
list1 = ['h', 'e', 'l', 'l', 'o']
list2 = ' '.join(list1)
print(list2)    # h e l l o

p = '，'
for s in list1:
	p += s
print(p)    # ，hello


# 深浅copy
import copy
obj = (1, 3, 5, ['a', ['c', 'd']])
obj1 = copy.copy(obj)
obj2 = copy.deepcopy(obj)
print(obj1)
print(obj2)

obj[3][1][0] = 10
print(obj1)    # (1, 3, 5, ['a', [10, 'd']])
print(obj2)    # (1, 3, 5, ['a', ['c', 'd']])
print(id(obj))    # 1836186602376
print(id(obj1))    # 2251528407944
print(id(obj2))    # 2251528408024

t = (1, 2, 3)
t1 = copy.copy(t)
t2 = copy.deepcopy(t)    # 由不可变对象组成的对象，不论深浅拷贝，不会申请新的内存空间
print(id(t1))    # 2472931299048
print(id(t2))    # 2472931299048


# 生成器惰性求值，只迭代一遍  节省内存开销
def func():
	for i in range(10):
		yield i
f = func()
print(next(f))    # 0  调用一次，迭代一次
print(next(f))    # 1


# 循环优化
import timeit

def func1():
	for i in range(10):
		for j in range(10000):    # 大的循环放在里层，可以让CPU在相近的内存地址上进行计算，减小随机性
			pass

def func2():
	for i in range(10000):
		for j in range(10):
			pass

print(timeit.timeit(func1, number=100))    # 0.3393954700863091
print(timeit.timeit(func2, number=100))    # 0.743681654822326


# 变量命名空间
# 能使用局部变量就不要使用全局变量
# 放在循环更外层的就不要放到循环更里层
def func1():
	a = 1
	for i in range(10000):
		print(a)

def func2():
	for i in range(10000):    # a = 1 放在循环里面，要被初始化一万次
		a = 1
		print(a)
