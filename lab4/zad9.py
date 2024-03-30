import numpy as np

fibonacci_numbers = []

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        fibonacci_numbers.append(a) 
        a += b
        b = a - b
        
def create_matrix(n):
    return np.array(fibonacci_numbers).reshape((n, n))

fibonacci(25)

print(create_matrix(5))