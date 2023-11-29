#!/usr/bin/python3
"""
An indentation Module
removes space at beginning or end of line
and after '.?:'
"""


def text_indentation(text):
    """
    Returns processed text
    Args: text pased
    Raise: TypeError
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end='')
        if text[i] == '\n' or text[i] in ".?:":
            if text[i] in ".?:":
                print('\n')
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
