from math import sqrt


class Rectangle:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        area = self.__width * self.__height
        return area

    def perimeter(self):
        return (self.__width * 2 ) + (self.__height * 2)

    def diagonal(self):
        return sqrt(self.__width ** 2 + self.__height ** 2)

    def __str__(self):
        return (f"Area = {self.area():.2f}\n"
              f"Perimeter = {self.perimeter():.2f}\n"
              f"Diagonal = {self.diagonal():.2f}")
