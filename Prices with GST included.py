"""
Coder: Jacky Shew
Description: Produces a list of Prices with GST added
"""

def main():
	price_list = [12.45, 2.56, 10.79, 8.36, 9.27] #change Price values here
	prices_with_gst = add_gst(price_list)
	print("Prices without GST:    ", price_list)
	print("Prices with GST added: ", prices_with_gst)
	
	
def add_gst(price_list):
	gst_list = []
	for gst in range(len(price_list)):
		gst = round(price_list[gst]*1.15,2) #change Param1 for GST value and Param2 for rounding decimal here
		gst_list.append(gst)
	return gst_list
		
	
main()