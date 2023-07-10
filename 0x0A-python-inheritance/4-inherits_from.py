#!/usr/bin/python3
"""A module that ckecks if object is inherited form a apecified class
or not.
"""


def inherits_from(obj, a_class):
    """Returns true if object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    """
    result = issubclass(type(obj), a_class) and type(obj) != a_class
    return (result)
