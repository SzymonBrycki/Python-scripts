def CtoK(celcius):
	kelvin = 273,15 + celcius
	return kelvin

def CtoF(celcius):
	fahrenheit = 32 + ( 9 / 5 * celcius)
	return fahrenheit

def KtoC(kelvin):
	celcius = kelvin - 273.15
	return celcius

def KtoF(kelvin):
	fahrenheit = 1.8 * (kelvin - 273) + 32
	return fahrenheit

def FtoC(fahrenheit):
	celcius = (fahrenheit - 32) * 5 / 9
	return celcius

def FtoK(fahrenheit):
	kelvin = (fahrenheit + 459.67) * 5 / 9
	return kelvin

print("Welcome to the temperature calculator! Enter the temperature below to find its value in different degrees!")

type_of_degrees = str(input("What kind of degrees you wanna recalculate? [C/F/K] "))

temperature_value = int(input("Enter the number of degrees "))

if type_of_degrees == "C" or "F" or "K":
	if type_of_degrees == "C":
		celcius = temperature_value
	elif type_of_degrees == "F":
		fahrenheit = temperature_value
	else:
		kelvin = temperature_value
else: 
	raise ValueError("Unknown type of temperature!")

print(temperature_value, type_of_degrees)