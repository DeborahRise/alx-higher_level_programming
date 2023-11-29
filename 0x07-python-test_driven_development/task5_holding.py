#!/usr/bin/python3
def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in text:
        if c == '.' or c == '?' or c == ':':
            print("{}".format(c))
            print()
        else:
            print("{}".format(c), end='')
