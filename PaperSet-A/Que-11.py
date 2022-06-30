try:
    # TypeError
    a = 'abc' + 2
    # value Error
    a = int("Abc")
    # Zero division error
    a = 1 / 0
    # IndexError
    arr = [1, 2]
    print(arr[7])
    # NameError
    a = b
    pass
except TypeError:
    print("TypeError Accured, Please check type of operand")
    pass
except ZeroDivisionError:
    print("You can't divide any number by zero.")
    pass
except ValueError:
    print("Value Error Accrued")
    pass
except NameError:
    print("Variable Doesn't declared")
    pass
except IndexError:
    print("You can't access out of index.")
    pass
