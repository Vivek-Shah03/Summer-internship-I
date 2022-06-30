import pickle
f = open('my_variables.data', 'rb')
temp = pickle.load(f)
print(temp)
