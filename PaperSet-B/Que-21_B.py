import functools
import random
import string
import operator
a = []

for i in range(10):
    a.append(random.choice(string.ascii_letters))


print(functools.reduce(operator.add, a))