#!/usr/bin/python3
"""
student module
"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """student initialisation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs):
        """returns json repr of class with specific attributes in attrs"""
        if attrs is None:
            return self.__dict__
        dict_1 = {}
        for a in attrs:
            try:
                dict_1[a] = self.__dict__[a]
            except Exception:
                pass
        return dict_1
