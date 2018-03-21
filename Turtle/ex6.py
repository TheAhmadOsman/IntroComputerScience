######################################
#
# CS150 - Interactive Python; Python Turtle Graphics Section, Exercise Chapter - Exercise 6
# Purpose: Drawing a polygon from user's input
# 
# Author: Ahmad M. Osman
# Date: September 22, 2016
#
# Filename: ex6.py
#
#####################################

#Importing turtle module
import turtle

#Initiating window canvas
window = turtle.Screen()
window.bgcolor("lightgreen")

#Getting user input
sides = int(input("Enter polygon number of sides: "))
length = float(input("Enter side length: "))
pen_color = str(input("Enter polygon drawing color: "))
fill_color = str(input("Enter polygon fill color: "))

#Calculating the polygon's angle
angle = 360 / sides

#Initiating polygon turtyle
poly = turtle.Turtle()
poly.setposition(0, 0)
poly.color(pen_color, fill_color)
poly.pensize(4)
poly.speed(0)

#Begin filling polygon
poly.begin_fill()

#Drawing polygon
for i in range(sides):
	poly.forward(length)
	poly.left(angle)

#End filling polygon
poly.end_fill()

#Waiting for user to exit through clocking on the turtle program screen
window.exitonclick()