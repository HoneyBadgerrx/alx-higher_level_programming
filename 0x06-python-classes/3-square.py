#!/usr/bin/python3
""" format of class square"""


class Square:
    """square class format

        Attributes:
            __size (int): size of sqaure
    """
    def __init__(self, size=0):
        """ init function
        Args:
            size (int, optional): size of square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """returns area of sqaure

        Returns:
            area of sqqaure
        """
        return (self.__size) ** 2
