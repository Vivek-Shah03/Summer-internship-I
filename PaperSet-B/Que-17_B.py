num = int(input("Enter Base: "))
exp = int(input("Enter Exponent: "))
ans = lambda a, b: a ** b
print(ans(num, exp))
s = "abcd"

assert len(s) > 10, "Length of String should be greater than 10."
