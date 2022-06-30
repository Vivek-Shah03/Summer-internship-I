import random
a = []
while len(a)<4:
    t = random.randint(1, 100)
    if not a.__contains__(t):
        a.append(t)
print(a)
