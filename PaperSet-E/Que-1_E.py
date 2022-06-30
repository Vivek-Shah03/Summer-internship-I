balance = (100,200,300,400)
expense = (50, 201,250,404)

for i in range(len(balance)):
    if balance[i] >= expense[i]:
        print("Expenses Paid!")
    else:
        print("Expenses not paid!")