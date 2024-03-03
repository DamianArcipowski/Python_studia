import sys

a = 56
print(type(a))

b = 5.5
print(type(b))

zmienna_tekstowa = 'wizualizacja danych'
print(type(zmienna_tekstowa))

c = 6
d = 3

e = c + d
print(e)

e = c - d
print(e)

e = 4
f = c // e
print(f)

g = c ** 2
print(g)

h = pow(c, 2)
print(h)

i = 6 ** (1/2)
print(i)

j = pow(6, 1/2)
print(j)

k = 'wizualizacja danych'
l = 'grupa 1'
m = 1
print(k + l + str(m))
print('liczba a jest rowna {:.2f}, liczba b jest rowna {}'.format(c, d))

inp = input('Wprowadz liczbe: ')
print(inp)
print(type(inp))
print(inp * 6)

sys.stdout.write('Wprowadz liczbe: ')
inp2 = sys.stdin.readline()
print(inp2)
print(type(inp2))

list1 = [5, 15, 2.6, [3, 4, 3], 'tekst']
print(list1)

list1.append(7)
print(list1)

list1.insert(3, 10)
print(list1)

list1.extend([14, 33])
print(list1)

list1.pop()
print(list1)

list1.pop(2)
print(list1)

list1.remove([3, 4, 3])
print(list1)

del list1[1]
print(list1)

list1.reverse()
print(list1)

#list1.sort()

dict1 = {'key': 'value', 1: 2, 'a': 5, 3: 'b'}
print(dict1)
print(dict1[3])

dict1[5] = 6
print(dict1)

dict1.pop(1)
print(dict1)

print(dict1.keys())
print(dict1.values())
del dict1[5]

a = 6
b = 10

if a > b:
    print('a is greater than b')
elif a < b:
    print('a is lesser than b')
else:
    print('a is equal to b')

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a > b) & (c > d):
    print(a, c)
else:
    print(b, d)

for i in range(1, 6, 2):
    print(i)
else:
    print('koniec petli')

list2 = [1, 15, 3, 4, 7]
for i in list2:
    print(i)

for i in range(5):
    for j in range(5):
        res = i + j
        print(res)
    print('')

counter = 0
while counter < len(list2):
    print(list2[counter])
    counter += 1
else:
    print('koniec petli')

counter = 0
while counter != 10:
    if counter == 7:
        print(counter)
        break
    else:
        counter += 1
else:
    print('licznik')


#zadanie
final_list = [15, 2, 3, 4, 1, 10]
inp = sys.stdin.readline()
counter = 0
print('---------')

while counter < len(final_list):
    if int(inp) == final_list[counter]:
        print(final_list[counter])
        break

    counter += 1