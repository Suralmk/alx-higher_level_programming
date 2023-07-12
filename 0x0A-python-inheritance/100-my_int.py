#!/usr/bin/python3
"""define a class MyInt which inherits int"""


class MyInt(int):
    """change int operators == and !="""

    def __eq__(self, value):
        """Override ==(equal to) opeartor with !=(not equal to) behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior"""
        return self.real == value
