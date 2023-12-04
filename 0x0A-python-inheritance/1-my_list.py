#!/usr/bin/python3
class MyList(list):

    """ This class inherits from list class """

    def print_sorted(self):
        """ sort the list in ascending order """
        sorted_list = sorted(self)
        print(sorted_list)

