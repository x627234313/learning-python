#!/usr/bin/env python
# encoding: utf-8

import sys, gc

def function_foo(x, y, z):
    '''function foo ...

    :param x: bla x
    :type x: int

    :param y: bla y
    :type y: float

    :param int z: bla z

    :return: sum
    :rtype: float

    :raises OSError: bla
    '''
    return x + y + z

result = function_foo(3, 2.6, 3)
print(result)

# 值传递
def foo(x):
    x += 1
    print('inner:', x)

y = 1
foo(y)
print('outer:', y)


# 引用传递
def bar(x):
    x.append(1)
    print('inner:', x)

y = []
bar(y)
print('outer:', y)


# 假的值传递
def foo(x):
    print('inner address:', id(x))
    x += 1
    print('inner value:', x)

y = 1
print('outer address:', id(y))
foo(y)
print('outer value:', y)


# 假的引用传递
def bar(x):
    x = [1, 2, 3]
    print('inner address:', id(x))
    print('inner value:', x)

y = []
print('outer address:', id(y))
bar(y)
print('outer value:', y)


# 参数传递
def hello(name, greeting='Hello', punctuation='!'):
    print('%s, %s%s' % (greeting, name, punctuation))

hello('Mars')
hello('Mars', 'Howdy', '...')
hello('Mars', greeting='Top of the morning to ya')


def print_params(x, y, z=3, *args, **kw):
    print(x, y, z)
    print(args)
    print(kw)

print_params(1, 2, 5, 6, 7, foo=1, bar=2)    # 1 2 5 
                                             # (6, 7)
                                             # {'foo': 1, 'bar': 2}


# 匿名函数
f = lambda *args, **kwargs: (args, kwargs)
print(f(1, 2, 3, a=1, b=2))

f = lambda a, b: lambda c, d: c if a>0 else c+d
print(f(-1, 2)(3, 4))

f = lambda : 'Hello World'
print(f())

li = [lambda : x for x in range(10)]
print(type(li))    # <class 'list'>
print(type(li[0]))    # <class 'function'>
print(li[0]())    # 9
print(li[1]())    # 9


# 作用域
a = 3

def func1():
    print(a)

def func2():
    global a
    a += 1
    print(a)

def func3():
    a = 6
    print(a + 1)

def func4():
    if 1 > 0:
        a = 3
    print(a)

# nonlocal
def outside():
    msg = 'Outside!'
    def inside():
        nonlocal msg
        msg = "Inside!"
        print(msg)
    inside()
    print(msg)

outside()    # Inside!
             # Inside!

def outside():
    msg = 'Outside!'
    def inside():
        msg = 'Inside!'
        print(msg)
    inside()
    print(msg)

outside()


# 引用计数和分代回收
class A:
    pass


class B:
    pass


a = A()
sys.getrefcount(a)    # 2

b = c = a
sys.getrefcount(a)    # 4
sys.getrefcount(A())    # 1

li = [a, a, a]
sys.getrefcount(a)    # 7

del li[0]
sys.getrefcount(a)    # 6

b = B()
sys.getrefcount(a)    # 5
sys.getrefcount(A())    # 1

gc.get_count()    # 当前回收计数,默认阈值是(700,10,10)


# 闭包
def outer():
    x, y = [], 1
    def inner(elem):
        z = 2
        x.append(elem)
        return x
    return inner

f = outer()
print(f(1))    # [1]
print(f(2))    # [1, 2]
print(f(3))    # [1, 2, 3]
print(f.__closure__)    # (<cell at 0x7f9863e20af8: list object at 0x7f9863ded988>,)


# 函数注解
def calc_bmi(weight:float=60, height:'float>0'=1.75) -> str:
    '''Body Mass Index caculator
    '''

    return 'Your BMI is:{}'.format(weight/height)

print(calc_bmi())    # You BMI is:34.285714285714285
print(calc_bmi(65, 1.72))

