import random


def gen(n):
    for i in range(n):
        t = random.randint(1,100)
        if not a.__contains__(t):
            yield t

a = []
for i in gen(10):
    a.append(i)

print(a)