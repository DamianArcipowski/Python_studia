counter = 0
even_numbers_arr = []

while counter < 10:
    temp = int(input('Wprowadź liczbę: '))
    if temp % 2 == 0:
        even_numbers_arr.append(temp)
    counter += 1    
    
print(even_numbers_arr)