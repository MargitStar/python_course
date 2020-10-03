"""Main module"""

from my_functions import *
from time import sleep

if __name__ == '__main__':
    separator = get_separator()
    color = get_color()
    time = None
    while True:
        if time != get_current_time():
            clear_the_screen()
            time = get_current_time()
            get_my_numbers(time, next(separator), next(color))
        sleep(0.3)