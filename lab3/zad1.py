A = [x for x in range(1, 11)]
B = [4 ** x for x in range(0, 8)]
C = [x for x in B if x % 2 == 0]

print(A)
print(B)
print(C)