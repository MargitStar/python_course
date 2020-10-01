from represetations import *


def get_current_time():
    import datetime
    time = datetime.datetime.now().time()
    return time.hour, time.minute, time.second


def digits_from_number(number):
    return [char for char in str(number)]


def get_list_of_numbers(time):
    numbers = [digits_from_number(i) for i in time]
    for i in numbers:
        if len(i) == 1:
            i.insert(0, '0')
    return [digit for number in numbers for digit in number]


def get_my_numbers(time):
    numbers = get_list_of_numbers(time)
    for i in range(5):
        for number in numbers:
            # if number == numbers[1] or number == numbers[3] and i == 3:
            #     print(representations[number][i], end='   \u2588   ')
            # if number == numbers[1] or number == numbers[3]:
            #     print(representations[number][i], end='       ')
            # else:
            print(representations[number][i], end='   ')
        print('')


def clear_the_screen():
    import os
    os.system('cls')
