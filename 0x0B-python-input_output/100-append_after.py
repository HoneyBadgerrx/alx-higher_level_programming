#!/usr/bin/python3
"""
function to append to file on key string
"""


def append_after(filename="", search_string="", new_string=""):
    """append after function"""
    with open(filename, 'r', encoding='utf-8') as f:
        a_list = []
        while True:
            line = f.readline()
            if line == "":
                break
            a_list.append(line)
            if search_string in line:
                a_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(a_list)
