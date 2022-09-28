#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string or type(roman_string) == str:
        s = 0
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'M': 1000, 'D': 500, 'C': 100}
        for i in range(roman_string):
            if roman_string[i] > roman_string[i - 1]:
                s = s + roman_string[i] - 2 * roman_string[i - 1]
            else:
                s += roman_string[i]
        return s
    return 0
