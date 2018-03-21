###########################################################
#
# CS150 ASSIGNMENT 3
# Purpose: Salary options program to dertmine the best
#		   earning option for the next ten years
# 
# Author: Ahmad M. Osman
# Date: November 2, 2016
#
# Filename: mOsmanSalaryOption.py
#
###########################################################

#Salary option #1 function - Yearly salary of 20000 and yearly increase of 1000 - Ten years' earning calculated
def calcOption1():
	
	#Initializing salary, salary increase and first year's earning
	salary = 20000
	salaryIncrease = 1000
	earning = salary

	#Loop to calculate and sum the salary option's following 9 years earning
	for i in range(9):
		earning += salary + salaryIncrease
		salary += salaryIncrease

	return earning

#Salary option #2 function - Half-yearly salary of 10000 and half-yearly increase of 250 - Ten years' earning calculated
def calcOption2():

	#Initializing salary, salary increase and first half-year's earning
	salary = 10000
	salaryIncrease = 250
	earning = salary

	#Loop to calculate and sum the salary option's following 19 half-years earning
	for i in range(19):
		earning += salary + salaryIncrease
		salary += salaryIncrease

	return earning

#main function - program execution instructions - calling other functions
def main():

	#Calling the salary options' functions and assigning their earnings accordingly
	option1Earning = calcOption1()
	option2Earning = calcOption2()

	#Printing options' earnings
	print("Option 1 earns ${:,d}".format(option1Earning))
	print("Option 2 earns ${:,d}".format(option2Earning))

#Calling main function for program execution
main()