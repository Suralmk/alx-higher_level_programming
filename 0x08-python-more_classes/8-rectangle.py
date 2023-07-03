#!/usr/bin/python3
"""defining a rectangle class."""


class Rectangle:
    """Represents  rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__ (self, width=0, height=0):
        """Initialize a new rectangle.
        Args:
            width(int): width of the new rctangle.
            height(int): height of the rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self) -> str :
        """Returns Printable form of the rectangle in #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle = rectangle + str(self.print_symbol)
            if i != self.__height - 1:
                rectangle = rectangle + "\n"
        return (rectangle)

    def __repr__(self):
        """Return string representation of a rectangle object."""
        return ("Rectangle({:s}, {:s})".format(str(self.__width), str(self.__height)))

    def __del__(self):
        """prints a message when an object is deleted"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares tow instances of Rectangle class
        based on their area.
        Args:
            rect_1: the first rectangle.
            rect_2: the second rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return (rect_2)
        elif rect_1.area() > rect_2.area():
            return (rect_1)
        else:
            return (rect_1)
