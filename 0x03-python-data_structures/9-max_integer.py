#!/usr/bin/python3

def max_integer(my_list=[]):
    max_val = my_list[0]
    for i in range(len(my_list)):
        
        if my_list[i] > max_val:
            max_val = my_list[i]
        i = i + 1
    return max_val 
