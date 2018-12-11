# -*- coding: utf-8 -*-
import numpy as np
import math
import common as cmn
import matplotlib.pyplot as plt


TOMAS_A = 1
TOMAS_B = 4
TOMAS_C = 1

# http://www.machinelearning.ru/wiki/index.php?title=%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BF%D0%BE%D0%BB%D1%8F%D1%86%D0%B8%D1%8F_%D0%BA%D1%83%D0%B1%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%BC%D0%B8_%D1%81%D0%BF%D0%BB%D0%B0%D0%B9%D0%BD%D0%B0%D0%BC%D0%B8


func = lambda x: x - np.sqrt(np.log(x + 2))

h = 0.2
x0 = 0.0
xn = 1
n = 5
x = []
for i in np.arange(x0, xn + h + h, h):
    x += [i]
y = []
for i in x:
    y += [func(i)]

print("x", x)
print("y", y)

points = (x0 + 0.5 * h, 0.5 * x0 + 0.5 * xn, xn - 0.5 * h)


def thomas_algorithm(a, c, b, f):
    def alpha(x, i):
        new_val = (-b[i]) / (a[i - 1] * x[-1] + c[i])
        return x + [new_val]

    def beta(x, i):
        new_val = (f[i] - a[i - 1] * x[-1]) / (a[i - 1] * alphas[i] + c[i])
        return x + [new_val]

    def find_xi(x, i):
        new_val = alphas[i + 1] * x[-1] + betas[i + 1]
        return x + [new_val]

    n = len(a)
    init_aplha = [0.0, -b[0] / c[0]]

    alphas = cmn.foldl(alpha, init_aplha, range(1, n))

    init_beta = [0.0, f[0] / c[0]]

    betas = cmn.foldl(beta, init_beta, range(1, n))

    xn = (f[n] - a[n - 1] * betas[n]) / (a[n - 1] * alphas[n] + c[n])

    coefficients = list(reversed(cmn.foldl(find_xi, [xn], range(n - 1, -1, -1))))

    return coefficients


def init_thomas_algorithm(n, a, b, c, f):
    thomas_a = np.full(n - 1, a)
    thomas_b = np.full(n, b)
    thomas_c = np.full(n - 1, c)

    return thomas_algorithm(thomas_a, thomas_b, thomas_c, f)


def find_nearest_point_index(points, point):
    touples = []

    for i in range(0, len(points)):
        p = points[i]
        touples += [(i,p)]

    return list(filter(lambda tp: point < tp[1], touples))[0][0]

def get_spline_coefficients(y, h, n):
    def find_f(i):
        return 6 * (y[i + 1] - 2 * y[i] + y[i - 1]) / h / h

    def find_d(i):
        return (c[i] - c[i - 1]) / h

    def find_b(i):
        return (c[i] * h / 2) - \
               ((d[i] * h ** 2) / 6.0) + \
               ((y[i] - y[i - 1]) / h)

    f_list = []
    for i in range(1, n + 1):
        f_list += [find_f(i)]

    c = [0.0] + init_thomas_algorithm(n, TOMAS_A, TOMAS_B, TOMAS_C, f_list)

    d = [0.0]
    for i in range(1, n + 1):
        d += [find_d(i)]

    b = [0.0]
    for i in range(1, n + 1):
        b += [find_b(i)]

    a = y[:-1]

    return (a, b, c, d)


def get_spline_coefficients_by_index(y, h, n, i):
    coefficients = get_spline_coefficients(y, h, n)

    coefficients_dict = {
        "a": coefficients[0][1:][i],
        "b": coefficients[1][1:][i],
        "c": coefficients[2][1:][i],
        "d": coefficients[3][1:][i],
    }

    return coefficients_dict


# https://ru.wikipedia.org/wiki/%D0%9A%D1%83%D0%B1%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%BF%D0%BB%D0%B0%D0%B9%D0%BD#%D0%9F%D0%BE%D1%81%D1%82%D1%80%D0%BE%D0%B5%D0%BD%D0%B8%D0%B5
def get_interpolar_spline(xs, point):
    nearest_point_index = find_nearest_point_index(xs, point)
    coefficients = get_spline_coefficients_by_index(y, h, n, nearest_point_index)
    # print("x:", point, "nearest:", nearest_point_index, "c:", coefficients)
    spline = coefficients["a"] + coefficients["b"] * (point - xs[nearest_point_index]) + coefficients["c"] * math.pow(
        point - xs[nearest_point_index], 2) + \
             coefficients["d"] * math.pow(point - xs[nearest_point_index], 3)

    return spline



lin_space = np.linspace(0, 0.9, 1000)
function_lin_space = list(map(lambda x: func(x), lin_space))
plt.plot(lin_space, function_lin_space, label='функции')

for point in points:
    print("in point:", point, "f(x):", func(point), " spline=", get_interpolar_spline(x[1:][:-1], point))

space = list(map(lambda mx: get_interpolar_spline(x[1:][:-1], mx), lin_space))
plt.plot(lin_space, space, label='сплайн:')
plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()