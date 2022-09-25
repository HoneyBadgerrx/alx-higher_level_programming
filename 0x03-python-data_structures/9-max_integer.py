#!/usr/bin/python3
def max_integer(my_list=[]):
    mi = 0
    for i in my_list:
        if i > mi:
            mi = i
    return mi
