try:
    a = int(input("Wprowadz a\n"))
    b = int(input("Wprowadz b\n"))
    result = a / b
except ZeroDivisionError:
    print('Division by zero')
except ValueError:
    print('Wrong value')
except Exception:
    print('Error')
else:
    print(result)

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = []

for i in l1:
    l2.append(i**2)
print(l2)

l2 = [i**2 for i in l1]
print(l2)

l3 = [3**y for y in range(1, 6)]
print(l3)

l4 = [x for x in l1 if x % 2 == 1]
print(l4)

l5 = [(x, y) for x in l2 for y in l3]
print(l5)

l6 = []
for i in l2:
    for j in l3:
        l6.append((i, j))
print(l6)

d1 = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9}
d2 = {}
print(d1)

for key, value in d1.items():
    d2[value] = key
print(d2)

d3 = {v: k for k, v in d1.items()}
print(d3)

import math

def square_equation(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('Brak rozwiazan')
        return 0
    elif delta == 0:
        print('Jeden pierwiastek')
        return -b / (2 * a)
    else:
        print('Dwa pierwiastki')
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2

print(square_equation(6, 3, 1))
print(square_equation(1, 2, 1))
print(square_equation(1, 6, 1))

def segment_length(x1=1, x2=2, y1=3, y2=4):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print(segment_length())
print(segment_length(3, 5, 1, 6))
print(segment_length(y1=5, x1=3, y2=6, x2=0))
print(segment_length(1, 5, y2=0, y1=3))

file1 = open('C:\\Users\\local\\Desktop\\Python_studia\\lab3\\tekst.txt', 'r', encoding='utf-8')
char = file1.read(10)
line = file1.readline()
lines = file1.readlines()
file1.close()
print(char)
print(line)
print(lines)

file2 = open('tekst.txt', 'a+')
file2.write('aaaa')
file2.seek(105)
chars = file2.read(10)
file2.close()
print(chars)

with open('tekst.txt', 'r') as file3:
    chars = file3.read()

print(chars)