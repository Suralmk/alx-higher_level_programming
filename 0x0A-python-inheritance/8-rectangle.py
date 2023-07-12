#!/usr/bin/python3
"""A module that inherits base geometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define a rectangle"""

    def __init__(self, width, height):
        """create aa rectangle onject
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
