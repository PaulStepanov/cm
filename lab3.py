# -*- coding: utf-8 -*-
import numpy as np
import math
import common as cmn

xs = [-3, -2, -1, 0, 1, 2, 3]
ys = [2.6, -0.3, -2, -2.3, -1.5, 0.7, 3.2]
h = 1
n = 6


def least_square_linear(xs, ys):
    n = len(xs)

    a_1 = sum([xs[i] ** 2 for i in range(n)])
    b_1 = sum(xs)
    y_1 = sum([xs[i] * ys[i] for i in range(n)])
    a_2 = b_1
    b_2 = n
    y_2 = sum(ys)

    left_eq = np.array([[a_1, b_1], [a_2, b_2]])
    right_eq = np.array([y_1, y_2])

    [a, b] = np.linalg.solve(left_eq, right_eq)

    print("Полученая линейная функция", a, "* x +", format(b))
    return lambda x: a * x + b


def least_square_quadratic(xs, ys):
    n = len(xs)

    a_1 = sum([xs[i] ** 4 for i in range(n)])
    b_1 = sum([xs[i] ** 3 for i in range(n)])
    c_1 = sum([xs[i] ** 2 for i in range(n)])
    y_1 = sum([xs[i] ** 2 * ys[i] for i in range(n)])
    a_2 = b_1
    b_2 = c_1
    c_2 = sum(xs)
    y_2 = sum([xs[i] * ys[i] for i in range(n)])
    a_3 = c_1
    b_3 = c_2
    c_3 = n
    y_3 = sum(ys)

    left_eq = np.array([[a_1, b_1, c_1], [a_2, b_2, c_2], [a_3, b_3, c_3]])
    right_eq = np.array([y_1, y_2, y_3])

    [a, b, c] = np.linalg.solve(left_eq, right_eq)

    print("Полученая квадратичная функция", a, "*x^2 +", b, "*x +", c)
    return lambda x: a * x ** 2 + b * x + c


def least_square_cubic(xs, ys):
    n = len(xs)

    a_1 = sum([xs[i] ** 6 for i in range(n)])
    b_1 = sum([xs[i] ** 5 for i in range(n)])
    c_1 = sum([xs[i] ** 4 for i in range(n)])
    d_1 = sum([xs[i] ** 3 for i in range(n)])
    y_1 = sum([xs[i] ** 3 * ys[i] for i in range(n)])
    a_2 = b_1
    b_2 = c_1
    c_2 = d_1
    d_2 = sum([xs[i] ** 2 for i in range(n)])
    y_2 = sum([xs[i] ** 2 * ys[i] for i in range(n)])
    a_3 = b_2
    b_3 = c_2
    c_3 = d_2
    d_3 = sum(xs)
    y_3 = sum([xs[i] * ys[i] for i in range(n)])
    a_4 = b_3
    b_4 = c_3
    c_4 = d_3
    d_4 = n
    y_4 = sum(ys)

    left_eq = np.array([[a_1, b_1, c_1, d_1], [a_2, b_2, c_2, d_2], [a_3, b_3, c_3, d_3], [a_4, b_4, c_4, d_4]])
    right_eq = np.array([y_1, y_2, y_3, y_4])

    [a, b, c, d] = np.linalg.solve(left_eq, right_eq)

    print("Полученая кубическая функция", a, "*x^3 +", b, "*x^2 +", c, "*x+", d)
    return lambda x: a * x ** 3 + b * x ** 2 + c * x + d

# https://www.desmos.com/calculator/4fcpeogamr
[print("(", xs[i], ",", ys[i], ")") for i in range(n)]

calc_lsl = least_square_linear(xs, ys)
calc_lsq = least_square_quadratic(xs, ys)
calc_lsc = least_square_cubic(xs, ys)

lin_arr = [calc_lsl(x) for x in xs]
lin_error = sum([(ys[i] - lin_arr[i]) ** 2 for i in range(n)]) ** 0.5
print("Значение линейной функции", lin_arr)
print("Погрешность линейной функции", lin_error)

quadr_arr = [calc_lsq(x) for x in xs]
quadr_error = sum([(ys[i] - quadr_arr[i]) ** 2 for i in range(n)]) ** 0.5
print("Значение квадратичной функции", quadr_arr)
print("Погрешность квадратичной функции", quadr_error)

cubic_arr = [calc_lsc(x) for x in xs]
cubic_error = sum([(ys[i] - cubic_arr[i]) ** 2 for i in range(n)]) ** 0.5
print("Значение кубической функции", cubic_arr)
print("Погрешность кубической функции", cubic_error)
