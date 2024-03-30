import numpy as np

def create_diag_matrix(n):
    diag_values = [2] * n
    diag_matrix = np.diag(diag_values)
    
    for i in range(n):
        for j in range(n):
            if i == 0:
                diag_matrix[i, j] = j * 2 + 2
            if j == 0:
                diag_matrix[i, j] = i * 2 + 2
            if i == n - 1:
                diag_matrix[i, j] = (i - j) * 2 + 2
            if j == n - 1:
                diag_matrix[i, j] = (j - i) * 2 + 2
            
    return diag_matrix
    
    
print(create_diag_matrix(3))