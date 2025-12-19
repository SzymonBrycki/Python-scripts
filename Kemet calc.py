import math

# au = astronomical units

au = 149597870700 # m

# end of the Oort cloud

Oort_end = 100000*au # m

light_speed = 299792458 # m/s

#speed of shaceship (1/100 of the light speed)

spaceship_speed = light_speed / 100 # m/s

#time when spaceship will reach end of Oourt cloud

time_for_Oort_end = Oort_end / spaceship_speed #POV of Earth!

seconds_in_minute = 60

minutes_in_hour = 60

hours_in_day = 24

days_in_year = 365

time_divisor = seconds_in_minute * minutes_in_hour * hours_in_day * days_in_year

time_formatted = time_for_Oort_end / time_divisor

print("Time of journey (POV of the Earth)", time_formatted, "years")

gamma = (math.sqrt(1 - (pow(spaceship_speed, 2) / pow(light_speed, 2))))

time_on_spaceship = time_for_Oort_end / gamma

time_formatted_2 = time_on_spaceship / time_divisor

print("Time on the Spaceship: ", time_formatted_2, "years")

'''
#from Wikipedia

WikiDil = time_dilatation_2*(0.005/100) + time_dilatation_2

Wiki_format = WikiDil / time_divisor

print("Time on Earth (Wiki): ", Wiki_format, "years")

#WRONG!

# spaceship_speed = time_dilation / math.sqrt(1 - (spaceship_speed * spaceship_speed / light_speed * light_speed))

gamma = (math.sqrt(1 - (pow(spaceship_speed, 2) / pow(light_speed, 2))))

time_dilation = spaceship_speed * gamma

time_dil_for = time_dilation / time_divisor

print("Spaceship time: ", time_formatted, "years")
print("Earth time: ", time_dil_for, "years")

# scapeship speed = time_dilation * gamma

time_dilation = spaceship_speed / gamma

time_dil_final = time_dilation / time_divisor

print("Spaceship time: ", time_formatted, "years")
print("Earth time: ", time_dil_final, "years")
'''