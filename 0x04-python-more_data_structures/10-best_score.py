#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for k in a_dictionary:
            m = a_dictionary[k]
            break
        for k, v in a_dictionary.items:
            if v > m:
                m = v
        return m
    else:
        return None
