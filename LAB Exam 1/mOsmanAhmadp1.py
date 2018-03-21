####################################
#	Author Name: Ahmad M. Osman
####################################

import turtle

def triangle(t):
	for i in range(3):
		t.forward(100)
		t.left(120)

def funShape(t):
	t.color("orange")
	for i in range(18):
		triangle(t)
		t.left(20)

def stampCenter(t):
	t.shape("turtle")
	t.color("blue")
	t.stamp()

def main():
	wn = turtle.Screen()
	t = turtle.Turtle()

	t.speed(10)
	t.pensize(3)
	t.hideturtle()
	funShape(t)
	stampCenter(t)

	wn.exitonclick()
	
main()