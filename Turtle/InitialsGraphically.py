######################################
#
# CS150 - Graphical Initials Homework
# Purpose: Drawing my initials (AMO) using turtle
# 
# Author: Ahmad M. Osman
# Date: September 23, 2016
#
# Filename: InitialsGraphically.py
#
#####################################

#Importing turtle module
import turtle

#Initiating window canvas
window = turtle.Screen()
window.bgcolor("black")

#Drawing A
A = turtle.Turtle()
A.setposition(-340,-250)
A.speed(0)
A.hideturtle()
A.pencolor("#009a22")

A.left(82)
A.forward(250)

A.left(-82)
A.forward(70)
A.left(180)
A.forward(70)

A.left(-98)
A.forward(250)

A.left(-164)
A.forward(500)

#Drawing M
M = turtle.Turtle()
M.setposition(-175, -250)
M.speed(0)
M.hideturtle()
M.pencolor("#009a22")

M.left(90)
M.forward(500)
M.right(150)
M.forward(250)
M.left(120)
M.forward(250)
M.left(-150)
M.forward(500)

#Drawing O
O = turtle.Turtle()
O.setposition(205, 0)
O.speed(0)
O.hideturtle()
O.pencolor("#009a22")

O.shape("circle")
O.shapesize(25.5, 11, 0)
O.stamp()


#Waiting 500 user to exit through clocking on the turtle program screen
window.exitonclick()