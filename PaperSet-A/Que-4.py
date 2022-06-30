# Merge two lists using the function of list and sort the resultant list in reverse order.
ls1 = [1, 3, 5, 7, 9]
ls2 = [2, 4, 6, 8, 10]

merged = ls1.copy()
merged.extend(ls2)
merged.sort(reverse=True)

print(merged)
