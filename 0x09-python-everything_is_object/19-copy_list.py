#!/usr/bin/python3
def copy_list(l):
    return l[:] if isinstance(l, list) else None
