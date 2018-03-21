###########################################################
#
# CS150 ASSIGNMENT 2
# Purpose: Calculating the area and perimeter
#		   of a rectangle through
#		   user-defined functions
# 
# Author: Ahmad M. Osman
# Date: October 3, 2016
#
# Filename: mOsmanRectangle.py
#
##########################################################

#Calculate Area function - Parameters of Length & Width
def calRecArea(recLength, recWidth):
	recArea = recLength * recWidth
	return recArea

#Calculate Perimeter function - Parameters of Length & Width
def calRecPeri(recLength, recWidth):
	recPeri = (recLength + recWidth) * 2
	return recPeri

#Display Calculated Area & Perimeter function - Parameters of Area & Perimeter
def disRecCal(recArea, recPeri):
	print("Area:", recArea)
	print("Perimeter:", recPeri)

#Main function - Getting user input & calling user-defined functions
def main():
	#Getting user input
	length = int(input("Enter length of rectangle: "))
	width = int(input("Enter width of rectangle: "))

	#Printing empty line
	print()

	#Calling calculations' functions
	area = calRecArea(length, width)
	perimeter = calRecPeri(length, width)
	
	#Displaying results through user-defined function
	disRecCal(area, perimeter)

#Calling main function for program execution
main()