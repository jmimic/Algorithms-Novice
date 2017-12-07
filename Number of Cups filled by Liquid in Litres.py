"""
Coder: Jacky Shew
Description: Calculates Number of Cylinders able to be filled given cylinder Dimensions and Litres of liquid
"""

import math

def main(): #Line8 function called
	number_of_cups = calculate_number_of_cups(2, 3, 10, 20) #calls Line23 function
															#parameters: (bottom radius, top radius, height, liquid in litres)
	display_result(number_of_cups, 2, 3, 10, 20) #calls Line33 function
												 #parameters: (no. of cups, bottom radius, top radius, height, liquid in litres)

	number_of_cups = calculate_number_of_cups(7, 9, 15, 50) 
	display_result(number_of_cups, 7, 9, 15, 50)
	
	number_of_cups = calculate_number_of_cups(2, 4, 10, 30)
	display_result(number_of_cups, 2, 4, 10, 30)

	number_of_cups = calculate_number_of_cups(3, 5, 9, 40)
	display_result(number_of_cups, 3, 5, 9, 40)

def calculate_number_of_cups(bottom_radius, top_radius, height, litres_of_liquid): #Line23 function called
	volume_of_cups = calculate_cone_volume(bottom_radius, top_radius, height) #calls Line29 function
																			  #parameters: (bottom radius, top radius, height)
	cups = int(litres_of_liquid//(volume_of_cups/1000))
	return cups	

def calculate_cone_volume(bottom_radius, top_radius, height): #Line29 function called
	volume = (math.pi/3) * height * (bottom_radius**2 + bottom_radius*top_radius + top_radius**2)
	return volume
	
def display_result(cups, bottom_radius, top_radius, height, litres): #Line33 function called
	print(str(litres) + " litres will completely fill " + str(cups) + " cups with dimensions of "    \
					  + str(bottom_radius) + ", " + str(top_radius) + " and " + str(height) + ".")

main() #calls Line8 function
