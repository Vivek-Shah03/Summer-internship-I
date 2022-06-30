import math


class circle:
    def __init__(self):
        self.r = 2

    def diameter(self):
        return 2 * self.r


def area(c=circle()):
    return math.pi * c.r ** 2

c = circle()
print(c.diameter())
print(area(c))
