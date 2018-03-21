######################################
#
# CS 150 - Worksheet #03
# Purpose: Practicing User-Defined Functions
# 
# Author Ahmad M. Osman
# Date: September 30, 2016
#
# Filename: mOsmanA_Wk03.py
#
#####################################

#First name input function
def getFirstName():
	firstName = str(input("Enter first name: "))
	return firstName

#Last name input function
def getLastName():
	lastName = str(input("Enter last name: "))
	return lastName

#Current salary input function
def getCurrentSalary():
	currentSalary = int(input("Enter current salary: "))
	return currentSalary

#New salary calculating function
def calculateNewSalary(salary):
	newSalary = salary * 1.05
	return newSalary

#Results displaying function
def displayResults(first, last, results):
	print("New salary for {0:} {1:}: ${2:,.2f}".format(first, last, results))

#Main function - Calling all other functions
def main():
	fName = getFirstName()
	lName = getLastName()
	cSalary = getCurrentSalary()
	nSalary = calculateNewSalary(cSalary)
	displayResults(fName, lName, nSalary)

#Calling main function for program execution
main()