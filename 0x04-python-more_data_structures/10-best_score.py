#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        m = list(a_dictionary.keys())[0]
        for k, v in a_dictionary.items:
            if v > a_dictionary[m]:
                m = k
        return m
    return None
