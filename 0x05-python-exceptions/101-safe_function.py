#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        res = None
        return res
    else:
        return res
