#!/usr/bin/python3
def no_c(my_string):
    i = 0
    j = len(my_string)
    while i < j:
        if my_string[i] == 'c' or my_string[i] == 'C':
            my_string = my_string[:i] + my_string[i + 1:]
            j = j - 1
            continue
        i = i + 1
    return my_string
