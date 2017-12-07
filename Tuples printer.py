"""
Coder: Jacky Shew
Description: Prints a list of Tuples of pairs
"""

def main(): 
	pairs_list = [("salt", "pepper"), ("chalk", "cheese"),
				  ("noughts", "crosses"), ("night", "day")]
	print_pairs(pairs_list)
	
def print_pairs(pairs_list):
	for word in pairs_list:
		pair_1 = word[0]
		pair_2 = word[1]
		print (pair_1, "and", pair_2)
	
main()