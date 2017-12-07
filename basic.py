"""
Author: Jacky Shew
Date Written: 13/03/2015

Basic calculations

Variables and basic calculations using those variables (e.g. sphere radius, BMI) 
"""

import math

'''
Variables (3): No. of Days, Whole weeks of those No. of Days, 
and Days remaining after calculating Whole weeks
Prints:
> There are 84 weeks and 3 days in 591 days.
'''
number_of_days = 591
whole_weeks = number_of_days // 7
leftover_days = number_of_days % 7
print ("There are", whole_weeks, "weeks and", leftover_days, "days in", number_of_days, "days.")

'''
Variables (2): A sphere's radius, and Surface area of that sphere
Prints:
> The surface area of a sphere with a radius of 11 cms is 1521 sq cms.
'''
sphere_radius = 11
sphere_surface_area = round(4*math.pi*sphere_radius**2)
print ("The surface area of a sphere with a radius of", sphere_radius, "cms is", sphere_surface_area, "sq cms.")

'''
Variables (3): Some person's Height, Weight, and BMI 
using those Height, Weight measurements
Prints:
> Sally's bmi is 25.15.
'''
sally_height = 1.62
sally_weight = 66
sally_body_mass_index = round(sally_weight/sally_height**2,2)
print ("Sally's bmi is ", sally_body_mass_index, ".", sep="")

'''
Variables (4): Amount Invested, Interest rate, Years into the future, and
Value of the Investment after Years into the future with said Interest rate
Prints:
> Total value after 10 years would be $7163.39.
'''
amount_invested = 4000
interest_rate = 0.06
after_years = 10
total_value = round(amount_invested*(1+interest_rate)**after_years,2)
print ("Total value after ", after_years, " years would be $", total_value, ".", sep="") 
