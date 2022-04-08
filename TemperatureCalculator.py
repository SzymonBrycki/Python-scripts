################################################
#          FUNCTIONS AND GLOBAL VARIABLES
################################################

return_string = None

def CtoK(celcius):
	kelvin = 273.15 + celcius
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

def get_return_string(type_of_degrees):

	global return_string

	if type_of_degrees.upper() == "C":
		return_string = "C"
	elif type_of_degrees.upper() == "F":
		return_string = "F"
	else:
		return_string = "K"

'''
def set_temperature(temperature_value):

	global celcius
	global fahrenheit
	global kelvin

	if return_string == "C":
		celcius = temperature_value
	elif return_string == "F":
		fahrenheit = temperature_value
	else:
		kelvin = temperature_value
'''

def print_results():
	if return_string.upper() == "C":
		print(temperature_value, "Celcius is", CtoK(temperature_value), "Kelvin")
		print(temperature_value, "Celcius is", CtoF(temperature_value), "Fahrenheit")
	elif return_string.upper() == "F":
		print(temperature_value, "Fahrenheit is", FtoC(temperature_value), "Celcius")
		print(temperature_value, "Fahrenheit is", FtoK(temperature_value), "Kelvin")
	elif return_string.upper() == "K":
		print(temperature_value, "Kelvin is", KtoC(temperature_value), "Celcius")
		print(temperature_value, "Kelvin is", KtoF(temperature_value), "Fahrenheit")

################################################
#          PROGRAM
################################################

print("Welcome to the temperature calculator! Enter the temperature below to find its value in different degrees!")

type_of_degrees = str(input("What kind of degrees you wanna recalculate? [C/F/K] "))

if type_of_degrees.upper() != "C" and type_of_degrees.upper() != "F" and type_of_degrees.upper() != "K":
	raise Exception("Wrong value! Should be C or F or K!")

temperature_value = int(input("Enter the number of degrees "))

get_return_string(type_of_degrees)
print_results()
