#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    last_idx = -1
    for i in my_list:
        print("{}".format(my_list[last_idx]))
        last_idx = last_idx  - 1
