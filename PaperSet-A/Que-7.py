# filter the list with False elements. [10,0,[],[11],(),{'a':1,'b':2}]
ls = [10,0,[],[11],(),{'a':1,'b':2}]
filtered = []
for ele in ls:
    if not ele:
        filtered.append(ele)


print(filtered)