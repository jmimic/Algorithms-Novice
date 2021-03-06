'''
Coder: Jacky Shew
Description: Paints a Pattern

Objective: Use of Tkinter
'''

from tkinter import * 
 
def draw_pattern_in_canvas(canvas): 
	grid_size = 50
	for row in range(0,7):
		fill_in = row % 2 == 0
		for column in range (0,10):
			if fill_in:
				canvas.create_rectangle(column * grid_size, row * grid_size,(column + 1) * grid_size, (row + 1) *grid_size, fill = 'green', width = 3)
			else:
				canvas.create_oval(column * grid_size, row * grid_size, (column + 1) * grid_size, (row + 1) * grid_size, fill = 'white', width = 3)
				canvas.create_line(column * grid_size + grid_size / 2, row * grid_size, column * grid_size + grid_size / 2, row * grid_size + grid_size, width = 3)
				canvas.create_line(column * grid_size, row * grid_size + grid_size / 2, column * grid_size  + grid_size, row * grid_size + grid_size / 2, width = 3)
			fill_in = not fill_in
			
def draw_grid(a_canvas):
	for row in range(50, 350, 50):
		a_canvas.create_line(-1, row, 501, row, fill = "lightblue")
	for column in range(50, 500, 50):
		a_canvas.create_line(column, -1, column, 351, fill = "lightblue")
		
def main(): 
	window = Tk()  
	window.title("Green and White Pattern")  
	window.config(background = 'white')   
	window.geometry("500x350+10+20") 

	a_canvas = Canvas(window) 
	a_canvas.config(background = "white")   
	a_canvas.pack(fill = BOTH, expand = True) #Canvas fills the whole top level window 
	draw_grid(a_canvas)
	draw_pattern_in_canvas(a_canvas) 
	window.mainloop()   
 
main()