#!/usr/bin/python3
"""
a class inheriting list class
"""


class MyList(list):
    """a class inheriting from list"""
    def print_sorted(self):
        """prints sorted list in ascending order"""
        print(sorted(self))
