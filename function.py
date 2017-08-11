#!/usr/bin/env python
# encoding: utf-8

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

