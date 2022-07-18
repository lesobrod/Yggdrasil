from utilites import *
import math


class Node:
    def __init__(self, next=None):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


class Yggdrasil(LinkedList):
    # It's a LinkedList of levels

    def __init__(self, max_index: int):
        assert 1 < max_index < 100, 'Incorrect levels number'
        super().__init__()
        self.levels = []
        self.head = Level(0, max_index)
        self.levels.append(self.head)
        for i in range(1, max_index):
            self.levels.append(Level(i, None))
            self.levels[i-1].next = self.levels[i]

    def __str__(self):
        # Печатаем инфу о древе
        out = 'Yggdrasil:\n'
        lev = self.head
        while lev.next is not None:
            lev = lev.next
            out += str(lev) + '\n'
        return out


class Point(Node):

    def __init__(self, level, point_index):
        super().__init__()
        self.index = point_index
        self.level = level
        self.angle = angle(level.shift, point_index, level.num_points)
        self.x = level.radius * math.cos(self.angle)
        self.y = level.radius * math.sin(self.angle)
        self.to_points = []
        self.from_points = []

    def __str__(self):



class Level(Node):

    def __init__(self, level_index, max_index):
        super().__init__()
        self.index = level_index
        self.radius = radius(level_index, max_index)
        self.shift = shift(-0.1, 0.1)
        self.num_points = number_points(level_index)

        self.points = LinkedList()
        self.points.points_list = []
        self.points.head = Point(self, 0)
        self.points.points_list.append(self.points.head)
        for i in range(1, self.num_points):
            self.points.points_list.append(Point(self, i))
            self.points.points_list[i - 1].next = self.points.points_list[i]
        self.points.points_list[i].next = self.points.points_list[0]

    def __str__(self):
        # Печатаем инфу об уровне
        out = f'Level: {self.index} Radius: {self.radius} ' \
              f'Shift: {self.shift} NumPoints: {self.num_points}'
        out += '\nPoints:'
        for i in range(self.num_points):
            out += str(self.points.points_list[i])
        return out



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




