#!/usr/bin/python3
""" format of class square"""


class Square:
    """square class format"""
    def __init__(self, size):
        """ init function"""
        self.size = size
    @property
    def size(self):
        """ returns value of size"""
        return self.__size
    @size.setter
    def size(self, value):
        """ sets value of size """
        self.__size = value
