# Have a list of even numbers between 1 t0 100 in one line

even = []
for i in range(1,100):
    if i % 2 == 0:
        even.append(i)

print(even)