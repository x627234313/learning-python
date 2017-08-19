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

	def __str__(self):
		return '__str__'

x = MyClass()
print(str(x))    # __str__
print(repr(x))    # <__main__.MyClass object at 0x000001C743397F60>

class MyClass_1:
	'''compare __str__  __repr__
	'''
	def __repr__(self):
		# 只能使用return返回字符串，数值会报错
		return '__repr__'

x = MyClass_1()
print(str(x))    # __repr__  str()先找__str__,没有再找__repr__
print(repr(x))    # __repr__  repr()找__repr__,没有返回默认。


class MyClass_2(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@classmethod
	def func(cls):
		name = 'zhangsan'
		age = 22
		return cls(name, age)    # cls代表的就是类自己，return cls() 等价于 return MyClass_2()

	@staticmethod
	def func1(x, y):
		return x + y


ls = MyClass_2('lisi', 33)
print(ls.name)    # lisi
print(ls.age)    # 33

zs = MyClass_2.func()
print(zs.name)    # zhangsan

n = MyClass_2.func1(2, 3)
m = ls.func1(8, 9)
print(n)
print(m)


class Test(object):
	def __init__(self, num):
		self.num = num

	def __add__(self, other):
		return Test(self.num + other.num)

x = Test(3)
y = Test(5)
z = x + y
print(z.num)    # 8
x = Test('a')
y = Test('b')
z = x + y
print(z.num)    # ab


class Test1(object):
	def __init__(self, num):
		self.num = num

	def __radd__(self, other):
		return Test1(self.num + other.num)

class Test2(object):
	def __init__(self, num):
		self.num = num

x = Test1(8)
y = Test2(9)
#z1 = x + y    # TypeError: unsupported operand type(s) for +: 'Test1' and 'Test2'
z2 = y + x
print(z2.num)    # 17


class Test3(object):
	def __init__(self, num):
		self.num = num

	def __iadd__(self, other):
		return Test3(self.num + other.num)

x = Test3(5)
y = Test3(6)
x += y
y += x
print(x.num)    # 11
print(y.num)    # 17

x = Test3(5)
y = Test2(6)
x += y
#y += x    # TypeError: unsupported operand type(s) for +=: 'Test2' and 'Test3'
print(x.num)    # 11


class Test4(object):
	def __init__(self, num):
		self.num = num

	def __add__(self, other):
		return Test4(self.num + other.num)

	def __radd__(self, other):
		return Test4(self.num + other.num)

	def __iadd__(self, other):
		return Test4(self.num + other.num)

x = Test4(11)
y = Test4(22)
z1 = x + y
z2 = y + x
print(z1.num)    # 33
print(z2.num)    # 33
x += y
y += x
print(x.num)    # 33
print(y.num)    # 55


class Test5(object):
	def __init__(self, a, b, c):
		self.a = a
		self._b = b
		self.__c = c

t = Test5('chai', 'li', 'shuai')
print(dir(t))    # ['_Test5__c', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
                 #  '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
	         #  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
		 #  '__weakref__', '_b', 'a']
print(t.a)
print(t._b)    # 单下划线的属性，是实验、保护性质的，不要随便访问
print(t._Test5__c)    # 双下划线的属性，是私有性质的，不能‘直接’访问
