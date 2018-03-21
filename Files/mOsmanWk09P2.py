################################################################
#
# CS 150 - Worksheet #09 --- Problem #2
# Purpose: Practicing how to read a file, store its content,
#		   and search the file's content after storing it
# 
# Author: Ahmad M. Osman
# Date: November 21, 2016
#
# Filename: mOsmanWk09P2.py
#
################################################################

#Reading presidents' file into a list and returning the list
def readPresidents(file):
	infile = open(file, "r")
	presidents = [president for president in infile]
	infile.close()
	return presidents

#main function - program execution instructions
def main():
	#Openning presidents' file and reading it into a list
	presidents = readPresidents("USPresidents.txt")
	
	#Displaying the presidents with the first name of "John"
	print("".join(presidentName for presidentName in presidents if presidentName.startswith("John")).rstrip())

#Calling main function for program execution
main()