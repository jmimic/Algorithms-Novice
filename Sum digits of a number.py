"""
Author: Jacky Shew
Description: Sums all digits of a number
"""

number = 932 #Change number here

number_string = str(number)
sum = int(number_string[0]) + int(number_string[1]) + int(number_string[2])

print("The sum of all digits in", number, "is", sum)