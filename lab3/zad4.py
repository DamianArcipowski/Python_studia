def is_right_angled(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return 'Prostokątny'
    else:
        return 'Nieprostokątny'

print(is_right_angled(1, 2, 3))
print(is_right_angled(3, 4, 5))