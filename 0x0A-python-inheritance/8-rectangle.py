#!/usr/bin/python3
"""
rectangle class
"""


class BaseGeometry:
    """exception class"""

    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates int for corrrect type and if <= 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """rectangle class from geometry"""
    def __init__(self, width, height):
        """initialises width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
