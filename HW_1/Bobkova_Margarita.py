input_string = "Не знаю как там в Лондоне, я не была."\
    "Может, там собака - друг человека."\
    "А у нас управдом - друг человека!"

print("Original string: ", input_string)
print("The amount of symbles: ", len(input_string))
print("Reversed string: ", input_string[::-1])
print("Capitilized string: ", input_string.title())
print("Uppercased string: ", input_string.upper())
amount_of_nd = input_string.count("нд")
amount_of_or = input_string.count("ор")
print("Amount of 'нд' in string: ",amount_of_nd, input_string.count("о"),input_string.count("ам"))
print("Amount of 'ам' in string: ", input_string.count("ам"))
print("Amount of 'о' in string: ", input_string.count("о"))
print("Is amount of 'нд' higher than 'ор': ", amount_of_nd > amount_of_or)
