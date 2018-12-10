# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import common

# general
points = [1.33, 2.55]


def my_func(x):
    return 0.2 * np.power(x + 2, 2) + 0.25 * np.exp(x)


interval_points = np.arange(0.0, 6.0, 1.0)
calculated_values = list(map(my_func, points))


# lagrange http://mathworld.wolfram.com/LagrangeInterpolatingPolynomial.html
def lagrange_polynomial_2(points, x, isPrint = False):
    nearest_points = find_nearest_points(points, x)
    x1 = nearest_points[0]
    x2 = nearest_points[1]
    x3 = nearest_points[2]
    y1 = my_func(x1)
    y2 = my_func(x2)
    y3 = my_func(x3)

    if isPrint:
        print("lagrange_polynomial 2", "x1:", x1, "x2:", x2, "x3:", x3, "y1:", y1, "y2:", y2 , "y3:", y3)
    return (x - x2) * (x - x3) * y1 / (x1 - x2) / (x1 - x3) + (x - x1) * (x - x3) * y2 / (x2 - x1) / (x2 - x3) + (
            x - x1) * (x - x2) * y3 / (x3 - x1) / (x3 - x2)


def lagrange_polynomial_3(points, x, isPrint=False):
    nearest_points = find_nearest_points(points, x, 4)
    x1 = nearest_points[0]
    x2 = nearest_points[1]
    x3 = nearest_points[2]
    x4 = nearest_points[3]

    y1 = my_func(x1)
    y2 = my_func(x2)
    y3 = my_func(x3)
    y4 = my_func(x4)


    if isPrint:
        print("lagrange_polynomial 3", "x1:", x1, "x2:", x2, "x3:", x3, "x4:", x4,"y1:", y1, "y2:", y2, "y3:" , y3, "y4:", y4)

    return (x-x2)*(x-x3)*(x-x4)*y1/(x1-x2)/(x1-x3)/(x1-x4) + (x-x1)*(x-x3)*(x-x4)*y2/(x2-x1)/(x2-x3)/(x2-x4) + (x-x1)*(x-x2)*(x-x4)*y3/(x3-x1)/(x3-x2)/(x3-x4) + (x-x1)*(x-x2)*(x-x3)*y4/(x4-x1)/(x4-x2)/(x4-x3)

def lagrange_polynomial_4(points, x, isPrint=False):
    nearest_points = find_nearest_points(points, x, 5)
    x1 = nearest_points[0]
    x2 = nearest_points[1]
    x3 = nearest_points[2]
    x4 = nearest_points[3]
    x5 = nearest_points[4]

    y1 = my_func(x1)
    y2 = my_func(x2)
    y3 = my_func(x3)
    y4 = my_func(x4)
    y5 = my_func(x5)


    if isPrint:
        print("lagrange_polynomial 4", "x1:", x1, "x2:", x2, "x3:", x3, "x4:", x4, "x5:", x5, "y1:", y1, "y2:", y2, "y3:" , y3, "y4:", y4, "y5:", y5,"y6:", y6, )

    return (x-x2)*(x-x3)*y1*(x-x4)*(x-x5)/(x1-x2)/(x1-x3)/(x1-x5)/(x1-x4)+(x-x1)*(x-x3)*y2*(x-x4)*(x-x5)/(x2-x4)/(x2-x5)/(x2-x1)/(x2-x3)+(x-x1)*(x-x2)*(x-x4)*(x-x5)*y3/(x3-x4)/(x3-x5)/(x3-x1)/(x3-x2)+(x-x1)*(x-x2)*(x-x3)*(x-x5)*y4/(x4-x1)/(x4-x2)/(x4-x3)/(x4-x5)+(x-x1)*(x-x2)*(x-x3)*(x-x4)*y5/(x5-x1)/(x5-x2)/(x5-x3)/(x5-x4)

def lagrange_polynomial_5(points, x, isPrint=False):
    nearest_points = find_nearest_points(points, x, 6)
    x1 = nearest_points[0]
    x2 = nearest_points[1]
    x3 = nearest_points[2]
    x4 = nearest_points[3]
    x5 = nearest_points[4]
    x6 = nearest_points[5]


    y1 = my_func(x1)
    y2 = my_func(x2)
    y3 = my_func(x3)
    y4 = my_func(x4)
    y5 = my_func(x5)
    y6 = my_func(x6)

    if isPrint:
        print("lagrange_polynomial 5", "x1:", x1, "x2:", x2, "x3:", x3, "x4:", x4, "x5:", x5, "x6:", x6,"y1:", y1, "y2:", y2, "y3:" , y3, "y4:", y4, "y5:", y5)

    return (x-x2)*(x-x3)*(x-x4)*(x-x5)*(x-x6)*y1/(x1-x2)/(x1-x3)/(x1-x4)/(x1-x5)/(x1-x6) + (x-x1)*(x-x3)*(x-x4)*(x-x5)*(x-x6)*y2/(x2-x1)/(x2-x3)/(x2-x4)/(x2-x5)/(x2-x6) + (x-x1)*(x-x2)*(x-x4)*(x-x5)*(x-x6)*y3/(x3-x1)/(x3-x2)/(x3-x4)/(x3-x5)/(x3-x6) + (x-x1)*(x-x2)*(x-x3)*(x-x5)*(x-x6)*y4/(x4-x1)/(x4-x2)/(x4-x3)/(x4-x5)/(x4-x6) + (x-x1)*(x-x2)*(x-x3)*(x-x4)*(x-x6)*y5/(x5-x1)/(x5-x2)/(x5-x3)/(x5-x4)/(x5-x6) + (x-x1)*(x-x2)*(x-x3)*(x-x4)*(x-x5)*y6/(x6-x1)/(x6-x2)/(x6-x3)/(x6-x4)/(x6-x5)

# utils
def find_nearest_points(points, point, n=3):
    tuples_arr = list(map(lambda x: (x, np.abs(x - point)), points))

    return sorted(map(lambda x: x[0],
                      sorted(tuples_arr,
                             key=lambda x: x[1])[:n]))


def find_diff(arr1, arr2):
    zipped_tuples = list(zip(arr1, arr2))
    return list(map(lambda t: np.abs(t[0] - t[1]), zipped_tuples))


lagrange_polynomials = list(map(lambda p: lagrange_polynomial_3(interval_points, p, True), points))
lagrange_polynomials5 = list(map(lambda p: lagrange_polynomial_5(interval_points, p, True), points))

print("значение функции", list(calculated_values))
print("полиномы лагранжа 3", list(lagrange_polynomials))
print("точность лагранжа 3", find_diff(calculated_values, lagrange_polynomials))
print("полиномы лагранжа 5", list(lagrange_polynomials5))
print("точность лагранжа 5", find_diff(calculated_values, lagrange_polynomials5))


lin_space = np.linspace(0, 2.6, 1000)
function_lin_space = list(map(lambda x: my_func(x), lin_space))
lagrange_lin_space = list(map(lambda x: lagrange_polynomial_3(interval_points, x), lin_space))
lagrange_lin_space_5 = list(map(lambda x: lagrange_polynomial_5(interval_points, x), lin_space))

plt.plot(lin_space, function_lin_space, label='функции')
plt.plot(lin_space, lagrange_lin_space, label='лагранжа 3')
plt.plot(lin_space, lagrange_lin_space_5, label='лагранжа 5')

common.renderDots(zip(points, calculated_values))


plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()
