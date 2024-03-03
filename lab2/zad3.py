word = input('Wprowadź słowo do sprawdzenia: ')
reversed_word = word[::-1]
if word == reversed_word:
    print('Jest palindromem')
else:
    print('Nie jest palindromem')