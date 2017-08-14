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