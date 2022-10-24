#!/usr/bin/python3
"""
class to raise exception
"""


class BaseGeometry:
    """exception class"""

    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")
