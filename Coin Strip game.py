"""
Coder: Jacky Shew
Description:  Coin  Strip game

This  game  requires two  players starting off with: 
A  row  of  9  spaces  with  4  coins  placed  randomly  along  the  nine spaces.   
Each  of  the  players  takes  turns  moving  a  coin. 

* How  coins  may  be  moved:  
- Two  coins  may  not  share  a  space. 
- No  coin  may  pass  another  coin. 
- Coins  only  move  to  the  left. 
- Within  these  restrictions,  coins  can  move  any  number  of  spaces.  

* Winning Condition:
The  game  finishes  when  all  the  coins  are  lined  up  on  the  left  and  no  more  coins  can  be 
moved.  The  last  player  to  move  a  coin  is  the  winner.  
(This  means  that  the  first  person  who cannot  move  a  coin  loses.)
"""

"""
Note: Game does not raise exceptions if an illegal move has been made i.e. moving coin into occupied slot
"""

import random

def create_game_string():
	game_line = " $ $ $ $ "
	game_line = jumbled_game_line(game_line)
	return game_line

def jumbled_game_line(game_line):
	count = 0
	while count < 7:
		count += 1
		random_position = random.randrange(0,9)
		start_to_position = game_line[:random_position]
		position_to_end = game_line [random_position+1:]
		removed_character = game_line[random_position]
		game_line = start_to_position + position_to_end + removed_character
	return game_line

def display_game_string(game_string):
	print("\n     ", "1" ,"      ", "2", "      ", "3", "     ", "4", "      ", "5", "      ", "6", "      ", "7", "      ", "8", "       ", "9", "     ")
	print("||    ","   |   ","    |   ","    |   ","    |   ","   |   ","     |   ","    |   ","    |   ", "    ||")
	print("||    " + game_string[0] + "   |    " + game_string[1] + "   |    " + game_string[2] + "   |   " + game_string[3] + "    |   " + game_string[4] + "   |    " + game_string[5] + "    |   " + game_string[6] + "    |   " + game_string[7] + "    |    " + game_string[8] + "   ||")
	print("||    ","   |   ","    |   ","    |   ","    |   ","   |   ","     |   ","    |   ","    |   ", "    ||\n")
	
def get_user_position_num(player_number):
	print("PLAYER NUMBER: ", player_number)
	position_number = input("Enter position number: ")
	return position_number
	
def get_num_to_move():
	to_move = input("Enter number to move: ")
	return to_move
	
def move_dollar_to_the_left(game_string, position_num, to_move):
	game_string = game_string[0:int(position_num)-1] + " " + game_string[int(position_num):]
	game_string = game_string[0:int(position_num)-int(to_move)-1] + "$" + game_string[int(position_num)-int(to_move):]
	return game_string
	
	
def get_next_player_num(player_num):
	if player_num == 1:
		return 2
	else:
		return 1
	
def congratulate_player(player_num):
	print ("=" * 25)
	print ("** Y O U H A V E W O N **")
	print (" " * 3, "PLAYER NUMBER:", player_num, " " * 4)
	print ("** Y O U H A V E W O N **")
	print ("=" * 25)
	print("\nBYE FROM COIN STRIP\n")

def display_menu():
	user_input = input ("1. PLAY COIN STRIP \n2. EXIT \nEnter selection: ")
	user_input = int(user_input)
	if user_input == 1:
		play_one_game()
	elif user_input == 2:
		print("\nBYE FROM COIN STRIP\n")
		
# CHECK IF THE GAME HAS FINISHED
def check_game_finished(game_string):
	first_four_symbols = game_string[0:4]
	if first_four_symbols == "$$$$":
		return True
	return False

# PLAY ONE GAME OF COIN STRIP
def play_one_game():
	player_num = 1
	
	game_finished = False
	game_string = create_game_string()
	
	while game_finished == False:
		display_game_string(game_string)
		position_num = get_user_position_num(player_num)
		move_num = get_num_to_move()
		game_string = move_dollar_to_the_left(game_string,position_num, move_num)
		game_finished = check_game_finished(game_string)
		
		if game_finished:
			display_game_string(game_string)
			congratulate_player(player_num)
		else:
			player_num = get_next_player_num(player_num)
		
def main():
	display_menu()
	
main()