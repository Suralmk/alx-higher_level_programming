#!/usr/bin/python3
"""defining a class square """


class Square:
    """A class called square is defined"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            position: position of the square
        """
        
        self.__size = size
        self.position = position
    
    def __str__(self):
        self.my_print()


    @property
    def size(self):
        """retrive size"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """setter for the position o f the suare
        Args: value as a tuple of two positive integers
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """

        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([n for n in value if isinstance(n, int) and n >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculate the area of the square
        Returns: the area of the square
        """

        return (self.__size ** 2)

    def pos_print(self):
        """return the position"""
        pos_where = ""
        if self.size == 0:
            return "\n"
        for val in range(self.position[1]):
            pos_where += "\n"
        for val in range(self.size):
            for i in range(self.position[0]):
                pos_where += " "
            for j in range(self.size):
                pos_where += "#"
            pos_where += "\n"
        return pos_where

    def my_print(self):
        """for printing the position"""
        print(self.pos_print(), end='')

