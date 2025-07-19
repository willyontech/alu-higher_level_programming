#!/usr/bin/python3
"""Defines Node and SinglyLinkedList with sorted insertion."""


class Node:
    """Node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize Node with data and optional next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data with validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next_node with validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initialize list with head set to None."""
        self.__head = None

    def __str__(self):
        """Return a string of the entire list, one node per line."""
        node = self.__head
        nodes = []
        while node:
            nodes.append(str(node.data))
            node = node.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """Insert a Node in increasing sorted order."""
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
