import numpy as np

def generate(base, index):
    return np.logspace(1, index, index, base=base)

print(generate(2, 4))