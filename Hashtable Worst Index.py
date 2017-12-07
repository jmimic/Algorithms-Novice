'''
Coder: Jacky Shew
Description: Using Hashtable Linear Probing, find the worst index position

Explanation for 'worst index position': In the event of a collision at chosen 'worst index'
										the probing to an unused index is longest
'''
# Program begins at Line42

class MyHashTable:
	
	def __init__(self, capacity):
		self.capacity = capacity
		self.slots = [None]*capacity
		
	def insert(self, key):
		value = key
		while self.slots[key % self.capacity] != None:
			key += 1
		self.slots[key % self.capacity] = value
		return self.slots
		
	def probe_check(self, key):
		count = 0
		while self.slots[key % self.capacity] != None:
			key += 1
			count += 1
		return count
		
def q2(size,values):
	table = MyHashTable(size)
	amount_of_probes = []
	worst_index_list = []
	for i in values: table.insert(i)
	for i in range(size): 
		amount_of_probes.append(table.probe_check(i))
	worst_number = max(amount_of_probes)
	for i in range(size):
		if amount_of_probes[i] == worst_number:
			worst_index_list.append(i)
	return worst_index_list
	
values = [25, 32, 88, 10, 35, 11] #Change hashtable values here
worst = q2(11, values) #Change Param1: Size here
print(worst)