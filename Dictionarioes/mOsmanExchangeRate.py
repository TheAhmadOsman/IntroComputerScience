#################################################################################
#
# CS 150 - Assignment #04 - Program 2
# Purpose: Reading a file's content into a list and converting
#          this list into a dictioanry and filtering this
#          dictionary based on user's input.
#          File Input & Output Assignment Program.
#
# Author: Ahmad M. Osman
# Date: December 5, 2016
#
# Filename: mOsmanExchangeRate.py
#
#################################################################################

#Reading exchange rates file and storing its content to a list
def readfile(file):
	infile = open(file, 'r')
	countries = infile.readlines()
	countries = [item.rstrip() for item in countries]
	countries = [item.split(',') for item in countries]
	infile.close()
	return countries

#Converting list into a dictionary with the Key being the country's name
def convertListToDict(list):
	dictionary = {}
	for item in list:
		dictionary[item[0]] = (item[1], item[2])
	return dictionary

#main function - program execution instructions
def main():

	#Reading countries' exchange rates into a list
	countriesList = readfile("exchangeRate.txt")
	#Converting countries' exchange rates list to a dictionary
	countriesDictionary = convertListToDict(countriesList)

	#Getting user input on which country to filter and give the currency information about
	country = str(input("Enter the name of a country: "))
	print()

	#Checking whether the country is in the dictionary or not and based on that giving output
	if country in countriesDictionary:
		print("Country:", country)
		print("Currency:", countriesDictionary[country][0])
		print("Exchange rate:", countriesDictionary[country][1])
	else:
		print(country, "not found")

#Calling main function for program execution
main()