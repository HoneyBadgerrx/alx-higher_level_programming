#!/usr/bin/python3
"""
appends to end of file
"""


def append_write(filename="", text=""):
    """appends to fiel"""
    with open(filename, "a", encoding="utf=8") as f:
        return f.write(text)
