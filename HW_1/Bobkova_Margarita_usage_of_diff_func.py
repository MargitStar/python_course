input_string = "Не знаю как там в Лондоне, я не была."\
    "Может, там собака - друг человека."\
    "А у нас управдом - друг человека!"


# Using different functions 


print("Make only one Capital letter(the first one): "\
    , input_string.capitalize())
print("Encoded string: ", input_string.encode())
print("The first index of 'а':", input_string.find("а"))
print("The last index of 'а':", input_string.rfind("а"))
print("Is the string in lowercase? ", input_string.islower())
print("Is the string in uppercase? ", input_string.isupper())
print("Is the string titled? ", input_string.istitle())
print("Lowercased string: ", input_string.lower())
print("String 'а' with 'А': ", input_string.replace("а", "А"))
print("String splited by space: ", input_string.split(" "))
print("String with swaped case: ", input_string.swapcase())

# Checking simple operations with Strings

s1 = 'boy'
s2 = 'girl'

print("s1 equals s2? ",s1 == s2)
print("s1 + s2: ", s1 + s2)
print("adress of s1: ", id(s1))
print("adress of s2: ", id(s2))

s1 = s2
print("Is adress the same now?: ", id(s1) == id(s2))

s1 = 'boy'
print(f"{s1.title()} loves {s2}!")

print("Take the 3 element of s1: ", s1[2])

s3 = "Dogs can bite!"

print("symbols from first till the sixth(included): ", s3[0:6])

print("One letter every two: ", s3[::2])



