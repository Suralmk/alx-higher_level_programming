#!/usr/bin/python3
"""This module defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n
    """
    if n <= 0:
        return []

    master = [[1]]
    while len(master) != n:
        tri = master[-1]
        new_t = [1]
        for i in range(len(tri) - 1):
            new_t.append(tri[i] + tri[i + 1])
        new_t.append(1)
        master.append(new_t)
    return master
