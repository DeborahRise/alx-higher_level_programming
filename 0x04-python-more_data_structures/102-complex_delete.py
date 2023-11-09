#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_delete = []
    for keys, values in a_dictionary.items():
        if values == value:
            to_delete.append(keys)

    for d in to_delete:
        del a_dictionary[d]

    return a_dictionary
