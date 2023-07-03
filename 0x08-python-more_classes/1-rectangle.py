#!/usr/bin/python3
"""defining a rectangle class."""


class Rectangle:
    """Represents  rectangle."""

    def __init__ (self, width=0, height=0):
        """Initialize a new rectangle
        Args:
            width(int): width of the new rctangle
            height(int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Define width method to retrive  widdth"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height mwthod to retrive height."""
        return self.__height
        
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
