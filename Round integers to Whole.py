"""
Coder: Jacky Shew
Description: Rounds a list of numbers to Whole numbers
"""

def main():
	numbers = [7.5, 8.5, 7.3, 3.7, 4.21, 5.25, 49.18]
	print("Original list of numbers:", numbers)
	round_to_whole_numbers(numbers)
	print("List of numbers is now:  ", numbers)
	
def round_to_whole_numbers(numbers_list):
	list = []
	for numbers in range(len(numbers_list)):
		numbers_list[numbers] = round(numbers_list[numbers])
		list.append(numbers)
	return list
	
main()