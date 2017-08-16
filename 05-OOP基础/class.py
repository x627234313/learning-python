#!/usr/bin/env python
# encoding: utf-8

class Base:
	def func(self):
		print('Hello')


class Child(Base):
	def func1(self, name):
		print('Hello', name)


c = Child()
c.func()    # Hello  继承父类的方法
c.func1('World')    # Hello World


class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def func(self):
		print(self.name, 'is a Person.')


class Student(Person):
	def __init__(self, name, age, score):
		super(Student, self).__init__(name, age)
		self.score = score

	def func(self):
		print(self.name, 'is a Student.')


s = Student('zhangsan', 15, 88)
s.func()    # zhangsan is a Student.  子类中的方法覆盖了父类的方法
print(hasattr(s, 'name'))    # True
print(getattr(s, 'name'))    # zhangsan
print(getattr(s, 'name', 'lisi'))    # zhangsan  对象的属性有值，返回原有的值
print(getattr(s, 'gender', 'man'))    # man  对象没有某个属性，返回指定的
setattr(s, 'score', 99)
print(getattr(s, 'score'))    # 99
delattr(s, 'score')
print(getattr(s, 'score', 100))    # 100
print(s.name, s.age)

print(Student.__dict__)
print(Student.__name__)    # Student
print(Student.__doc__)
print(Student.__module__)    # 直接在Python解释器中执行都是__main__
print(Student.__bases__)


class Test(object):
	def __new__(self):
		print('__new__被执行')

	def __init__(self):
		print('__init__被执行')


t = Test()    # __new__是真正的构造方法，__init__是初始化方法


class A:
	x = 'x in A'
	y = 'y in A'

class B:
	x = 'x in B'
	y = 'y in B'

class C(A, B):
	pass

class D(B, A):
	pass

print(C.y)    # y in A
print(D.y)    # y in B
print(C.__bases__)    # (<class '__main__.A'>, <class '__main__.B'>)
print(D.__bases__)    # (<class '__main__.B'>, <class '__main__.A'>)
                      # 多继承时的解析顺序是按照__base__中基类元组的顺序
issubclass(C, A)
issubclass(D, B)
issubclass(C, (A, B))

d = D()
print(isinstance(d, D))    # True
print(isinstance(d, A))    # True
print(isinstance(d, (D, B, A)))    # True

print(type(d) == D)    # True
print(type(d) == A)    # False
                       # 多继承判断类型时，不要使用type.

class MyClass(object):
	'''A simple example class
	'''

	def __init__(self, num):
		self.num = num

	def __repr__(self):
		return '__repr__执行'

	def __str__(self):
		return '__str__执行'

	i = 123
	def func(self):
		return 'Hello World!'


x = MyClass(999)
print(str(x))
print(repr(x))
