from my_functions import *
from time import sleep

if __name__ == '__main__':
    while True:
        time = get_current_time()
        get_my_numbers(time)
        clear_the_screen()
        sleep(0.3)
