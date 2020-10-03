"""Module with functions"""

from represetations import *


# Returns current time in hours, minutes and seconds
def get_current_time():
    import datetime
    time = datetime.datetime.now().time()
    return time.hour, time.minute, time.second


# Makes list of time digits and adds leading zero if it's needed
def digits_from_number(number):
    digit_list = []
    for digit in str(number):
        digit_list.append(digit)
    if len(digit_list) == 1:
        digit_list.insert(0, '0')

    return digit_list


# Prints the current time using digits representation
def get_my_numbers(time, separator, color):
    numbers = [digits_from_number(i) for i in time]
    print("\n\n")
    for i in range(5):
        components = []
        for num_list in numbers:
            components.append("  ".join(representations[num][i] for num in num_list))
        if i == 2:
            line = f"  {separator}  ".join(components)
        else:
            line = "      ".join(components)
        end_color = '\033[0m'
        print(color, line, end_color, end="")
        print()


# Clears the screen
def clear_the_screen():
    import os
    os.system('cls')


# Generate clock separator
def get_separator():
    while True:
        yield "\u2588\u2588"
        yield "\u25A0\u25A0"


# Generate colors for clock
def get_color():
    while True:
        yield '\033[36m'
        yield '\033[35m'
        yield '\033[37m'
