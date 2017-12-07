"""
Coder: Jacky Shew
Description: Prints a list of words that contain a Particular Letter.
"""

def main():
	selected_words = get_selected_words("i", "The rain in Spain stays mainly in the plain") #change Param1 letter in words of Param2 sentence here
	print("List of words containing i:", selected_words)
	selected_words = get_selected_words("e", "The quick brown fox jumps over the lazy dog") #change Param1 letter in words of Param2 sentence here
	print("List of words containing e:", selected_words)
	
def get_selected_words(letter, sentence):
	words = sentence.lower()
	words_list = words.split()
	selected_words = []
	for word in words_list:
		if letter in word and word not in selected_words:
			selected_words += [word]
	return selected_words

			
main()
