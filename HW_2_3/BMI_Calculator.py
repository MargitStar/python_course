"""This calculator helps you count your body index"""
max_index = 50
min_index = 10
people_dict = {}

print("Hello! This is a bmi calculator!")

while True:
    option = "1"
    if people_dict:
        print("Choose the option:\n1 - Create\n2 - Read\n3 - Update\n4 - Delete")
        option = input().strip()

    if option == "1":
        print("Please, enter your name!")
        name = input().title()
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
        age = int(age)
        people_dict[name]['age'] = age


        print("Please, enter your weight in kilos!")
        while True:
            try:
                weight = float(input())
                people_dict[name]['weight'] = weight
                break
            except ValueError:
                print("Weight could only be a number! Please, try again!")


        print("Please, enter your height in meters!")
        while True:
            try:
                height = float(input())
                people_dict[name]['height'] = height
                break
            except ValueError:
                print("Height could only be a number! Please, try again!")


        bmi_index = weight / (height ** 2)
        print(f"Your BMI index is {bmi_index}")

        equal_signs_before = int((bmi_index - min_index) / 2)
        equal_signs_after = int((max_index - bmi_index) / 2 - 1)
        print(f"{min_index}{'='*equal_signs_before}|{'='*equal_signs_after}{max_index}")
        print(' ' * (equal_signs_before + 1), round(bmi_index))

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
                print("Your weight is pretty high! Ask your children to do sport with you!")

    elif option == "2" or option == "3" or option == "4":
        print("Please, enter a name!")
        input_name = input().strip().title()
        while input_name not in people_dict:
            print("We don't have such person. Please, try again")
            input_name = input().strip().title()
        print("")

        if option == "2":
            for field, value in people_dict[input_name].items():
                print(f"{field.title()} - {value}")

        elif option == "3":
            print("Please enter an field you want to update! sex, age, weight, height.")
            field_to_update = input().strip().lower()
            while field_to_update not in people_dict[name]:
                print("We don't have such field. Please, try again")
                input_name = input().strip().title()
            print("Please enter new value!")
            new_value = input().strip().lower()

            if field_to_update == 'sex':
                while True:
                    if new_value != "woman" and new_value != "man":
                        print("Sex could be a woman or a man! Please, try again!")
                        new_value = input().strip().lower()
                    else:
                        break

            if field_to_update == "age":
                while True:
                    if not new_value.isnumeric():
                        print("Age could only be a number! Please, try again!")
                        new_value = input().strip().lower()
                    else:
                        break

            if field_to_update == "weight" or field_to_update == "heigth":
                while True:
                    try:
                        new_value = float(input())
                        break
                    except ValueError:
                        if field_to_update == 'weight':
                            print("Weight could only be a number! Please, try again!")
                        if field_to_update == "height":
                            print("Height could only be a number! Please, try again!")

            people_dict[input_name][field_to_update] = new_value
            print(f"Field {field_to_update} successfully updated!")

        elif option == "4":
            del people_dict[input_name]
            print(f"Person {input_name} successfully deleted!")
            
    
    print("\nList of users: ")
    if not people_dict:
        print("No users in the list")
    for index, person in enumerate(people_dict):
        print(f"{index+1}. {person}")

    print("To exit write QUIT. Press enter to continue!")
    choice = input()
    if choice == "QUIT":
        break
