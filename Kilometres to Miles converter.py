"""
Coder: Jacky Shew
Description: Converts Kilometres (input) to Miles

Input: Positive Integer
"""

def main():
	kilometres = get_kilometres_from_user()
	miles = convert_kilometres_to_miles(kilometres)
	print_conversion(kilometres, miles)
	
def get_kilometres_from_user():
	user_kilometres = float(input("Enter kilometres: "))
	return user_kilometres

def convert_kilometres_to_miles(kilometres):
	convert_kilometres = round(float(kilometres * 0.621371),2)
	return convert_kilometres
	
def print_conversion(kilometres, miles):
	print(kilometres, "kms is equivalent to", miles, " miles.")
	
main()