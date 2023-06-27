#!/usr/bin/python3

"""defining class"""

class Square:
    """class defined"""

    def __init__(self, size=0):

        """instanciated the class with var          iable xize
        raise TypeError : if size is other than int
        raise ValueError : if size is less than zero"""

        if not isinstance(self, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError(size must be >= 0)


        self.__size = size
