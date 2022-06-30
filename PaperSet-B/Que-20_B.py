class person:
    name = "Admin"
    Age = 18


p1 = person()

try:
    getattr(p1, 'name')
except AttributeError:
    print("Doesn't exist")
else:
    print("Exists")
# Fetching value of an attribute of class
print(p1.Age)

# updating value of an attribute of class
p1.Age = 25
print(p1.Age)

# deleting an attribute of object
del p1.Age

print(p1.Age)
