#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this class represents a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new rectangle"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        rectangle_area = self.__width * self.__height
        return rectangle_area

    def __str__(self):
        """rreturn the print and string representation of a rectangle onject"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
