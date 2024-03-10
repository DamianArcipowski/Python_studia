def sequence_product(a1=1, b=4, amount=10):
    sum = a1
    for i in range(amount):
        sum *= b
    return sum

print(sequence_product())