#!/usr/bin/python3
"""Prints a square"""


def print_square(size):
    """# filled square is printed.
    Args:
        size (int): The height or width
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
