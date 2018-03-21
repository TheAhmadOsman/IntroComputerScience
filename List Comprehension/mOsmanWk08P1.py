################################################################
#
# CS 150 - Worksheet #08
# Purpose: Lists and List Comprehension practice
#		   Removing vowels through list
#		   comprehension program
# 
# Author: Ahmad M. Osman
# Date: November 7, 2016
#
# Filename: mOsmanWk08P1.py
#
################################################################

# using list comprehension to remove vowels
def removeVowels(sentence):
    vowels = 'aeiou'
    noVowels = [str(ch) for ch in sentence if ch not in vowels]
    return ''.join(noVowels)

#main function - program execution instructions
def main():

	#Getting user input
	sentence = str(input("Enter a sentence: "))

	#Calling and assinging removeVowels
	noVowelSentence = removeVowels(sentence)

	#Printing new sentence without vowels
	print(noVowelSentence)
	
#Calling main function for program execution
main()