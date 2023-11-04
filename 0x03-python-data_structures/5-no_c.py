#!/usr/bin/python3
def no_c(my_string):
    new_c = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            new_c += c
    return new_c
