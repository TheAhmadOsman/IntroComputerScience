######################################
#
# CS150 - Interactive Python; Python Turtle Graphics Section, Exercise Chapter - Exercise 10
# Purpose: Drawing a clock with turtles
# 
# Author: Ahmad M. Osman
# Date: September 22, 2016
#
# Filename: ex10.py
#
#####################################

#Importing turtle module
import turtle

#Initiating window canvas
window = turtle.Screen()
window.bgcolor("lightgreen")

#Initiating clock turtle
clock = turtle.Turtle()
clock.shape("turtle")
clock.color("blue")
clock.hideturtle()
clock.speed(0)
clock.pensize(5)
clock.pu()
clock.setposition(0, 0)
clock.stamp()

#Drawing clock
for i in range(12):
	clock.left(30)
	clock.forward(125)
	clock.pd()
	clock.forward(10)
	clock.pu()
	clock.forward(25)
	clock.stamp()
	clock.forward(-160)

#Waiting for user to exit through clocking on the turtle program screen
window.exitonclick()