#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        s = 0
        rom = {'I': 1, 'X': 10, 'L': 50, 'M': 1000, 'D': 500, 'C': 100}
        for i in roman_string:
            if rom.get(i, 0):
                s += rom[i]
        return s
    return None
