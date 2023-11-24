#!/usr/bin/python3
"""
A python linked list
"""


class Node:
    """creating a Node Object"""

    def __init__(self, data, next_node=None):
        """initializing the node appropriately"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter"""

        return self.__data

    @data.setter
    def data(self, value):
        """data setter"""

        if not isinstance(value, int):
            raise TypeError("data must be integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node getter"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter"""

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """for creating an sigly linked list"""

    def __init__(self):
        """initialize the head"""

        self.__head = None

    def __str__(self):
        """make it printable"""

        prnt = ""
        ptr = self.__head
        while ptr:
            prnt += str(ptr.data) + "\n"
            ptr = ptr.next_node
        return prnt[:-1]

    def sorted_insert(self, value):
        """a soted insetion"""

        self.new_node = Node(value)
        if self.__head is None:
            self.__head = self.new_node
        elif self.__head.data >= self.new_node.data:
            self.new_node.next_node = self.__head
            self.__head = self.new_node
        else:
            ptr = self.__head
            while ptr.next_node and ptr.next_node.data < self.new_node.data:
                ptr = ptr.next_node
            self.new_node.next_node = ptr.next_node
            ptr.next_node = self.new_node
