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
hex()                 # Return a hexadecimal representation of a floating-point number. 以十六进制表示浮点数。
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
center()        # Return S centered in a string of length width. 字符居中，指定宽度和填充字符（默认为空格。
                # S.center(width[, fillchar]) -> str
count()         # Return the number of non-overlapping occurrences of substring sub in string S[start:end].
                # S.count(sub[, start[, end]]) -> int
encode()        # Encode S using the codec registered for encoding.
                # S.encode(encoding='utf-8', errors='strict') -> bytes
endswith()      # Return True if S ends with the specified suffix, False otherwise.
                # S.endswith(suffix[, start[, end]]) -> bool
startswith()    #
expandtabs()    # Return a copy of S where all tab characters are expanded using spaces. 把制表符tab("\t")转换为空格。
                # S.expandtabs(tabsize=8) -> str
find()          # Return the lowest index in S where substring sub is found,
                # S.find(sub[, start[, end]]) -> int
rfind()         #
format()        # Return a formatted version of S, using substitutions from args and kwargs.
                # S.format(*args, **kwargs) -> str
format_map()    # Return a formatted version of S, using substitutions from mapping.
                # S.format_map(mapping) -> str
index()         # Return the lowest index in S where substring sub is found,such that sub is contained within S[start:end].
                # S.index(sub[, start[, end]]) -> int
rindex()        # 
isalnum()       # Return True if all characters in S are alphanumeric and there is at least one character in S, False otherwise.
                # S.isalnum() -> bool
isalpha()       # 如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
                # S.isalpha() -> bool
isdecimal()     # 如果字符串是一个十进制正整数返回True，否则返回False。
isdigit()       # 如果字符串是一个正整数返回True，否则返回 False。
isidentifier()  # 判断是否为python中的标识符
isnumeric()     # 
isprintable()   # 判断引号里面的是否都是可打印的
isspace()       # 判断字符串里面都是空白位，空格或者tab
istitle()       # 判断字符串里面的字符是否都是大写开头
isupper()       #
islower()       #
join()          # 将字符串以指定的字符连接生成一个新的字符串
partition()     # 以指定字符分割，返回一个元组
rpartition()    # 以指定字符从右向左分割，只分割一次，返回元组，若没有指定的字符，则在返回的元组前面加两个空字符串
replace()       # 将指定的字符替换为新的字符，可指定替换的个数
ljust()         # 左对齐，可指定字符宽度和填充字符
rjust()         #  
split()         # 分割，可以以指定的字符分割，可指定分割的次数，默认从左向右分割，与partition不同的是，split分割后会删除指定的字符，
                # 默认以空格为分割符
rsplit()        #
splitlines()    # 字符串转换为列表
strip()         # 默认去除两边空白字符，可指定去除的字符，去除指定的字符后，会被空白占位。
lstrip()        #
rstrip()        # 
swapcase()      # 将字符串中的大小写互换
title()         # 
translate()     # 
upper()         #
lower()         #
zfill()         # 指定字符串宽度，不足的右边填“0”
maketrans       # Return a translation table usable for str.translate().
"""


#列表
l = [1,2,3], l = list(123)
"""

"""
