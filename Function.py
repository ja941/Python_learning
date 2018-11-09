# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 19:19:57 2018

@author: Lukasz
"""


def Fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

#fib200 = Fib(200)

f100 = Fib(100)

#print(f(100))