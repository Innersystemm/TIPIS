import numpy as np
import matplotlib.pyplot as plt
import math as math
import sympy as sp

interval = (1, 3)
begin_approx = (1, 3)
eps = 0.00001


def func(x):
    return pow(x, 5) - x - 0.2


def chord_approx(a, b):
    return a - func(a) * (b - a) / (func(b) - func(a))


def chord_start():
    a, b = interval
    while True:
        c = chord_approx(a, b)
        f_c = func(c)
        if c - a < eps or b - c < eps:
            return c, f_c
        if np.sign(f_c) == np.sign(func(a)):
            a = c
        else:
            b = c


# x0 = x(k-1), x1 = xk
def secants_approx(x0, x1):
    if func(x0) * func(x1) < 0:
        return None
    return x1 - func(x1) / (func(x1) - func(x0) / x1 - x0)


def secants_start():
    x0, x1 = begin_approx
    n = 0
    while True:
        if np.abs(x1 - x0) < eps:
            return x1, n
        tmp = x1
        x1 = secants_approx(x0, x1)
        x0 = tmp
        n += 1


def draw_func(x_range):
    y = []
    x_min, x_max = x_range
    for x in range(x_min, x_max):
        y.append(func(x))
    plt.plot(range(x_min, x_max), y, linewidth=1.0)
    plt.title('График функции x^5 - x - 0.2')
    plt.grid(True)
    plt.show()


def find_roots():
    x, y, z, t = sp.symbols('x y z t')
    roots_eq = [rt for rt in sp.solveset(pow(x, 5) - x - 0.2, x)]
    print(roots_eq)
    xs = []
    ys = []
    for rt in roots_eq:
        if type(rt) is not sp.Float:
            continue
        current = rt - 0.5
        step = 0.1
        while current < rt + 0.5:
            xs.append(current)
            ys.append(func(current))
            current += step
            plt.plot(xs, ys)
            plt.title("x = {0}".format(rt))
            plt.grid(True)
        plt.show() 
        xs.clear()
        ys.clear()

# i_a, i_b = interval
# c_val, c_func_val = chord_start()
# print("c = {0}, f(c) = {1}".format(c_val, c_func_val))
#
# s_x, s_n = begin_approx
# print("x = {0}, n = {1}".format(s_x, s_n))

draw_func((-10, 10))


find_roots()
