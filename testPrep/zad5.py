import numpy as np

def create_matrix_and_sum_rows(n):
    my_matrix = np.random.randint(50, size=(n, n))
    return my_matrix.sum(axis=1)

print(create_matrix_and_sum_rows(4))