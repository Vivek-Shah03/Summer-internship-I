import random

random_numbers = []
even = []
odd = []
for i in range(10):
    t = random.randint(1, 100)
    if t % 2 == 0:
        even.append(t)
    else:
        odd.append(t)
    random_numbers.append(t)

print(random_numbers)
print(even)
print(odd)
