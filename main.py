from utilites import *
import math


class Yggdrasil:

    def __init__(self, max_index: int):
        assert 1 < max_index < 100, 'Incorrect levels number'
        self.max_index = max_index
        self.levels = [Level(i, max_index) for i in range(max_index)]

    def __str__(self):
        # Печатаем инфу о древе
        out = 'Yggdrasil:\n\n'
        for lev in self.levels:
            out += str(lev) + '\n\n'
        return out


class Level:

    def __init__(self, level_index, max_index):
        self.index = level_index
        self.radius = radius(level_index, max_index)
        self.shift = shift(-0.1, 0.1)
        self.num_points = number_points(level_index)

        self.points = [Point(self, i) for i in range(self.num_points)]

    def __str__(self):
        # Печатаем инфу об уровне
        out = f'Level: {self.index} Radius: {self.radius:.2f} ' \
              f'Shift: {self.shift:.3f} NumPoints: {self.num_points}'
        out += '\nPoints:\n'
        for pt in self.points:
            out += str(pt) + '\n'
        return out


class Point:

    def __init__(self, level, point_index):
        self.index = point_index
        self.level = level
        self.angle = angle(level.shift, point_index, level.num_points)
        self.x = level.radius * math.cos(self.angle)
        self.y = level.radius * math.sin(self.angle)
        self.to_points = []
        self.from_points = []

    def __str__(self):
        return f'Point: {self.index} angle: {self.angle:.3f} \n' \
               f'to_points: {self.to_points} from_points: {self.from_points}'


#     def set_to_points(self):
#         if self.index == 0:
#             # Центр связан со всеми точками след уровня
#             self.points[0].to_points = self.next.points
#         else:
#
#     def set_from_points(self):
#         if self.index == 0:
#             # Центр связан со всеми точками след уровня
#             self.points[0].from_points = self.next.points
#         else:
#


if __name__ == '__main__':
    new_tree = Yggdrasil(2)
    print(new_tree)
