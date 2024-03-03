perfect_numbers_amount = 0
factors_arr = []

for i in range(1, 1000):
    for j in range(1, i - 1):
        if i % j == 0:
            factors_arr.append(j)
    factors_sum = sum(factors_arr)
    if factors_sum == i:
        perfect_numbers_amount += 1
    factors_arr.clear()
    
print(perfect_numbers_amount)