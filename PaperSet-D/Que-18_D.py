a = ['a','b','c','d','e']
b = [1,2,3,4,5]
d = {a[i]:b[i] for i in range(len(a))}
print(d)