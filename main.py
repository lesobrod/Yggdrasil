from utilites import *

class Yggdrasil:
    # It's a Chain of levels
    def __init__(self, max_index: int):
        assert 1 < max_index < 100, 'Incorrect levels number'


class Level:
    def __init__(self, level_index, start_angle, max_index, next=None):
        self.index = level_index
        self.next = next
        self.radius = radius(level_index, max_index)
        self.shift = shift(-0.1, 0.1)
        self.num_points = number_points(level_index)
        self.points = [Point(level_index, i) for i in range(self.num_points)]

    def set_to_points(self):
        if self.index == 0:
            # Центр связан со всеми точками след уровня
            self.points[0].to_points = self.next.points
        else:

    def set_from_points(self):
        if self.index == 0:
            # Центр связан со всеми точками след уровня
            self.points[0].from_points = self.next.points
        else:

class Point:
    def __init__(self, level, point_index):
        self.index = point_index
        self.level = level
        self.angle = angle(level.shift, point_index, level.num_points)
        self.to_points = []
        self.from_points = []



