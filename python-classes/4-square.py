#!/usr/bin/python3
"""Defines a class Square with size property and area method."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square with optional size (default 0)."""
        self.size = size  # Use setter to validate size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
