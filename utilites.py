import math
import random
from main import Bud, Level

PI = 3.1415926
DPI = 2 * PI


def radius(lev: int, max_level: int) -> float:
    # Радиусы уровней. Степенной вариант
    coef = 0.88
    return (pow(coef, 1 + lev) - 1) / (pow(coef, max_level) - 1)


def angle(shift: float, index: int, num: int) -> float:
    # Угол почки
    return shift + 2 * index * PI / num


def shift(min, max) -> float:
    # Сдвиг уровня
    return random.uniform(min, max)


def number_buds(lev, max_index: int) -> int:
    # Число почек на уровне. Должно постепенно возрастать
    # Надо уточнить
    return int(random.uniform(lev + 2, 3 * (lev + 1)))


def circle_dist(ang1, ang2):
    # Расстояние по кругу в радианах
    dist = abs(ang1 - ang2) % DPI
    if dist >= PI:
        return DPI - dist
    else:
        return dist


def find_closest_bud(next_lev: Level, bud: Bud):
    # Находим ближайшую точку для данной со след уровня
    # TODO next_lev можно определять по самой точке

    new_dist = 10.
    new_bd = next_lev.buds[0]
    for bd in next_lev.buds:
        dist = circle_dist(bud.angle, bd.angle)
        if dist < new_dist:
            new_dist = dist
            new_bd = bd
    return new_bd.index


def select_buds(start, size, max, num: int):
    # Создаем массив start..start + size (c учетом круга по max)
    # и случайно выбираем из него num почек
    assert num < size, 'Wrong number of choice'
    data = [k % max for k in range(start, start + size)]
    return random.sample(data, num)


def set_to_buds(next_level: Level, bud: Bud, num_min, num_max, delta_ind: int):
    # Выбираем ростки для почки. Mежду min-max (Могут быть равны 0)
    # в диапазоне center_ind +- delta_ind с учетом круга
    num_to_bds = int(random.uniform(num_min, num_max + 1))
    center_ind = find_closest_bud(next_level, bud)
    return select_buds(center_ind - delta_ind, 2 * delta_ind,
                       next_level.num_buds, num_to_bds)


if __name__ == '__main__':
    # # Проверка радиусов
    # for n in range(7):
    #     print('Lev ', n, 'Rad ', radius(n, 10))
    #
    # # Проверка углов
    # print(angle(0.0, 2, 3))
    print(circle_dist(6.2, 1.1))
