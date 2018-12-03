import numpy as np
import matplotlib.pyplot as plt
import common


def B1(x):
    return (-1)*((-1) * x + 3)


def B2(x):
    return (-1)*(3 * x + 1)


def B3(x):
    return (-1)*(-4 * x + 5)


lin_space = np.linspace(0, 1, 100)
b1_lin_space = list(map(lambda x: B1(x), lin_space))
b2_lin_space = list(map(lambda x: B2(x), lin_space))
b3_lin_space = list(map(lambda x: B3(x), lin_space))
plt.plot(lin_space, b1_lin_space, label='A1')
plt.plot(lin_space, b2_lin_space, label='A2')
plt.plot(lin_space, b3_lin_space, label='A3')
dots = [(4/7, -19/7), (0.5, -2.5), (2/3, -7/3)]
common.renderDots(dots)
plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()