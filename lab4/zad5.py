import numpy as np

def create_diagonal_matrix(vec_length):
    vector = [x for x in range(vec_length)]
    reversed_vector = vector[::-1]
    return np.diag(reversed_vector)
    
print(create_diagonal_matrix(4))