"""
Coder: Jacky Shew
Description: No. of Items calculates Boxes and Cost
"""

def main(): #function called by Line30
	items = get_number_of_items() #calls Line13 function, retrieves userinput <int>
	boxes_needed = calculate_boxes_needed(items) #calls Line16 function, uses Line7 argument, retrieves no. of boxes required
	cost = calculate_cost(boxes_needed) #calls Line23 function, uses Line8 argument, retrieves cost of boxes
	print_boxes_needed_and_cost(items, boxes_needed, cost) #calls Line26 function to print using Line7,8,9 arguments
	
def get_number_of_items(): #function called by Line7
	number_of_items = int(input("Enter number of items: ")) #userinput for no. of items
	return number_of_items

def calculate_boxes_needed(items): #function called by Line8
	boxes = items // 10
	items_left_over = items % 10
	if items_left_over > 0:
		boxes += 1
	return boxes

def calculate_cost(boxes): #function called by Line9
	return 8 * min(boxes, 6) + 5 * max(boxes - 6, 0)

def print_boxes_needed_and_cost(items, boxes_needed, cost): #function called by Line10
	print("Boxes needed: " + str(boxes_needed)) #end
	print("Cost: $" + str(cost)) #end
	
main() #call Line6 function