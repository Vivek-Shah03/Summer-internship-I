import random


def cube(N):
    return N**3


ls = [random.randint(1, 10) for i in range(10)]
print(list(map(cube,ls)))