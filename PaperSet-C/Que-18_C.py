import random

list1 = []
for i in range(25):
    list1.append(random.randint(1,100))

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[j] < list1[i]:
            list1[j], list1[i] = list1[i], list1[j]


print(list1)
