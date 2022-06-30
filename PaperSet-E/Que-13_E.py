dividend = int(input("Enter Dividend: "))
divisor = int(input("Enter Divisor:" ))
try:
    result = dividend / divisor
except ZeroDivisionError:
    print("Divisor can't be zero.")
else:
    print(result)
