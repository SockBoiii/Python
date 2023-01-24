# Manases Garcia
# CSCI 248 Homework#10 Problem#5
# point3.py
# 11-5-2020
#
# This is the class for Point

import math

"""Provide the Point class."""

class Point:
    
    """Represent a point in 2-D coordinates."""

    def __init__(self, x_value=0, y_value=0):
        """Create a new point.

        Arguments:
            x_value (default 0)
            y_value (default 0)
        """

        self.__x = x_value
        self.__y = y_value

    def get_x(self):
        """Return the x coordinate of the point."""
        return self.__x

    def get_y(self):
        """Return the y coordinate of the point."""
        return self.__y

    def set_point(self, x_value, y_value):
        """Set the point to the new values.

        Arguments:
            x_value (default 0)
            y_value (default 0)
        """
        self.__x = x_value
        self.__y = y_value

    def get_distance(self, other):
        """Return the distance calling from self and other."""
        distance = math.sqrt(((self.__x - other.__x) ** 2) 
            + ((self.__y - other.__y) ** 2))
        return distance

    def move(self, dx, dy):
        """ Moves x and y by adding dx and dy to them"""
        self.__x += dx
        self.__y += dy
            
    def __eq__(self, other):
        """Return self == other."""
        return self.__x == other.__x \
            and self.__y == other.__y

    def __str__(self):
        """Create a string representation in format (%.2f, %.2f)."""
        return '(%.2f, %.2f)' % (self.__x, self.__y)

