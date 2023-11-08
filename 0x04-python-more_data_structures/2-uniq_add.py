#!/usr/bin/python3
def uniq_add(my_list=[]):
    result, x = set(my_list), 0
    for y in result:
        x = x + y
    return x
