"""
Coder: Jacky Shew
Description: Measures Wind-chill temperature
"""

fahrenheit = 23 #change Fahrenheit here
speed = 5 #change Speed here

wind_chill_index = 35.74+0.6215*fahrenheit-35.75*speed**0.16+0.4275*fahrenheit*speed**0.16 

print("The temperature in Fahrenheit is", fahrenheit)
print("The wind speed is", speed, "mph")
print("The wind chill index is", wind_chill_index)