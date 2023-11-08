#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_a = sorted(a_dictionary.items(), key=lambda a: a[0])
    sort_dict = {key: value for key, value in sort_a}
    for x, y in sort_dict.items():
        print(f"{x}: {y}")
