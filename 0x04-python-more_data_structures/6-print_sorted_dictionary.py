#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    mylist = []
    for i in a_dictionary.keys():
        mylist.append(i)
    for i in sorted(mylist):
        print("{}: {}".format(i, a_dictionary[i]))
