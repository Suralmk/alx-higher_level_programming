#!/usr/bin/python3

class Rectangle:
    """defines rectangle"""
    def __init__ (self, width=0, height=0):
        """initialize a new rectangle
        Args:
        width(int): width of the new rctangle
        height(int): height of the rectangle
        """
        self.__width = width
        self.__height = heght

    @property
    def width(self):
        """define width method to retrive  widdth"""
        return self.__width

    @propert_setter
    def width(self, value):
        """set width to value
        Args:
        value(int): the new width value
        """

        if isinstance(value, int) == False:

            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
    
    @property
    def height(self):
        """height mwthod to retrive height"""

        return self.__height
        

    @property_setter
    def height(self, value):
        """set height value to value variable"""

        if isinstance(value, int) == False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
