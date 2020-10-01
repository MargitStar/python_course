from represetations import *


def get_current_time():
    import datetime
    time = datetime.datetime.now().time()
    return time.hour, time.minute, time.second


def digits_from_number(number):
    digit_list = []
    for digit in str(number):
        digit_list.append(digit)
    if len(digit_list) == 1:
        digit_list.insert(0, '0')

    return digit_list


def get_my_numbers(time):
    numbers = [digits_from_number(i) for i in time]
    print("\n\n")
    counter = 0
    for i in range(5):
        for num_list in numbers:
            line = ''
            for number in num_list:
                line += representations[number][i]
                line += "  "
            if i == 2 and counter < 2:
                line += " \u2588   "
                counter += 1
            else:
                line += "     "
            print(line, end="")
        print()


def clear_the_screen():
    import os
    os.system('cls')
