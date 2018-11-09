# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 21:36:39 2018

@author: Lukasz
"""

#def ask_ok (prompt, retries = 4, reminder = 'Try again!'):
#    while True:
#        ok = input(prompt)
#        if ok in ('y', 'ye', 'yes'):
#            return True
#            #reminder = 'Correct Response'
#        if ok in ('n', 'no', 'nop', 'nope'):
#            return False
#        retries = retries-1
#        if retries == 0:
#            raise ValueError('Invalid Response')
#        print(reminder)

n = 1

while n < 10:
    print(n)
    n = n+1

def ask_ok (prompt, retries = 4, reminder = 'Try again!'):
    x = False
    while x == False:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            x = True
            reminder = 'Correct Response'
        elif ok in ('n', 'no', 'nop', 'nope'):
            x = False
        retries = retries-1
        if retries == 0:
            raise ValueError('Invalid Response')
        print(reminder)
