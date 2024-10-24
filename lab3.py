# -*- coding: utf-8 -*-
import math as m
x1 = 3
xn = 7
step_x = 0.2
a = 1.9
b = 1.1


def fx(x):
    return m.sqrt((a * x) / (b + m.cos(x)**2))


n = x1
while not n >= xn:
    n += step_x
    print('x= ', round(n, 3), 'f(x) = ', round(fx(n), 7))
    
    

