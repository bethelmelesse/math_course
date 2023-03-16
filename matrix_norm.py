import numpy as np
import math

def l1_matrix_norm(A):
    abs_x = np.absolute(A)
    column_sum = np.sum(abs_x, axis=0)
    value = np.max(column_sum)
    return value

def l_inf_matrix_norm(A):
    abs_x = np.absolute(A)
    row_sum = np.sum(abs_x, axis=1)
    value = np.max(row_sum)
    return value

def l2_matrix_norm(A):
    sq_A = np.square(A)
    summed = np.sum(sq_A)
    value = math.sqrt(summed)
    return value

A = np.array([[1, -7], [-2,-3]])
l1_matrix_norm_value = l1_matrix_norm(A)
l_inf_matrix_norm_value = l_inf_matrix_norm(A)
l2_matrix_norm_value = l2_matrix_norm(A)

print(l1_matrix_norm_value)
print(l_inf_matrix_norm_value)
print(l2_matrix_norm_value)

