'''
Worksheet 11 - Classes - SOLUTION - Problem 2

Purpose: Student class
Author: Dr Carolyn Hardy
Date: December 6, 2016
Filename: student.py
'''

class Student():
    ''' Student class to keep student records'''
    
    def __init__(self, first='unknown', last='unknown', major='unknown', gpa=0):
        self.first = first
        self.last = last
        self.major = major
        self.gpa = gpa
        
    def setFirstName(self, first):
        self.first = first
        
    def setLastName(self, last):
        self.last = last
        
    def setMajor(self, major):
        self.major = major
        
    def setGpa(self, gpa):
        self.gpa = gpa
        
    def getFirstName(self):
        return self.first

    def getLastName(self):
        return self.last
    
    def getMajor(self):
        return self.major
    
    def getGpa(self):
        return self.gpa
    
    def __str__(self):
        name = self.last + ', ' + self.first
        displayStr = '{:20s} {:15s} {:4.2f}'.format(name, self.major, float(self.gpa))
        return displayStr