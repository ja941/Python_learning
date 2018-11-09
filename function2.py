# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 21:23:37 2018

@author: Lukasz
"""

def fib2(n):  # return Fibonacci series up to n

    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
