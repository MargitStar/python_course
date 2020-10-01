from my_functions import *
from time import sleep

if __name__ == '__main__':
    while True:
        clear_the_screen()
        time = get_current_time()
        get_my_numbers(time)
        sleep(0.25)
