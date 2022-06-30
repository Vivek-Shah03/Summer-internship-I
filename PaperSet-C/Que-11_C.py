import pickle
a = 10
b = "Hi"
c = True
f = open('my_variables.data', 'wb')
pickle.dump(a, f)
pickle.dump(b, f)
pickle.dump(c, f)
