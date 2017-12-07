"""
Coder: Jacky Shew
Description: Counts Number of Words in a Sentence
"""

def main():
	user_sentence = get_sentence_from_user()
	words = count_words(user_sentence)
	print_number_of_words (user_sentence, words)
	
def get_sentence_from_user():
	sentence = input("Enter a sentence: ")
	return sentence
	
def count_words(sentence):
	if len(sentence) == 0:
		return 0
	count = 1
	for letter in sentence:
		if letter == " ":
			count += 1
	return count
	
def print_number_of_words(words, number_of_words):
	print("There are " + str(number_of_words) + " words in the sentence '" + words + "'.")	
	
main()