#!/usr/bin/python3
"""Checks an object is an instance of a class"""


def is_same_class(obj, a_class):
    """Function which return true if instance of a class
        else return false
    """
    return (type(obj) == a_class)
