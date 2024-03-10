import math

num = int(input('Wprowadz liczbe \n'))

try:
    num_sqrt = math.sqrt(num)
except Exception:
    print('Square root from a negative number')
else:
    print(num_sqrt)