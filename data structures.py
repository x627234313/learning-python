#!/usr/bin/env python
# encoding: utf-8

list = []

for i in range(ord('A'),ord('z')+1):
    list.append(chr(i))

print(list)

list1 = [(x,y) for x in [1,2,3] if x > 2 for y in [3,1,4]]
list2 = [(x,y) if x >= 2 else x+5 for x in [1,2,3] for y in [3,1,4]]
print(list1)
print(list2)

del list1[:]
del list2

print(list1)
print(list2)
