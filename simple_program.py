# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 22:44:22 2018

@author: Lukasz
"""

import datetime as dt

print('What is your name?')

MyName = input()

print('Hello ' + MyName)

print('What is your age?')

myAge = input()

if int(myAge) <= 18:
    print('You\'re not adult, yet!')

else:
    print('You are born in ' + str(int(dt.datetime.now().year) - int(myAge)))
