PI = 3.1415926
import math
import random


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


def random_divide(total, num, min, max: int):
    # Число total делиться на num случайных слагаемых, каждое от min max
    pass


if __name__ == '__main__':
    # Проверка радиусов
    for n in range(7):
        print('Lev ', n, 'Rad ', radius(n, 10))

    # Проверка углов
    print(angle(0.0, 2, 3))
