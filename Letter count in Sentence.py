"""
Coder: Jacky Shew
Description: Prints letter count in a sentence (userinput)

Objective: Use of Dictionary
"""
def main():
	sentence = get_sentence_from_user()
	sentence = sentence.lower()
	letter_counts_dict = count_letter_occurrences(sentence)
	print(letter_counts_dict)
	
def get_sentence_from_user():
	sentence = input("Enter a sentence: ")
	return sentence

def count_letter_occurrences(sentence):
	word_dict = {}
	for i in sentence:
		if i.isalpha():
			if i in word_dict:
				word_dict[i] += 1
			else:
				word_dict[i] = 1
	return word_dict
		
main()