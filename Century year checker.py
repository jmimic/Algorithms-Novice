"""
Coder: Jacky Shew
Description: Checks which given years are Century years
"""

def main():
	years = [1200, 2015, 1900, 1642, 2900, 1962, 1700] #change Year value to check
	print_century_years(years)
	
def print_century_years(years_list):
	print ("Century Years")
	print ("="*13)
	for year in years_list:
		if year %100 == 0:
			print (year, end=' ')
	
main()