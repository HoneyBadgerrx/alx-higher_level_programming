#!/usr/bin/python3
"""creates MagicClass"""
import math

class MagicClass:
    """shows a circle"""
    def __init__(self, radius=0):
        """magic cic init"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
    def area(self):
        """area of magic cic"""
        return (self.__radius ** 2) * math.pi
    def circumference(self):
        """curcumference of cir"""
        return 2 * math.pi * self.__radius
