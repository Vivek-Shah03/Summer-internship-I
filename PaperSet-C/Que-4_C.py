a = []
for i in range(2, 25):
    a.append(i)


def check(i):
    if i % 2 == 0 and i % 3 == 0:
        return i


print(list(filter(check, a)))
