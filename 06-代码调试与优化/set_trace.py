#!/usr/bin/env python
# encoding: utf-8

import pdb

def func(x, y):
    return x * y


def test():
    a = 2
    b = 3
    pdb.set_trace()
    ret = func(a, b)
    if ret > 10:
        print(ret)
    else:
        a = a + 1
        b = b + a
    pdb.set_trace()
    print(a, b)

test()

# ll 查看当前函数的代码
# j  跳到某行，向前、向后都可以，向前是代码未执行部分，向后是已执行部分，但不可跳到while、try、for代码块中间。
#    已执行过的参数不会再变化
# p  打印变量，pp：pretty-print
# w  where 打印当前函数调用栈
