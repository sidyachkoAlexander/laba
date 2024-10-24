# -*- coding: utf-8 -*-
import math as m
b = True
a = 0
x, y = float(input('x=')), float(input('y='))   
hp1 = x/y > 0                                   
hp2 = x/y < 0


def fx1(y):
    return m.sinh(m.radians(y))              


def fx2(y):
    return x**(m.exp(x))                 


def fx3(x):
    return x**y                                 



while b:
    gh = input('f1 == 1, f2 == 2, f3 == 3: ')
    if gh == '1':
        a = fx1(y)
        b = False
    elif gh == '2':
        a = fx2(y)
        b = False
    elif gh == '3':
        a = fx3(x)
        b = False
    else:
        print('Invalid input')
        gh = ''

if hp1:
    c = (a + m.log(y))**3    
elif hp2:
    c = m.log(abs(m.sin(y)))**3
else:
    c = m.sqrt(a)**3 + y  
print('c=', c)

