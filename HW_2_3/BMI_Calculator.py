"""This calculator helps you count your body index"""
max_index = 50
min_index = 10
people_dict = {}

print("Hello! This is a bmi calculator!")

while True:
    print("Please, enter your name!")
    name = input()
    people_dict[name] = {}

    print("Please, enter your sex!")
    while True:
        sex = input()
        if sex != "woman" and sex != "man":
            print("Sex could be a woman or a man! Please, try again!")
        else:
            break
    people_dict[name]['sex'] = sex


    print("Please, enter your age!")
    while True:
        age = input()
        if not age.isnumeric():
            print("Age could only be a number! Please, try again!")
        else:
            break
    people_dict[name]['age'] = int(age)


    print("Please, enter your weight in kilos!")
    weight = float(input())
    people_dict[name]['weight'] = weight


    print("Please, enter your height in meters!")
    height = float(input())
    people_dict[name]['height'] = height


    bmi_index = weight / (height ** 2)
    print(f"Your BMI index is {bmi_index}")

    equal_signs_before = int((bmi_index - min_index) / 2)
    equal_signs_after = int((max_index - bmi_index) / 2 - 1)
    print(f"{min_index}{'='*equal_signs_before}|{'='*equal_signs_after}{max_index}")
    print(' ' * (equal_signs_before + 1), round(bmi_index))

    print("To exit write QUIT. To continue write CONT!")
    choise = input()
    if choise == "QUIT":
        break

print("\nList of users: ")
for index, person in enumerate(people_dict):
    print(f"{index+1}. {person}")
