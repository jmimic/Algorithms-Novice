"""
Coder: Jacky Shew
Description: Prints all Weekdays then by every second day of the week starting with Monday.
"""

def main(): 
	days_tuple = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
	print("Days of Week:",days_tuple, "\n")
	weekdays = get_weekdays(days_tuple)
	alternate_days = get_alternate_days(days_tuple)
	print("Weekdays:", weekdays, "\n")
	print("Alternate days:", alternate_days)
	
def get_weekdays(days_tuple):
	days_tuple = tuple(days_tuple)
	return days_tuple[:5]

def get_alternate_days(weekdays_tuple):
	weekdays_tuple = tuple(weekdays_tuple)
	return weekdays_tuple[::2]
	

main()