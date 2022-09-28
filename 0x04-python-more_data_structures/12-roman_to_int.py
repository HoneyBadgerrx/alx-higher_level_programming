#!/usr/bin/python3
def roman_to_int(r):
    if r and type(r) == str:
        s = 0
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'M': 1000, 'D': 500, 'C': 100}
        for i in range(r):
            if i > 0 and rom[r[i]] > rom[r[i - 1]]:
                s = s + rom[r[i]] - 2 * rom[r[i - 1]]
            else:
                s += rom[r[i]]
        return s
    return 0
