from my_functions import *
from time import sleep


def separator():
    while True:
        yield "\u2588\u2588"
        yield "\u25A0\u25A0"


def get_colors():
    while True:
        yield '\033[36m'
        yield '\033[35m'
        yield '\033[37m'


if __name__ == '__main__':
    separator = separator()
    color = get_colors()
    while True:
        clear_the_screen()
        time = get_current_time()
        get_my_numbers(time, next(separator), next(color))
        sleep(0.5)
