#!/usr/bin/python3
def check_tuple(tuple_x=()):
    for r in range(2 - len(tuple_x)):
        tuple_x = tuple_x + (0,)
    return tuple_x


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = check_tuple(tuple_a)
    if len(tuple_b) < 2:
        tuple_b = check_tuple(tuple_b)

    new_tup = ()
    for r in range(2):
        new_tup = new_tup + (tuple_a[r] + tuple_b[r],)
    return new_tup
