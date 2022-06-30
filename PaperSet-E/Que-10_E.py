a = 1
b = 2
if  a < b:
    print(f"{a} < {b}")
if a > b:
    print(f"{a} > {b}")
if a != b:
    print(f"{a} != {b}")
if a <= b:
    print(f"{a} <= {b}")
if a >= b:
    print(f"{a} >= {b}")
if a == b:
    print(f"{a} == {b}")

ls1 = [11, 22,33, 44]

if 11 in ls1:
    print("11 is in ls1.")

if ls1.__contains__(10):
    print("10 is in ls1.")
else:
    print("ls1 doesn't contain 10.")
