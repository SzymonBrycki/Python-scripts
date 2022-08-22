print("Welcome to the BMI Calculator. Enter your data balow.")

mass = int(input("Your weight in kilograms? "))
height = float(input("Your height in meters? "))

BMI = mass / height**2

print("Your BMI is %.2f" % BMI)