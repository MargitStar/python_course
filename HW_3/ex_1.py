number_list = []

while len(number_list) < 3:
    number_list.append(int(input()))

zero_count = number_list.count(0)

result = number_list[0] and number_list[1] and number_list[2]\
     or "Нет нулевых значений"
print(result)

result1 = number_list[0] or number_list[1] or number_list[2] or "Введены все нули"
print("Result 1",result1)

result = (number_list[0] == 0 and number_list[1] == 0 and\
 number_list[2] == 0) or "Нет нулевых значений"



# while zero_count == 0:
#     print("Нет нулевых значений!")
#     break
#
# while zero_count > 0:
#     print(0)
#     break

# while zero_count == 3:
#     print("Введены все нули!")
#     break

# for i in range(len(number_list)):
#     number_list.


if number_list[0] > number_list[1] + number_list[2]:
    print(number_list[0] - number_list[1] - number_list[2])
elif number_list[0] <= number_list[1] + number_list[2]:
    print(number_list[1] + number_list[2] - number_list[0])

if number_list[0] > 50 and (number_list[1] > number_list[0]\
     or number_list[2] > number_list[0]):
     print("Вася")
    
if number_list[0] == 5 or number_list[1] == number_list[2] == 7:
    print("Петя")


