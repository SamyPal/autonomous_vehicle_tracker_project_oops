"""
A Position represents an x, y coordinate in a given warehouse. Position
can be used to determine how far apart or near together two vehicles are.
"""

import math


class Position(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return ("(" + str(self.x) + ", " + str(self.y) + ")")

    def __eq__(self, other):
        if not isinstance(other, Position):
            return False

        return (self.x == other.get_x() and self.y == other.get_y())


def get_distance(position_1, position_2):
    """
    Determines the distance between two Positions
    Distance is calculated as the Euclidean distance in two dimensions
    https://en.wikipedia.org/wiki/Euclidean_distance
    """
    x_diff = abs(position_1.get_x() - position_2.get_x())
    y_diff = abs(position_1.get_y() - position_2.get_y())
    return math.sqrt(pow(x_diff, 2) + pow(y_diff, 2))
