######################################
#
# CS150 ASSIGNMENT 1
# Purpose: Calculating number of diagonals within a polygon
# 
# Author: Ahmad M. Osman
# Date: September 16, 2016
#
# Filename: mOsmanDiagonals.py
#
#####################################

#Printing program label
print("Determine Diagonals")
print("----------------------------")

#Getting user input for number of sides of a polygon
poly_sides = int(input("Enter number of sides of a polygon: "))

#Calculating number of diagonals of the entered polygon
poly_diagonals = (poly_sides * (poly_sides-3)) / 2

#Printing the number of sides and number of diagonals of the polygon
print("A %d sided polygon has %d diagonals" %(poly_sides, poly_diagonals))