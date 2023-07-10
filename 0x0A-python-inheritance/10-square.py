#!/usr/bin/python3
"""A module that defines a subclass rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initialize a new square, for creating one
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

