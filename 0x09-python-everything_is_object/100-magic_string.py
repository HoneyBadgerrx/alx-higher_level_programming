#!/usr/bin/python3
def kab():
    kab.j = getattr(kab, 'j', 0) + 1
    return str("BestSchool, " * (kab.j - 1) + "BestSchool")
