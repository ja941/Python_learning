# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 23:04:01 2018

@author: Lukasz
"""

#list = ['bwipo', 'broxah', 'caps', 'rekkles', 'hylisang']
#
#print('long and short players names:\n')
#
#for i in list:
#    if len(i)>5:
#        print(i)
#    else:
#        print(i + ' - name shorter than 6 letters (' + str(len(i)) + ')')
#
#
## infinite loop?
#
## for i in list:
##    if len(i)==7:
##        list.insert(0, i)
#
#
## correct loop
#
#for i in list[:]:
#    if len(i)==7:
#        list.insert(0, i)
#
#print('\n'+str(list))


# break/continue/else

for n in range(2, 21):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
#
#for num in range(2,22):
#    if num % 2 == 0:
#        print('Found an even number: ', num)
#        continue
#    print('Found an odd number: ', num)


input()

#while True:
#    pass
