# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# general
points = [0.27, 0.62, 0.89]


def my_func(x):
    return x - np.sqrt(np.log(x + 2))


interval_points = np.arange(0.0, 1.0, 0.2)
calculated_values = list(map(my_func, points))


# lagrange http://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html
def lagrange_polynomial(points, x):
    nearest_points = find_nearest_points(points, x)
    x1 = nearest_points[0]
    x2 = nearest_points[1]
    x3 = nearest_points[2]
    y1 = my_func(x1)
    y2 = my_func(x2)
    y3 = my_func(x3)

    return (x - x2) * (x - x3) * y1 / (x1 - x2) / (x1 - x3) + (x - x1) * (x - x3) * y2 / (x2 - x1) / (x2 - x3) + (
            x - x1) * (x - x2) * y3 / (x3 - x1) / (x3 - x2)


# newton http://mathfaculty.fullerton.edu/mathews/n2003/NewtonPolyMod.html
def seq2(x0, x1, f):
    return (f(x1) - f(x0)) / (x1 - x0)


def seq3(x0, x1, x2, f):
    return (seq2(x1, x2, f) - seq2(x0, x1, f)) / (x2 - x0)


def seq4(x0, x1, x2, x3, f):
    return (seq3(x1, x2, x3, f) - seq3(x0, x1, x2, f)) / (x3 - x0)


def newton_polynomial(points, x, f):
    nps = find_nearest_points(points, x, 4)
    x0 = nps[0]
    x1 = nps[1]
    x2 = nps[2]
    x3 = nps[3]
    return f(x0) + seq2(x0, x1, f) * (x - x0) + seq3(x0, x1, x2, f) * (x - x0) * (x - x1) + seq4(x0, x1, x2, x3, f) * (
            x - x0) * (x - x1) * (x - x2)


# utils
def find_nearest_points(points, point, n=3):
    tuples_arr = list(map(lambda x: (x, np.abs(x - point)), points))

    return sorted(map(lambda x: x[0],
                      sorted(tuples_arr,
                             key=lambda x: x[1])[:n]))


def find_diff(arr1, arr2):
    zipped_tuples = list(zip(arr1, arr2))
    return list(map(lambda t: np.abs(t[0] - t[1]), zipped_tuples))


lagrange_polynomials = list(map(lambda p: lagrange_polynomial(interval_points, p), points))
newton_polynomials = list(map(lambda p: newton_polynomial(interval_points, p, my_func), points))
print("значение функции", list(calculated_values))
print("полиномы лагранжа", list(lagrange_polynomials))
print("точность лагранжа", find_diff(calculated_values, lagrange_polynomials))
print("полиномы ньютона", list(newton_polynomials))
print("точность ньютона", find_diff(calculated_values, newton_polynomials))

lin_space = np.linspace(0, 1, 1000)
function_lin_space = list(map(lambda x: my_func(x), lin_space))
lagrange_lin_space = list(map(lambda x: lagrange_polynomial(interval_points, x), lin_space))
newton_lin_space = list(map(lambda p: newton_polynomial(interval_points, p, my_func), lin_space))
plt.plot(lin_space, function_lin_space, label='функции')
plt.plot(lin_space, lagrange_lin_space, label='лагранжа')
plt.plot(lin_space, newton_lin_space, label='ньютона')
plt.plot(points, calculated_values, label='точки', marker='X')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()
