from math import sqrt
from typing import Tuple

class Point:
    cords: Tuple[float, ...]

    def __init__(self, cords: Tuple[float, ...]):
        self.cords = cords

    def distance(self, other) -> float:
        return sqrt(sum((x_1 - x_2) ** 2 for (x_1, x_2) in zip(self.cords, other.cords)))
        
    def __add__(self, other):
        return Point(tuple(x_1 + x_2 for x_1, x_2 in zip(self.cords, other.cords)))
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __truediv__(self, other):
        return Point(tuple(x / other for x in self.cords))

    def __hash__(self):
        return hash(self.cords)

    def __eq__(self, other):
        return self.cords == other.cords

    def __str__(self):
        return str(self.cords)
    def __repr__(self):
        return str(self) 
