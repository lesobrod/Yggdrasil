import matplotlib.pyplot as plt
from main import Yggdrasil, Level, Bud


def plot_tree(tree: Yggdrasil) -> None:
    fig, ax = plt.subplots()
    for level in tree.levels:
        for bud in level.buds:
            ax.plot(bud.x, bud.y, 'ro')

    ratio = 1.0
    x_left, x_right = ax.get_xlim()
    y_low, y_high = ax.get_ylim()
    ax.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * ratio)
    plt.show()
