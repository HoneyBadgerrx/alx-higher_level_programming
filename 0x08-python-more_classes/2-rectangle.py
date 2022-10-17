#!/usr/bin/python3
"""module containing rect class"""


class Rectangle:
    """rect class"""
    def __init__(self, width=0, height=0):
        """initialisation"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width seter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """heigth getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height seter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """retuns area"""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
