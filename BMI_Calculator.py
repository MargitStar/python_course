print("Please, enter your weight in kilos!")
weight = float(input())
print("Please, enter your height in meters!")
height = float(input())

bmi_index = weight / (height ** 2)

print(f"Your BMI index is {bmi_index}")
print(f"10{'='*int((bmi_index - 10)/2)}|{'='*int((50 - bmi_index)/2 - 1)}50")
print(' ' * (int((bmi_index - 10) / 2) + 1), round(bmi_index))

