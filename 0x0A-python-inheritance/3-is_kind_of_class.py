#!/usr/bin/python3
"""
checks for if obj is in class tree of class
"""


def is_kind_of_class(obj, a_class):
    """checks if obj is instance or inherited from class"""
    return isinstance(obj, a_class)
