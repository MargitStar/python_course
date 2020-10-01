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


def get_my_numbers(time, separator):
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
        print(line, end="")
        print()


def clear_the_screen():
    import os
    os.system('cls')
