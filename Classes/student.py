########################################################################
#
# CS 150 - Worksheet #11 --- Problem #2
# Purpose: Practicing User-Defined Classes.
# 
# Author: Ahmad M. Osman
# Date: December 9, 2016
#
# Filename: student.py
#
########################################################################

class Student:
	#Student Class

	#Creating a student object and initiating his or her values
	def __init__(self, first="unknown", last="unknown", major="unknown", gpa = 0.0):
		self.first = first
		self.last = last
		self.major = major
		self.gpa = gpa

	#Setting student's first name
	def setFirstName(self, first):
		self.first = first

	#Setting student's last name
	def setLastName(self, last):
		self.last = last

	#Setting student's major
	def setMajor(self, major):
		self.major = major

	#Setting student's GPA
	def setGpa(self, gpa):
		self.gpa = gpa

	#Getting user's first name
	def getFirstName(self):
		return self.first

	#Getting user's last name
	def getLastName(self):
		return self.last

	#Getting user's major
	def getMajor(self):
		return self.major

	#Getting user's GPA
	def getGpa(self):
		return self.gpa

	#Printing student's information
	def __str__(self):
		display = "%-25s" %(self.last + ', ' + self.first) + "%-25s" %(self.major) + "%-3.2f" %(self.gpa)
		return display