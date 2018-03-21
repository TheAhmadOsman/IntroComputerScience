################################################################
#
# CS 150 - Worksheet #07
# Purpose: Generating random rainfall values for the year's 12
#		   month and storing them in a list where a variety of
#		   calculations are proceeded on - Practicing Lists
# 
# Author: Ahmad M. Osman
# Date: November 4, 2016
#
# Filename: mOsmanWkst07.py
#
################################################################

import random

#main function - program execution instructions
def main():

	#Generating and assigning a random list of 12 values between 0 and 50 inclusive
	rainfall = random.sample(range(0,51), 12)

	#Calculating total rainfall
	totalRainfall = sum(rainfall)
	#Calculating average rainfall
	avgRainfall = totalRainfall / len(rainfall)
	#Calculating maximum rainfall
	maxRainfall = max(rainfall)
	#Calculating minimum rainfall
	minRainfall = min(rainfall)

	#Printing the rainfall randomly generated list and its calculations
	print("Monthly rainfall in inches")
	print(" ".join(repr(i) for i in rainfall))
	print()
	print("Total rainfall for the year: %d inches" %(totalRainfall))
	print("Average monthly rainfall:", round(avgRainfall, 2))
	#Count function is used to find how many occurances of the same max and min rainfall values occured a year
	print(rainfall.count(minRainfall), "month(s) had a low monthly rainfall of %d inches" %(minRainfall))
	print(rainfall.count(maxRainfall), "month(s) had a high monthly rainfall of %d inches" %(maxRainfall))
	
#Calling main function for program execution
main()