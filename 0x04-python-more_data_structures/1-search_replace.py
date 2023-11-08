#!/usr/bin/python3
def search_replace(my_list, search, replace):
    l2 = []
    l2 = list(map(lambda x: replace if x == search else x, my_list))
    return l2
