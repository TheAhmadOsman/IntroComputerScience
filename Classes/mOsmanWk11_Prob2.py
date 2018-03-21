########################################################################
#
# CS 150 - Worksheet #11 --- Problem #2
# Purpose: Practicing User-Defined Classes.
# 
# Author: Ahmad M. Osman
# Date: December 9, 2016
#
# Filename: mOsmanWk11_Prob2.py
#
########################################################################

#Importing Student class
from student import Student

#Reading students file and storing its content to a list of objects of the class Student
def readStudents(file):
	infile = open(file, 'r')
	studentList = infile.readlines()
	studentList = [item.rstrip() for item in studentList]
	studentList = [item.split() for item in studentList]
	studentList = [Student(item[0], item[1], item[2], float(item[3])) for item in studentList]
	infile.close()
	return studentList

#Printing students' information
def printStudents(studentList):
	for item in studentList:
		print(item)

#Finding the highest GPA among the list of students
def findHighestGpa(studentList):
	highestGpa = max(item.getGpa() for item in studentList)
	for student in studentList:
		if student.getGpa() == highestGpa:
			return student			

#Writing and displaying the students who have GPA above 3.0
def writeToFile(studentList):
	outfile = open("topStudents.txt", "w")
	for student in studentList:
		if student.getGpa() >= 3.0:
			outfile.write(student.getFirstName())
			outfile.write(" ")
			outfile.write(student.getLastName())
			outfile.write(" ")
			outfile.write(student.getMajor())
			outfile.write(" ")
			outfile.write(str(round(student.getGpa(),2)))
			outfile.write("\n")
			print(student)
	outfile.close()

#main function - program execution instructions
def main():

	#Reading student information from text file to a list of objects of the class Student
	studentList = readStudents("studentData.txt")
	#Printing the students' informations
	printStudents(studentList)
	print()

	#Finding the student with the highest GPA
	print("Highest GPA:")
	highestGpa = findHighestGpa(studentList)
	print(highestGpa)
	print()
	
	#Saving the top students(above 3.0 GPA) to a file
	print("Sending to file:")
	writeToFile(studentList)
	print()
	
#Calling main function for program execution
main()