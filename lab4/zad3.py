import numpy as np

def create_matrix(n):
    return np.arange(1, n * n + 1, 1).reshape((n, n))

print(create_matrix(5))