#!/usr/bin/python
def copy_list(l):
    return (l[:] if isinstance(l, list))
