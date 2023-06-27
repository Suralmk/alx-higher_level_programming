#!/usr/bin/python3
"""defining a class square """


class Square:
    """A class called square is defined"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculate the area of the square
        Returns: the area of the square
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """retrive size"""

        return (self.__size):

    @size.setter
    def size(self, value):
        """toset the value of size"""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

