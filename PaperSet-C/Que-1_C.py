def SortedList(l):
    a = list(l)
    a.sort()
    return a


dic = {1:'one', 2: 'two', 5:'five', 4:'four', 3:'three'}

print(dic.keys())
print(SortedList(dic.keys()))