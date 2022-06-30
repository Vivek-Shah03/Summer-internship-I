d = {chr(i):i for i in range(97,123)}
d.update({chr(i):i for i in range(65,91)})
d.update({chr(i): i for i in range(48, 58)})
print(d)
