# -*- coding: utf-8 -*-
import numpy as np

a = 0
b = 2
n = 5


def function(x):
    return x / ((x + 3) ** 2)


def F(x):
    return 3 / (x + 3) + np.log(x + 3)


# https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%BF%D1%80%D1%8F%D0%BC%D0%BE%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD8B_%D0%B4%D0%BB%D1%8F_%D1%80%D0%B0%D0%B2%D0%BD%D0%BE%D0%BC%D0%B5%D1%80%D0%BD%D1%8B%D1%85_%D1%81%D0%B5%D1%82%D0%BE%D0%BA%D0%B8%D0%BA%D0%BE%D0%B2#%D0%A1%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%BD%D1%8B%D0%B5_%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D1%
def square_method_right(a, b, n):
    sum = 0
    h = (b - a) / n

    for i in range(1, n + 1):
        x = a + i * h
        sum += function(x)
        # print("smr", function(x))
    sum *= h
    return sum


def square_method_left(a, b, n):
    sum = 0
    h = (b - a) / n

    for i in range(0, n):
        x = a + i * h
        sum += function(x)
        # print("sml", function(x))

    sum *= h
    return sum


def square_method_middle(a, b, n):
    sum = 0
    h = (b - a) / n

    for i in range(1, n + 1):
        x = a + i * h
        sum += function(x - h / 2)
        # print("smm", function(x - h / 2))
    sum *= h
    return sum


def porabol_method(a, b, n):
    f_2t_1 = 0
    f_2t = 0
    h = (b - a) / n / 2

    for i in range(0, n * 2 + 1, 2):
        if i != 0:
            f_2t_1 += function(a + i * h)
        if i + 1 <= n * 2:
            f_2t += function(a + (i + 1) * h)

    sum = function(a) + 4 * f_2t + 2 * f_2t_1 + function(a + 4 * h)
    sum *= h / 3
    return sum


def trapeze_method(a, b, n):
    sum = 0
    h = (b - a) / n

    for i in range(1, n):
        sum += 2 * function(a + i * h)

    # print("function(a)", function(a))
    # print("sum", sum)
    # print("function(b)", function(b))

    return (h / 2) * (function(a) + sum + function(b))

# http://www.math.tsu.ru/sites/default/files/mmf2/e-resources/Dit_An.pdf
def gauss(a, b):
    x = [-0.932469514,
         -0.661209386,
         -0.238619186,
         0.238619186,
         0.661209386,
         0.932469514]
    c = [0.171324492,
         0.360761573,
         0.467913935,
         0.467913935,
         0.360761573,
         0.171324492]

    f_x = 0
    for i in range(6):
        t = (b - a) / 2 * x[i] + (b + a) / 2
        f_x += c[i] * function(t)
    return (b - a) / 2 * f_x

def newton(a, b):
    return F(b) - F(a)


h = (b - a) / n
print("h", h)
print("square_method_left", square_method_left(a, b, n))
print("square_method_right", square_method_right(a, b, n))
print("square_method_middle", square_method_middle(a, b, n))
print("trapeze_method", trapeze_method(a, b, n))
print("porabol_method", porabol_method(a, b, n))
print("gauss_method", gauss(a, b))
print("newton method", newton(a,b))

