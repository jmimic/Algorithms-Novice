"""
Coder: Jacky Shew
Description: Prints subset of word list that are only 3 letters long
"""

def main():
	words_list = ["egg", "hello", "ego", "good", "pig", "aeroplane", "a", "rat"] #change Word values in type string here
	three_letter_words_list = create_3_letter_words_list(words_list)
	print(three_letter_words_list)
	
def create_3_letter_words_list(words_list):
	list = []
	for words in words_list:
		if len(words) == 3:
			list.append(words)
	return list
			
main()