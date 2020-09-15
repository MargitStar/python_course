"""This calculator helps you count your body index"""

print("Please, enter your weight in kilos!")
weight = float(input())
print("Please, enter your height in meters!")
height = float(input())

bmi_index = weight / (height ** 2)
print(f"Your BMI index is {bmi_index}")

max_index = 50
min_index = 10

equal_signs_before = int((bmi_index - min_index) / 2)
equal_signs_after = int((max_index - bmi_index) / 2 - 1)
print(f"{min_index}{'='*equal_signs_before}|{'='*equal_signs_after}{max_index}")
print(' ' * (equal_signs_before + 1), round(bmi_index))

