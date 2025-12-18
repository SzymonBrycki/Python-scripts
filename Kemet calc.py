import math

ja = 149597870700 # m

koniec_Oorta = 100000*ja # m

light_speed = 299792458 # m/s

predkosc_statku = light_speed / 100 # m/s

time_for_Oort_end = koniec_Oorta / predkosc_statku

seconds_in_minute = 60

minutes_in_hour = 60

hours_in_day = 24

days_in_year = 365

time_divisor = seconds_in_minute * minutes_in_hour * hours_in_day * days_in_year

time_formatted = time_for_Oort_end / time_divisor

print("Time of journey (POV of the spaceship)", time_formatted, "years")

time_dilatation = 1 / (math.sqrt(1 - (pow(predkosc_statku, 2) / pow(light_speed, 2)))) # gamma

time_dilatation_2 = time_dilatation * predkosc_statku

dil_formatted = time_dilatation_2 / time_divisor

print("Time on Earth: ", dil_formatted, "years")

#from Wikipedia

WikiDil = time_dilatation_2*(0.005/100) + time_dilatation_2

Wiki_format = WikiDil / time_divisor

print("Time on Earth (Wiki): ", Wiki_format, "years")

#WRONG!

# predkosc statku = time_dilation / math.sqrt(1 - (predkosc_statku * predkosc_statku / light_speed * light_speed))

gamma = (math.sqrt(1 - (pow(predkosc_statku, 2) / pow(light_speed, 2))))

time_dilation = predkosc_statku * gamma

time_dil_for = time_dilation / time_divisor

print("Spaceship time: ", time_formatted, "years")
print("Earth time: ", time_dil_for, "years")
