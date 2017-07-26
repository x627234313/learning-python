#!/usr/bin/env python
# encoding: utf-8

list = []

for i in range(ord('A'),ord('z')+1):
    list.append(chr(i))

print(list)

list1 = [(x,y) for x in [1,2,3] if x > 2 for y in [3,1,4]]
list2 = [(x,y) if x >= 2 else x+5 for x in [1,2,3] for y in [3,4,5]]
'''for x in [1,2,3]:
    for y in [3,4,5]:
        if x >= 2:
            list2.append((x,y))
        else:
            list2.append(x+5)
            
'''
list3 = [(x,y) for x in range(10) if x % 2 if x > 3 for y in range(10) if y > 7 if y != 8]

print(list1)  #[(3, 3), (3, 1), (3, 4)]
print(list2)  #[6, 6, 6, (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
print(list3)  #[(5, 9), (7, 9), (9, 9)]

del list1[:]
del list2

print(list1)
print(list2)

#整数
i = 12, i = int(3.14), i = int('0b100', base=0)    # 4
"""
bit_length()  # Number of bits necessary to represent self in binary. 返回整数的二进制的bit位数
conjugate()   # Returns self, the complex conjugate of any int.
from_bytes()  # Return the integer represented by the given array of bytes. 将字节数组转换为整数
              # int.from_bytes(bytes, byteorder, *, signed=False) -> int
to_bytes()    # Return an array of bytes representing an integer. 将整数转换为字节数组表示
              # int.to_bytes(length, byteorder, *, signed=False) -> bytes
imag          # the imaginary part of a complex number. 一个复数的虚部
real          # the real part of a complex number. 一个复数的实数部分
denominator   # the denominator of a rational number in lowest terms. 分母有理数的
numerator     # the numerator of a rational number in lowest terms. 分子有理数的
"""


#浮点数
f = 3.14, f = float(12)
"""
as_integer_ratio()    # Return a pair of integers, whose ratio is exactly equal to the original 
                      # float and with a positive denominator. 将浮点数表示为两个整数的商。
                      # float.as_integer_ratio() -> (int, int)
                      # Raise OverflowError on infinities and a ValueError on NaNs.
conjugate()           # Return self, the complex conjugate of any float.
fromhex()             # Create a floating-point number from a hexadecimal string. 16进制字符串转换为浮点数。
                      # float.fromhex(string) -> float 
hex()                 # Return a hexadecimal representation of a floating-point number.
                      # float.hex() -> string
is_integer()          # Return True if the float is an integer.
imag                  #
real                  #
"""


#复数
