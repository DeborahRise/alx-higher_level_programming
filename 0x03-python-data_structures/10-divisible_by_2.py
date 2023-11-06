#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if isinstance(my_list, list):
        return [True if li % 2 == 0 else False for li in my_list]
    return []
