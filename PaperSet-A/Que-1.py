list1 = ['abstract', 'goat', 'kite', 'dog', 'cat', 'apple', 'jug', 'carrot', 'dumb']
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[j] < list1[i]:
            list1[j], list1[i] = list1[i], list1[j]


print(list1)
