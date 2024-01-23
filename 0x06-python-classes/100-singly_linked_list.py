#!/usr/bin/python3
"""Node module."""


class Node:
    """Defines Node."""

    def __init__(self, data, next_node=None):
        """Constructor

        Args:
            data: collected number
            next_node: Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Property for collected data

        Returns:
            TypeError: if data is not intiger
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Property for next node

        Returns:
            TypeError: if node is not an object
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) != Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Defines SinglyLinkedList"""

    def __init__(self):
        """Constructor
        """
        self.head = None

    def __str__(self):
        """Constructor String

        Returns:
            ret: returns ret from the back of the string
        """
        ret = ""
        node = self.head
        while node:
            ret += str(node.data) + "\n"
            node = node.next_node
        return ret[:-1]

    def sorted_insert(self, value):
        """Sortes value

        Args:
            value: Value yo be sorted
        """
        new = Node(value)
        if not self.head:
            self.head = new
            return

        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        if node.next_node:
            new.next_node = node.next_node
        node.next_node = new
