################################################################
#
# CS 150 - Worksheet #08
# Purpose: Lists and List Comprehension practice
#		   Random list generating, sorting
#		   squaring and cubing through
#		   comprehension lists program
# 
# Author: Ahmad M. Osman
# Date: November 7, 2016
#
# Filename: mOsmanWk08P2.py
#
################################################################

import random

#main function - program execution instructions
def main():

	#Generating and assigning a random list of 10 values between 1 and 10 inclusive
	randomList = [random.randint(1, 10) for num in range(1, 11)]
	#Printing the random list
	print("Original list:", randomList)
	#Sorting the random list
	randomList.sort()
	#Pritning the sorted list
	print("Sorted list:", randomList)

	print()

	#Squaring the even numbers of the list
	squaredEvens = [pow(evenNumber, 2) for evenNumber in randomList if evenNumber % 2 == 0]
	#Printing squared even numbers
	print("Square of evens:", squaredEvens)
	#Cubing the odd numbers of the list
	cubedOdds = [pow(oddNumber, 3) for oddNumber in randomList if oddNumber % 2 == 1]
	#Printing the cubed odd numbers
	print("Cube of odds:", cubedOdds)
	
#Calling main function for program execution
main()