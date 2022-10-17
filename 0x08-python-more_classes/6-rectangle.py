#!/usr/bin/python3
"""module containing rectangle class"""
class Rectangle:
    """rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """init of instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del___(self):
        """on del method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """width getter"""
        return self.__width
    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height
    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area"""
        return self.__width * self.__height
    def perimeter(self):
        """returns perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints str repr of rect"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            string += '#' * self.__width
            if (i != self.__height - 1):
                string += '\n'
        return string
    def __repr__(self):
        """rept of class instace"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
