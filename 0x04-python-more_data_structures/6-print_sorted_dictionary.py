#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_a = sorted(a_dictionary.items(), key=lambda a: a[0])
    return sort_a
