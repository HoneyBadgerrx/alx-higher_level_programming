#!/usr/bin/python3
"""
square class inheriting from basegeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """inits square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area"""
        return self.__size ** 2
