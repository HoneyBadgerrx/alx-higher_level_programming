#!/usr/bin/python3
""" format of class square"""


class Square:
    """square class format

        Attributes:
            __size (int): size of sqaure
            __position (tuple): position of square
    """
    def __init__(self, size=0, position=(0, 0):
        """ init function
        Args:
            size (int, optional): size of square
            position (tuple, optional): position of square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple or len(position) != 2 \
                or type(position[0]) is not int or position[0] < 0 \
                or type(position[1]) is not int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
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
    @property
    def position(self):
        """gets position
            Returns:
            None
        """
        return self.__position
    @position.setter
    def position(self, position):
        """sets position

        Args:
            value (tuple): value to be set
        Returns:
            None
        """
        if type(position) is not tuple or len(position) != 2 \
                or type(position[0]) is not int or position[0] < 0 \
                or type(position[1]) is not int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
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
