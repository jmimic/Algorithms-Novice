"""
Coder: Jacky Shew
Description: Produces a list of prime numbers within a range (userinput)
"""

def main():
	start = int(input("Enter start of range: "))
	end = int(input("Enter end of range: "))
	print()
	print("Prime numbers from", start, "to", end, "inclusive:")
	prime_number_list = create_prime_number_list(start, end)
	print(prime_number_list)

def create_prime_number_list(start, end):
	prime_number_list = []
	for number in range(start, end+1):
		numbers = is_a_prime_number(number)
		if numbers == True:
			prime_number_list.append(number)
	return prime_number_list	
				
def is_a_prime_number(number):
	if number < 2:
		return False
	divisor = 2
	while divisor < number:
		if number % divisor == 0:
			return False
		divisor += 1
	return True
			
main()
