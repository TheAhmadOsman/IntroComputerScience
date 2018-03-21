################################################################
#
# CS 150 - Worksheet #08
# Purpose: Lists and List Comprehension practice
#		   CS150 Grade Calculator Program
# 
# Author: Ahmad M. Osman
# Date: November 7, 2016
#
# Filename: mOsmanWk08P3.py
#
################################################################

#main function - program execution instructions
def main():

	#Getting user's scores for different categories
	assignScores = [float(score) for score in input("Assignment scores (separated by a space): ").split()]
	quizScores = [float(score) for score in input("Quiz scores: ").split()]
	writtenExScores = [float(score) for score in input("Written exam scores: ").split()]
	labExScores = [float(score) for score in input("Lab exam scores: ").split()]
	finalEx = float(input("Final exam score (enter -1 if not taken yet): "))

	#Calculating the average of each category
	assignAvg = sum(assignScores) / len(assignScores)
	quizAvg = sum(quizScores) / len(quizScores)
	writtenExAvg = sum(writtenExScores) / len(writtenExScores)
	labExAvg = sum(labExScores) / len(labExScores)

	#Checking if to calculate the grade with the user taking the final exam into account or not
	if(finalEx == -1):
		grade = (assignAvg * 0.25 + quizAvg * 0.15 + writtenExAvg * 0.20 + labExAvg * 0.20) / 0.80
	else:
		grade = assignAvg * 0.25 + quizAvg * 0.15 + writtenExAvg * 0.20 + labExAvg * 0.20 + finalEx * 0.20

	#Determining the grade letter
	if(grade >= 93):
		letterGrade = 'A'
	elif(grade >= 90):
		letterGrade = 'A-'
	elif(grade >= 87):
		letterGrade = 'B+'
	elif(grade >= 83):
		letterGrade = 'B'
	elif(grade >= 80):
		letterGrade = 'B-'
	elif(grade >= 77):
		letterGrade = 'C+'	
	elif(grade >= 73):
		letterGrade = 'C'
	elif(grade >= 70):
		letterGrade = 'C-'
	elif(grade >= 67):
		letterGrade = 'D+'
	elif(grade >= 60):
		letterGrade = 'D'
	else:
		letterGrade = 'F'

	print()

	#Printing the overall grade and letter grade
	print("Overall grade:", round(grade, 2))
	print("Letter grade:", letterGrade)

#Calling main function for program execution
main()