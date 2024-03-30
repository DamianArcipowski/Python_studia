import numpy as np

def split_matrix(matrix, direction):
    num_rows, num_cols = matrix.shape

    if direction == 'horizontal':
        if num_rows % 2 == 0:
            return np.split(matrix, num_rows / 2, axis=0)[0]
        else:
            return 'This matrix can not be splitted horizontally'
            
    elif direction == 'vertical':
        if num_cols % 2 == 0:
            return np.split(matrix, num_cols / 2, axis=1)[0]
        else:
            return 'This matrix can not be splitted vertically'
    
    else:
        return 'Improper value'
    
    
my_matrix = np.full((4, 4), 0)

print(split_matrix(my_matrix, 'horizontal'))