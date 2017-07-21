#!/usr/bin/env python
# encoding: utf-8

#decorator
@name
class Student:
	pass
	
@name()
class Student():
	pass
	
@name(123)
def Teacher():
	pass

@name('abc',)
class Abc():
	pass
	
@name(123 for i in 123456)
async def Teacher():
	
@name(123 async for i in 123456)
async def Teacher():
	
@name(123 for i in 123456 for j in abcde)
async def Teacher():
	
@name (123 for i in not 123456 and not abc or not abcde if not 567)
async def Teacher():
	
@name(123 async for i in 12345, dos = doc, ** gbk, * utf)
async def Teacher():
	
@name(123 async for i in 12345 for j in abcde)
async def Teacher():
	
@name(a = 12,)
async def Teacher():
	
@name(** abc,)
async def Teacher():
	
@name(* abc)
async def Teacher():
	

#funcdef  async_funcdef
def name():
	pass

def name() -> str :
	pass

def name() -> cc:    #NameError: name 'cc' is not defined
	pass

def name(a):
	pass
	
def name(a, b):
	pass
	
def name(a, b=10):
	pass

def name(a=1, b):    #SyntaxError: non-default argument follows default argument
	pass

def name(a=1, b=2):
	pass

def name(a, b=10, ):
	pass
	
def name(a, b=10, *c):
	pass

def name(a, b=10, *):    #SyntaxError: named arguments must follow bare *
	pass

def name(a, b, *, x):
	pass

def name(a, b, *, **kw):    #SyntaxError: named arguments must follow bare *
	pass
		
def name(a, **kw):
	pass

def name(a, **kw,):
	pass

def name(a, b=10, *c, d=4):
	pass
	
def name(a, b=10, *c, d, **kw):
	pass
	
def name(a, b, *args, c, **kw,):
	pass
	

#lambdef  lambdef_nocond
x = lambda : 'abc'

x = lambda a : a+10
	
x = lambda a=10:a+10
	
x = lambda a=1,b=2:a*b
	
x = lambda a=2,b=3,:a*b    #,???

x = lambda a=2,b=3,** c:a+b*c     # x()  TypeError: unsupported operand type(s) for *: 'int' and 'dict'
	
x = lambda a=2,b=3,** c,:a+b*c    # x()  TypeError: unsupported operand type(s) for *: 'int' and 'dict'
	
x = lambda a,b=3,*,c=6:a+b*c

x = lambda a,b,*args:'test'
	
x = lambda a,b,*args,c:test

x = lambda a=3,b=4,*args,c=5:test
	
x = lambda a,b=3,*args,c=5,:'test'
	
x = lambda a=2,b=3,*args,c=4,**kw:test
	
x = lambda a,b,*args,**kw:test
	
x = lambda a,b,*args,**kw,:test
