#!/usr/bin/python3
"""A module that inherits list class(parent class)"""


class MyList(list):
    """A child class that inherits from list super class"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
