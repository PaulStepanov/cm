# -*- coding: utf-8 -*-
import numpy as np
import math
import common as cmn


# http://www.cleverstudents.ru/articles/mnk.html
def least_square_algorithm(points_x, points_y):
    sum_x = sum_y = sum_xy = sum_xx = 0

    count = len(points_x)
    for i in range(0, count):
        sum_x += points_x[i]
        sum_y += points_y[i]
        sum_xy += points_x[i] * points_y[i]
        sum_xx += points_x[i] * points_x[i]

    a_multiplier = (sum_xy - sum_x * sum_y / count) / (sum_xx - sum_x * sum_x / count)
    b_multiplier = sum_y / count - a_multiplier * sum_x / count

    error_sum = 0

    for i in range(1, count):
        error_sum += math.pow(points_y[i] - b_multiplier - a_multiplier * points_x[i], 2)

    determinant = count * sum_xx - math.pow(sum_x, 2)

    i = 1.0 / (count - 2.0) * error_sum

    error_a = math.sqrt(i / determinant * sum_xx)
    error_b = math.sqrt(count / determinant * i)

    return (a_multiplier, b_multiplier, error_a, error_b, lambda x: a_multiplier * x + b_multiplier)


points_x = [-3, -2, -1, 0, 1, 2, 3]
points_y = [2.6, -0.3, -2, -2.3, -1.5, 0.7, 3.2]

a_multiplier, b_multiplier, error_a, error_b, calculate = least_square_algorithm(points_x, points_y)
print("a_multiplier:", a_multiplier, " b_multiplier:", b_multiplier, " error_a:", error_a, " error_b:", error_b+)
