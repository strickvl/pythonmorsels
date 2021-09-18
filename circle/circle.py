import math


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * (self.radius * self.radius)

    def __repr__(self):
        return f'Circle({self.radius})'
