import numpy as np 
import math

def l1_distance(x, y):
    subs = np.subtract(x, y)
    abs_x = np.absolute(subs)
    value = np.sum(abs_x)
    return value


def l2_distance(x, y):
    subs = np.subtract(x, y)
    sq_x = np.square(subs)
    summed = np.sum(sq_x)
    value = math.sqrt(summed)
    return value


def l_inf_distance(x, y):
    subs = np.subtract(x, y)
    abs_x = np.absolute(subs)
    value = np.max(abs_x)
    return value

def lp_distance(x, y, p):
    subs = np.subtract(x, y)
    if p % 2 != 0:
        subs = np.absolute(subs)

    x_p = np.power(subs, p)
    summed = np.sum(x_p)
    value = np.power(summed, 1/p)
    return value


x = np.array([5,-6])
y = np.array([10,-2])

l1_distance_value = l1_distance(x, y)
l2_distance_value = l2_distance(x, y)
l_inf_distance_value = l_inf_distance(x, y)
lp_distance_value = lp_distance(x, y, 2)

print(l1_distance_value)
print(l2_distance_value)
print(l_inf_distance_value)
print(lp_distance_value)

