#!/usr/bin/python3
def copy_list(list_l):
    return list_l[:] if isinstance(list_l, list) else None
