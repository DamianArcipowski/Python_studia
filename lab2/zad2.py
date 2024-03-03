import sys

sys.stdout.write('Wprowadz pierwsza liczbe: \n')
a = int(sys.stdin.readline())
sys.stdout.write('Wprowadz druga liczbe: \n')
b = int(sys.stdin.readline())
sys.stdout.write('Wprowadz trzecia liczbe: \n')
c = int(sys.stdin.readline())

sys.stdout.write(f'Wynik: {a ** b + c}')