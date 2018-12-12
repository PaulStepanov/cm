# -*- coding: utf-8 -*-
import numpy as np
import math
import common as cmn

# http://codetown.ru/matlab/chislennoe-differencirovanie/

h = 0.2
a = 0
b = 1


def get_xs_yx(func, a, b, h):
    x = a
    xs = []
    ys = []

    while x <= b:
        xs.append(x)
        ys.append(func(x))
        x += h

    return (xs, ys)


def function(x):
    return -1 * np.exp(x) + x ** 2


def first_derivative(x):
    return 2 * x - np.exp(x) * (1 + x) # 2 x - e^x (1 + x)


def second_derivative(x):
    return 2 - np.exp(x) * (2 + x) # 2 - e^x (2 + x)


def left(func, x_0, i, h):
    return (func(x_0 + h * i) - func(x_0 + h * (i - 1))) / h


def right(func, x_0, i, h):
    return (func(x_0 + h * (i + 1)) - func(x_0 + h * i)) / h


def middle(func, x_0, i, h):
    return (func(x_0 + h * (i + 1)) - func(x_0 + h * (i - 1))) / (2 * h)


def second(func, x_0, i, h):
    return (func(x_0 + h * (i + 1)) - 2 * func(x_0 + h * i) + func(x_0 + h * (i - 1))) / h ** 2


[f_xs, f_ys] = get_xs_yx(function, a, b, h)
n = int(1 / h + 1.5)
print("x:", f_xs)
print("f(x):", f_ys)
print("f'(x)", [first_derivative(x) for x in f_xs])
print("left f'(x)", [left(function, a, i, h) for i in range(n)])
print("right f'(x)", [right(function, a, i, h) for i in range(n)])
print("middle f'(x)", [middle(function, a, i, h) for i in range(n)])
print("f''(x)", [second_derivative(x) for x in f_xs])
print("second f'(x)", [second(function, a, i, h) for i in range(n)])
