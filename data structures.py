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
c = 1+2j, c = complex(2,3)
"""
conjugate()    # Return the complex conjugate of its argument. (3-4j).conjugate() == 3+4j. 返回该复数的共轭复数对象。
imag           # the imaginary part of a complex number
real           # the real part of a complex number
"""


#分数

#字符串
s = '123', s = str(123)
"""
capitalize()    # Return a capitalized version of S, i.e. make the first character have upper case and the rest lower case.
                # S.capitalize() -> str
                # 返回首字母大写，其他小写
casefold()      # Return a version of S suitable for caseless comparisons.
                # S.casefold() -> str
center()        # Return S centered in a string of length width.
                # S.center(width[, fillchar]) -> str
count()         # Return the number of non-overlapping occurrences of substring sub in string S[start:end].
                # S.count(sub[, start[, end]]) -> int
encode()        # Encode S using the codec registered for encoding.
                # S.encode(encoding='utf-8', errors='strict') -> bytes
endswith()      # Return True if S ends with the specified suffix, False otherwise.
                # S.endswith(suffix[, start[, end]]) -> bool
expandtabs()    # Return a copy of S where all tab characters are expanded using spaces.
                # S.expandtabs(tabsize=8) -> str
find()          # Return the lowest index in S where substring sub is found,
                # S.find(sub[, start[, end]]) -> int
format()        # Return a formatted version of S, using substitutions from args and kwargs.
                # S.format(*args, **kwargs) -> str
format_map()    # Return a formatted version of S, using substitutions from mapping.
                # S.format_map(mapping) -> str
index()         # Return the lowest index in S where substring sub is found,such that sub is contained within S[start:end].
                # S.index(sub[, start[, end]]) -> int
isalnum()       # Return True if all characters in S are alphanumeric and there is at least one character in S, False otherwise.
                # S.isalnum() -> bool
isalpha()       # 
"""
#列表
l = [1,2,3], l = list(123)
"""

"""
