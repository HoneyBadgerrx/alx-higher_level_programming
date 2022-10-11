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
        """ area of square

        Returns:
            area of square
        """
        return (self.__size) ** 2
    @property
    def size(self):
        """returns size

        Returns:
            size
        """
        return self.__size
    @size.setter
    def size(self, value):
        """sets value of size

        Args:
            value (int): value of size
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def my_print(self):
        """prints square

        Returns:
            None
        """
        l = self.__size
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
