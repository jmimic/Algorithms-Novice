"""
Coder: Jacky Shew
Description: Checks whether a word is a palindrome.

Palindrome: word == word.reverse()
"""

def main():
	word = get_word_from_user()
	while len(word) > 0:
		print_palindrome_result(word)
		word = get_word_from_user()
	print("Goodbye")
	
def get_word_from_user():
	word = input ("Enter a word: ")
	return word

def is_a_palindrome(word):
	if word == word[::-1]:
		return True
	else:
		return False
	
def print_palindrome_result(word):
	if is_a_palindrome(word):
		print(word + " is a palindrome")
	else:
		print(word + " is not a palindrome")
	
main()
