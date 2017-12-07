"""
Coder: Jacky Shew
Description: Finds the Smallest Word in a list of words
"""

def main():
	words_list = ["short", "bye", "short", "cat", "pig", "pig", "elephant", "at", "bye", "hello", "pig"] #change Values here
	smallest_word = get_smallest_word(words_list)
	print('"' + smallest_word + '"' + " is the smallest word in the list.")
	
def get_smallest_word(words_list):
	smallest_word = words_list
	for word in words_list:
		if len(smallest_word) > len(word):
			smallest_word = word
	return smallest_word
			
main()