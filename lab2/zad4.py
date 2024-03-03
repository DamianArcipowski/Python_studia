my_number = int(input('Wprowadź liczbę: '))
is_prime = False

for i in range(2, my_number - 1):
    if my_number % i == 0:
        print('Nie jest pierwsza')
        break
else:
    is_prime = True
    
if is_prime:
    print('Jest pierwsza')