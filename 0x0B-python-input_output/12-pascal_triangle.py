#!/usr/bin/python3
"""
module containig pascal trianle
"""


def pascal_triangle(n):
    """prins pascal trianle of length n"""
    if n <= 0:
        return []

    l = []
    l.append([1])
    for i in range(n - 1):
        new_list = []
        new_list.append(1)
        a, b = 0 , 1
        while True:
            try:
                new_list.append(l[i][a] + l[i][b])
                a += 1
                b += 1
            except Exception:
                break
        new_list.append(1)
        l.append(new_list)
    return l
