#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    printes ordered dictionary
    """
    dic_keys = list(a_dictionary.dic_keys())
    dic_keys.sort()
    for key in dic_keys:
        print("{}: {}".format(key, a_dictionary[key]))
