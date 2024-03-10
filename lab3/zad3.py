shopping_list = {'mleko': 'l', 'jajka': 'szt', 'kurczak': 'kg', 'chleb': 'szt', 'sok': 'l', 'masło': 'szt'}
units = {k for (k, v) in shopping_list.items() if v == 'szt'}

print(units)