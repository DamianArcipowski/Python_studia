import random

print(random.random() * 20)
print(random.random() * 20)

random.seed(20)
print(random.randint(1, 100))

random.seed(20)
print(random.randint(1, 100))

some_tuple = [15, 23, 41, 18, 7]
random.shuffle(some_tuple)
print(some_tuple)

colors = ['black', 'yellow', 'green', 'red', 'white']
print(random.choice(colors))