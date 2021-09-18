from math import pi


class Circle:
    def __init__(self, radius=1):
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self.__radius = radius

    @property
    def diameter(self):
        return self.__radius * 2

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius cannot be negative')
        else:
            self.__radius = value

    @diameter.setter
    def diameter(self, diameter):
        if diameter < 0:
            raise ValueError('Diameter cannot be negative')
        self.__radius = diameter / 2

    @property
    def area(self):
        return pi * (self.__radius * self.__radius)

    def __repr__(self):
        return f'Circle({self.__radius})'
