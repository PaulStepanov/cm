import numpy as np
import matplotlib.pyplot as plt
import common


def B1(x):
    return 5 * x + 1


def B2(x):
    return -2 * x + 4


def B3(x):
    return -6 * x + 7


lin_space = np.linspace(0, 1, 100)
b1_lin_space = list(map(lambda x: B1(x), lin_space))
b2_lin_space = list(map(lambda x: B2(x), lin_space))
b3_lin_space = list(map(lambda x: B3(x), lin_space))
plt.plot(lin_space, b1_lin_space, label='B1')
plt.plot(lin_space, b2_lin_space, label='B2')
plt.plot(lin_space, b3_lin_space, label='B3')
dots = [(3/7, 15/7+1), (3/4, -3/2+4)]
common.renderDots(dots)
plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()