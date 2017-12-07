"""
Coder: Jacky Shew
Description: Calculates BMI based on Weight(Kg) and Height(m)
"""

def main():
	weight = get_weight_from_user()
	height = get_height_from_user()
	bmi = calculate_bmi(weight, height)
	display_bmi_message(bmi)
	
def get_weight_from_user():
	return float(input("Enter weight (kilograms): "))
	
def get_height_from_user():
	return float(input("Enter height (metres): "))

def calculate_bmi(weight, height):
	bmi = round(weight / height ** 2)
	return bmi

def display_bmi_message(bmi):
	print ("bmi is ", bmi)
	if bmi > 25:
		print ("Weight may be too high.")
	elif bmi < 19:
		print ("Weight may be too low.")
	else:
		print ("This is a healthy weight.")
		
main()