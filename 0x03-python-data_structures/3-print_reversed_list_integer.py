#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, list):
        new_list = my_list[::-1]
        for n in new_list:
            print("{:d}".format(n))
