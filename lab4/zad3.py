import numpy as np

def create_matrix(n):
    return np.full((n, n), [i for i in range(1, n)])

print(create_matrix(3))