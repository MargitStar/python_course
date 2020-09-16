amount_of_numbers = 0
number_list = []

while amount_of_numbers < 3:
    number_list.append(int(input()))
    amount_of_numbers += 1

if number_list[0] > number_list[1] + number_list[2]:
    print(number_list[0] - number_list[1] - number_list[2])
elif number_list[0] <= number_list[1] + number_list[2]:
    print(number_list[1] + number_list[2] - number_list[0])

if number_list[0] > 50 and (number_list[1] > number_list[0]\
     or number_list[2] > number_list[0]):
     print("Вася")
    
if number_list[0] == 5 or number_list[1] == number_list[2] == 7:
    print("Петя")


