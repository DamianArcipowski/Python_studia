import numpy as np
import random
import string

word_1 = ['P', 'Y', 'T', 'H', 'O', 'N']
word_2 = ['P', 'A', 'N', 'D', 'A', 'S']
word_3 = ['P', 'U', 'K', 'C', 'A', 'B']

matrix = np.diag(word_1)

for i in range(0, len(word_2)):
    matrix[0][i] = word_2[i]
    
for i in range(0, len(word_3)):
    matrix[i][0] = word_3[i]
    
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if matrix[i][j] == '':
            randomLetter = random.choice(string.ascii_letters)
            matrix[i][j] = randomLetter.upper()

print(matrix)