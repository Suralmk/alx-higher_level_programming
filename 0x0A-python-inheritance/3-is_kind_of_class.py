#!/usr/bin/python3
"""A module that checks if an object is instance of a class or
it is inherited.
"""


def is_kind_of_class(obj, a_class):
    """return ture if it is instance ot inherited
    """
    return (isinstance(obj, a_class))
