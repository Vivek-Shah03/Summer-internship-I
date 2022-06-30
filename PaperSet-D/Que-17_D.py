from operator import add
ls1 = [1, 2, 3, 4, 5]
ls2 = [6, 7, 8, 9, 10]
result = list(map(add, ls1, ls2))
print(result)