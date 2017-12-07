'''
Coder: Jacky Shew
Description: Duplicate pattern in a recursion manner based on levels(input)
'''

import turtle
import sys

def draw_shape(t, n, mover, position_list, level):
	position_list2 = []
	for i in range(4**level):
		t.goto(position_list[0])
		position_list.remove(position_list[0])
		for num in range(2):
			t.down()
			start = t.position()
			t.forward(mover)
			corner = t.position()
			t.setheading(180)
			t.forward(mover)
			position_list2.append(t.position())
			t.goto(corner)
			t.backward(mover)
			position_list2.append(t.position())
			t.up()
			t.goto(start)
			t.setheading(270)
		t.setheading(90)

	if n > 1: draw_shape(t, n-1, mover//2, position_list2, level+1)
	else: t.goto(0,0)
		
def q1():
	my_win = turtle.Screen()
	my_turtle = turtle.Turtle()
	my_turtle.speed(10000)
	my_turtle.left(90)
	n = int(input('Draw shape at level: '))
	if n < 1: sys.exit("Shape level must be higher than 0")
	draw_shape(my_turtle, n, 100, [(0.00,0.00)], 0)
	my_win.exitonclick()
	
q1()