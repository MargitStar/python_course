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
        sex = input().strip().lower()
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

    if sex == "woman":
        if age < 18:
            if bmi_index >= 18.5 and bmi_index <= 25:
                print("Your body condition is great! Keep going!")
            if bmi_index < 18.5:
                print("Your weight is very low! Try to eat more!")
            if bmi_index > 25:
                print("your weight is pretty high! Try to eat less!")
        
        if age >= 18 and age <= 45:
            if bmi_index > 18.5 and bmi_index <= 25:
                print("Your body condition is great! Your lifestyle is great! Keep going!")
            if bmi_index < 18.5:
                print("Your weight is very low! Please, visit a doctor. You might have health problems!")
            if bmi_index > 25:
                print("your weight is pretty high! Overweight can cause different health problems!")
        
        if age > 45:
             if bmi_index > 18.5 and bmi_index <= 25:
                print("Your body condition is great! You did great during your life!")
            if bmi_index < 18.5:
                print("Your weight is very low! Ask your children to give you some food!")
            if bmi_index > 25:
                print("your weight is pretty high! Ask your children to do sport with you!")

    print("To exit write QUIT. Press enter to continue!")
    choice = input()
    if choice == "QUIT":
        break

print("\nList of users: ")
for index, person in enumerate(people_dict):
    print(f"{index+1}. {person}")
