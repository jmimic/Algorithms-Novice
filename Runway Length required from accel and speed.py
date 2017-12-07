"""
Coder: Jacky Shew
Description: Runway length required for x acceleration and y speed
Objective: Passes parameters into function that returns a calculation
"""

import math

def main():
	acceleration = 3.1 #change Acceleration value here
	speed = 60.5 #change Speed value here
	length = calculate_runway_length(acceleration, speed) #calls Line25 Function
	print("Runway length needed for an acceleration of " + str(acceleration) +  " and speed of " + str(speed) + " is", str(length) + " metres.")
	
	acceleration = 4.1 #change Acceleration value here
	speed = 61 #change Speed value here
	length = calculate_runway_length(acceleration, speed) #calls Line25 Function
	print("Runway length needed for an acceleration of " + str(acceleration) +  " and speed of " + str(speed) + " is", str(length) + " metres.")
	
	acceleration = 3.5 #change Acceleration value here
	speed = 60.0 #change Speed value here
	length = calculate_runway_length(acceleration, speed) #calls Line25 Function
	print("Runway length needed for an acceleration of " + str(acceleration) +  " and speed of " + str(speed) + " is", str(length) + " metres.")

def calculate_runway_length (acceleration, speed): #function called from Line 12
	minimum_runway_length = math.ceil(speed**2 / (2 * acceleration)) #uses parameter's arguments to calculate
	return minimum_runway_length
	
main() #calls Line9 function