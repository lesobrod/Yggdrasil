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
        self.num_buds = number_buds(level_index, max_index)

        self.buds = [Bud(self, i) for i in range(self.num_buds)]

    def __str__(self):
        # Печатаем инфу об уровне
        out = f'Level: {self.index} Radius: {self.radius:.2f} ' \
              f'Shift: {self.shift:.3f} NumBuds: {self.num_buds}'
        out += '\nBuds:\n'
        for pt in self.buds:
            out += str(pt) + '\n'
        return out


class Bud:

    def __init__(self, level, bud_index):
        self.index = bud_index
        self.level = level
        self.angle = angle(level.shift, bud_index, level.num_buds)
        self.x = level.radius * math.cos(self.angle)
        self.y = level.radius * math.sin(self.angle)
        self.to_buds = []
        self.from_buds = []

    def __str__(self):
        return f'Bud: {self.index} Angle: {self.angle:.3f} \n' \
               f'To_buds: {self.to_buds} From_buds: {self.from_buds}'


if __name__ == '__main__':
    from plot import plot_tree
    new_tree = Yggdrasil(4)
    plot_tree(new_tree)
    print(new_tree)
    # print(set_to_buds(next_level: Level, bud: Bud, num_min, num_max, delta_ind: int))
    # print(find_closest_bud(new_tree.levels[2],
    #                        new_tree.levels[1].buds[2]))
    # print(set_to_buds(new_tree.levels[2], new_tree.levels[1].buds[0], 2, 5, 1))
