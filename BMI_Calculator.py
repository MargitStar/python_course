print("Please, enter your weight in kilos!")
weight = float(input())
print("Please, enter your height in meters!")
height = float(input())

bmi_index = weight / (height ** 2)

print(f"Your BMI index is {bmi_index}")
equal_signs_before = int((bmi_index - 10) / 2)
equal_signs_after = int((50 - bmi_index) / 2 - 1)
print(f"10{'='*equal_signs_before}|{'='*equal_signs_after}50")
print(' ' * (equal_signs_before + 1), round(bmi_index))