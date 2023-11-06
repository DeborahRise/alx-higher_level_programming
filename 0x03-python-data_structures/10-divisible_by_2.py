#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if isinstance(my_list, list):
        return [True if l % 2 == 0 else False for l in my_list]
    return []
