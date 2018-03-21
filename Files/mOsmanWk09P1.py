################################################################
#
# CS 150 - Worksheet #09 --- Problem #1
# Purpose: Practicing how to read a file's content into a list,
#		   sort the list alphabetically, and write the sorted
#		   list to another file
# 
# Author: Ahmad M. Osman
# Date: November 21, 2016
#
# Filename: mOsmanWk09P1.py
#
################################################################

#Reading states' file into a list and returning the list
def readStates(file):
	infile = open(file, "r")
	states = [state.rstrip() for state in infile]
	infile.close() 
	return states

#Writing sorted alphabetical states into a file
def writeSortedStates(file, sortedStates):
	outfile = open(file, "w")
	states = [state + '\n' for state in sortedStates]
	outfile.writelines(states)
	outfile.close()

#main function - program execution instructions
def main():
	#Openning states' file and reading it into a list
	states = readStates("states.txt")
	
	#Sorting the states' list alphabetically
	states.sort()

	#Writing sorted states to a file
	writeSortedStates("statesAlpha.txt", states)

#Calling main function for program execution
main()