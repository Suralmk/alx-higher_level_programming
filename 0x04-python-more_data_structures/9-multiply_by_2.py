#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """
    A function that return a dictionary where
    all values are multiplied y 2
    """
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict.update({key: (value * 2)})
    return new_dict
