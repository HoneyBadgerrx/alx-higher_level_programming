#!/usr/bin/python3
"""
rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class from geometry"""
    def __init__(self, width, height):
        """initialises width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
