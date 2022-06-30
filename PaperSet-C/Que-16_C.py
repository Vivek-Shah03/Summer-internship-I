import random
a = []
for i in range(10):
    a.append(random.randint(0,1))
print(a)
if not a.__contains__(0):
    print('All')
elif not a.__contains__(1):
    print('None')
else:
    print('Any')