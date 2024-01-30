#!/usr/bin/python3
""""Module for class Rectangle"""


class Rectangle:
    """Defines Rectangle."""

    def __init__(self, width=0, height=0):
        """Method that initializes instances

        Args:
            width: width of a Rectangle.
            height: height of a Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method that returns width of Rectangle.

        Returns:
            width of a Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Method that sets width of Rectangle

        Args:
            value: width

        Raises:
            TypeError: if width is not intiger
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Method that returns height of Rectangle.

        Returns:
            height of a Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method that sets height of Rectangle

        Args:
            value: height

        Raises:
            TypeError: if height is not intiger
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
