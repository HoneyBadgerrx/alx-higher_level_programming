#!/usr/bin/python3
"""
rads and outputs file
"""


def read_file(filename=""):
    """reads file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
