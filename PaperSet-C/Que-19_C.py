import functools
import random

a = []
for i in range(15):
    a.append(random.randint(1,100))

print(functools.reduce(lambda a, b: a+b, a))