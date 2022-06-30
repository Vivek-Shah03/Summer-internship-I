octal = 13
decimal = 0
i = 0
while (octal != 0):
      decimal = decimal + (octal % 10) * pow (8, i)
      i+=1
      octal = octal // 10


print(f"Decimal : {decimal}")
print(f"Binary : {bin(decimal)}")
print(f"HexaDecimal : {hex(decimal)}")