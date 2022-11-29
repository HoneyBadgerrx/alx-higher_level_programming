#!/usr/bin/python3
"""
module for class dict repr
"""


def class_to_json(obj):
    """returns dict repr of class"""
    return obj.__dict__
