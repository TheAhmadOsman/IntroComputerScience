###########################################################
#
# CS150 ASSIGNMENT 3
# Purpose: Guessing game for users based on random
#		   number and control structures
# 
# Author: Ahmad M. Osman
# Date: November 2, 2016
#
# Filename: mOsmanGuessGame.py
#
###########################################################

import random

#main function - program execution instructions
def main():

	#Printing program label
	print("***** NUMBER GUESSING GAME *****")

	#Generating random number between 1 and 50 inclusive
	randomNumber = random.randint(1, 50)

	#Getting user input and initializing number of tries
	guessedNumber = int(input("Guess a number between 1 and 50: "))
	numberOfTries = 1

	#Loop based on the user's guessed number being not equal to the generated random number
	while(guessedNumber != randomNumber):
		#Conditional statement in case guessed number is higher than randomized number - User inputs another guess
		if(guessedNumber > randomNumber):
			guessedNumber = int(input("Too high - Try again: "))
			numberOfTries += 1
		#Conditional statement in case guessed number is lower than randomized number - User inputs another guess
		else:
			guessedNumber = int(input("Too low - Try again: "))
			numberOfTries += 1

	#Printing the number of tries
	if(numberOfTries == 1):
		print("You got it in 1 try.")
	else:
		print("You got it in %d tries." %(numberOfTries))

#Calling main function for program execution
main()