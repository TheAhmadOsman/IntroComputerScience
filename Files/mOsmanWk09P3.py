########################################################################
#
# CS 150 - Worksheet #09 --- Problem #3
# Purpose: Practicing how to read a file's content, use the content of
#		   the file for different calculations and processes, store
#		   some of the results of the processes and the
#		   calculations to other files, and display
#		   some of the results on screen
# 
# Author: Ahmad M. Osman
# Date: November 21, 2016
#
# Filename: mOsmanWk09P3.py
#
########################################################################

#Reading numbers' file into an integer list and returning the list
def readNumbers(file):
	infile = open(file, "r")
	numbers = [int(number.rstrip()) for number in infile]
	infile.close() 
	return numbers

#Writing numbers' list to a file - Arguments specify file name and list numbers
def writeNumbers(file, numbers):
	outfile = open(file, "w")
	nums = [str(number) + '\n' for number in numbers]
	outfile.writelines(nums)
	outfile.close()

#Displaying the list's numbers and its length
def displayNumbers(numbers):
	print(numbers, "\n")
	print("File contains %d numbers." %(len(numbers)))

#Displaying, and storing into a file, all the even numbers of a list
def evenNumbers(numbers):
	nums = [number for number in numbers if number % 2 == 0]
	nums.sort()
	print("%d of the numbers are even" %(len(nums)))
	writeNumbers("events.txt", nums)

#Displaying, and storing into a file, all the odd numbers of a list
def oddNumbers(numbers):
	nums = [number for number in numbers if number % 2 != 0]
	nums.sort()
	print("%d of the numbers are odd" %(len(nums)))
	writeNumbers("odds.txt", nums)

#Displaying some calculations based on the numbers' list
def numbersCalculations(numbers):
	print("Largest number:", max(numbers))
	print("Smallest number:", min(numbers))
	print("Sum of numbers:", sum(numbers))
	print("Average of numbers:", (sum(numbers)/len(numbers)))
	print("Last number:", numbers[-1])

#main function - program execution instructions
def main():
	#Openning numbers' file and reading it into a list of integers
	numbers = readNumbers("nums.txt")

	#Displaying list's numbers and the number of numbers in the list
	displayNumbers(numbers)
	
	#Displaying, and storing into a file, all the even numbers
	evenNumbers(numbers)

	#Displaying, and storing into a file, all the odd numbers
	oddNumbers(numbers)

	#Displaying different results and calculations based on the list's numbers
	numbersCalculations(numbers)

#Calling main function for program execution
main()