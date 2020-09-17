number_list = []

while len(number_list) < 3:
    number_list.append(int(input()))
print()

print("#1")
result = number_list[0] and number_list[1] and number_list[2] and "Нет нулевых значений"
print(result,"\n")

print("#2")
result1 = number_list[0] or number_list[1] or number_list[2] or "Введены все нули"
print(result1,"\n")

print("#34")
if number_list[0] > number_list[1] + number_list[2]:
    print(number_list[0] - number_list[1] - number_list[2],"\n")
elif number_list[0] <= number_list[1] + number_list[2]:
    print(number_list[1] + number_list[2] - number_list[0],"\n")


if number_list[0] > 50 and (number_list[1] > number_list[0]\
     or number_list[2] > number_list[0]):
     print("#5")
     print("Вася\n")

    
if number_list[0] == 5 or number_list[1] == number_list[2] == 7:
    print("#6")
    print("Петя")


