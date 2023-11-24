#!/usr/bin/python3
"""
A python linked list
"""


class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def __str__(self):
        ptr = self.__head
        while ptr:
            print(ptr.data)
            ptr = ptr.next_node
        return ""

    def sorted_insert(self, value):
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
