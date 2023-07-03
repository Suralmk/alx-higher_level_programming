#!/usr/bin/python3
"""defining a rectangle class."""


class Rectangle:
    """Represents  rectangle."""

    def __init__ (self, width=0, height=0):
        """Initialize a new rectangle.
        Args:
            width(int): width of the new rctangle.
            height(int): height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Define width method to retrive  widdth."""
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
        """Height mwthod to retrive height."""
        return self.__height
        
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns Printable form of the rectangle in #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle = rectangle + '#'
            self.__height -= self.__heiht
            rectangle = rectangle + "\n"
        return (rectangle)
