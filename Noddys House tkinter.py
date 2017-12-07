'''
Coder: Jacky Shew
Description: Paints Noddy's House

Objective: Use of Tkinter
'''

from tkinter import * 

def draw_in_canvas(canvas):
	grid_size = 50
	canvas.create_polygon(50,100,125,25,200,100, fill = 'red')
	canvas.create_rectangle(50,100,200,250, fill = 'yellow')
	canvas.create_rectangle(50,100,100,150, fill = 'white')
	canvas.create_rectangle(150,100,200,150, fill = 'white')
	canvas.create_line(50,100,100,150)
	canvas.create_line(50,150,100,100)
	canvas.create_line(150,100,200,150)
	canvas.create_line(150,150,200,100)
	canvas.create_rectangle(100,175,150,250, fill = 'blue')
	canvas.create_oval(100,210,110,220, fill = 'yellow')
	my_font = ("Courier", 15, "bold")
	canvas.create_text(125,260, text = "Noddy's House", font = my_font)

def draw_grid(a_canvas):
	# Draws the gridlines 50 pixels apart
	for row in range(50, 301, 50):
		a_canvas.create_line(-1, row, 251, row, fill = "lightblue")
	for column in range(50, 251, 50):
		a_canvas.create_line(column, -1, column, 301, fill = "lightblue")
		
def main(): 
	window = Tk()  
	window.title("Noddy's House")  
	window.config(background = 'white')   
	window.geometry("250x300+10+20") 

	a_canvas = Canvas(window) 
	a_canvas.config(background = "white")   
	a_canvas.pack(fill = BOTH, expand = True) #Canvas fills the whole top level window 
	draw_grid(a_canvas)
	draw_in_canvas(a_canvas) 
	window.mainloop()   
 
main()