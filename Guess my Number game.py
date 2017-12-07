"""
Coder: Jacky Shew
Description: Guess my Number game
"""
import random

def main():
	play_guessing_game()
	
def play_guessing_game():
	target_number = random.randrange(1,100)
	guess = 0
	while guess != target_number:
		guess = get_guess_from_user()
		if guess > target_number:
			print (guess, "is too high")
		elif guess < target_number:
			print (guess, "is too low")
		elif guess == target_number:
			print ("That is correct. Congratulations!")
	
	
def get_guess_from_user():
	guess = int(input("Guess a number between 1 and 100: "))
	return guess
	
main()