class MIN_LENGTH(Exception):
    pass


try:
    a = list(input("Enter a List: ").split(' '))
    print(a)
    if len(a) < 5:
        print(len(a))
        raise MIN_LENGTH
except MIN_LENGTH:
    print("The Minimum Length Of List Should Be 5.")
