import math
import random
from main import Point, Level

PI = 3.1415926
DPI = 2 * PI


def radius(lev: int, max_level: int) -> float:
    # Радиусы уровней. Степенной вариант
    coef = 0.88
    return (pow(coef, 1 + lev) - 1) / (pow(coef, max_level) - 1)


def angle(shift: float, index: int, num: int) -> float:
    return shift + 2 * index * PI / num


def shift(min, max) -> float:
    return random.uniform(min, max)


def number_points(lev: int) -> int:
    # Число точек на уровне. Должно постепенно возрастать
    return int(random.uniform(lev + 2, 3 * (lev + 1)))


def circle_dist(ang1, ang2):
    # Расстояние по кругу в радианах
    dist = abs(ang1 - ang2) % DPI
    if dist >= PI:
        return DPI - dist
    else:
        return dist


def find_closest_point(next_lev: Level, point: Point):
    # Находим ближайшую точку для данной со след уровня
    new_dist = 10.
    new_pt = next_lev.points[0]
    for pt in next_lev.points:
        dist = circle_dist(point.angle, pt.angle)
        if new_dist < dist:
            new_dist = dist
            new_pt = pt
    return new_pt.index


def select_points(start, size, max, num: int):
    # Создаем массив start..start + size (c учетом круга по max)
    # и случайно выбираем из него num точек
    data = [k % max for k in range(start, start + size)]
    return random.choices(data, k=num)


def set_to_points(next_level: Level, point: Point, num_min, num_max, delta_ind: int):
    # Выбираем ростки для точки. Mежду min-max (Могут быть равны 0)
    # в диапазоне center_ind +- delta_ind с учетом круга
    num_to_pts = int(random.uniform(num_min, num_max + 1))
    center_ind = find_closest_point(next_level, point)
    return select_points(center_ind - delta_ind, 2 * delta_ind,
                         next_level.num_points, num_to_pts)


if __name__ == '__main__':
    # # Проверка радиусов
    # for n in range(7):
    #     print('Lev ', n, 'Rad ', radius(n, 10))
    #
    # # Проверка углов
    # print(angle(0.0, 2, 3))
    print(circle_dist(6.2, 1.1))
