#!/usr/bin/python3
def best_score(a_dictionary):
    for k, v in a_dictionary.items():
        m = a_dictionary[k]
        break
    for k, v in a_dictionary.items():
        if v > m:
            m = v
    return m
