#!/usr/bin/python3
"""
checks if class is subclass
"""


def inherits_from(obj, a_class):
    """truee if class is subclass of class"""
    return type(obj) != a_class and issubclass(type(obj), a_class)
