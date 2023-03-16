import numpy as np 
import math

def l1_norm(x):
    abs_x = np.absolute(x)
    value = np.sum(abs_x)
    return value


def l2_norm(x):
    sq_x = np.square(x)
    summed = np.sum(sq_x)
    value = math.sqrt(summed)
    return value


def l_inf_norm(x):
    abs_x = np.absolute(x)
    value = np.max(abs_x)
    return value

def lp_norm(x, p):

    if p % 2 != 0:
        x = np.absolute(x)

    x_p = np.power(x, p)
    summed = np.sum(x_p)
    value = np.power(summed, 1/p)
    return value

x = np.array([5,-6])

l1_norm_value = l1_norm(x)
l2_norm_value = l2_norm(x)
l_inf_norm_value = l_inf_norm(x)
lp_norm_value = lp_norm(x, 2)

print(l1_norm_value)
print(l2_norm_value)
print(l_inf_norm_value)
print(lp_norm_value)


