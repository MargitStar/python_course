from my_functions import *
from time import sleep


def separator():
    flag = False
    while True:
        if flag:
            yield "\u2588\u2588"
        else:
            yield "  "
        flag = not flag


if __name__ == '__main__':
    separator = separator()
    while True:
        clear_the_screen()
        time = get_current_time()
        get_my_numbers(time, next(separator))
        sleep(0.5)
