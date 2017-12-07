"""
Coder: Jacky Shew
Description: Appends Temperature values (userinput) into text file

Objective: Retrieve Temperature values from user. Append values into text file.
"""

def main():
	temperatures_list = get_temperatures_from_user()
	append_temperatures("temperatures.txt", temperatures_list)

def get_temperatures_from_user():
	temperatures = input("Enter temperatures separated by a comma: ")
	temperatures_list = temperatures.split(",")
	for i in range (0,len(temperatures_list)):
		temperatures_list[i] = int(temperatures_list[i].strip())
	return temperatures_list
	
def append_temperatures(temperatures_filename, temperatures_list):
	output_file = open(temperatures_filename,'a')
	for temp in temperatures_list:
		temp = str(temp)
		output_file.write(" " + temp)
	output_file.close()
	
main()