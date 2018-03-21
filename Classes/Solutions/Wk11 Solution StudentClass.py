import student

'''
Worksheet 11 - Classes - SOLUTION - Problem 2

Purpose: Read students from a file, create a list of student objects 
Author: Dr Carolyn Hardy
Date: December 6, 2016
Filename: Wk11 Solution StudentClass.py
'''

# read from file into a list of student objects
def readStudents(file):
    infile = open(file, 'r')
    studentList = []   
    for line in infile:
        studentRec = line.split()
        studentObj = student.Student(studentRec[0], studentRec[1], studentRec[2], float(studentRec[3]))
        studentList.append(studentObj)   
    #studentList.sort(key = lambda x: x.last)
    infile.close()
    return studentList

def printStudents(studentList):
    for student in studentList:
        print(student)
        
def findHighestGpa(studentList):
    high = 0
    for student in studentList:
        if student.getGpa() > high:
            high = student.getGpa()
            highStudent = student
    return highStudent

def writeToFile(studentList):
    outfile = open('topStudents.txt', 'w')
    for student in studentList:
        if student.getGpa() >= 3.0:
            print(student)
            line = student.getFirstName() + ' ' + student.getLastName() + ' ' + student.getMajor() + ' ' + str(student.getGpa()) + '\n'
            outfile.write(line)
    outfile.close()       
    
def main():
    studentList = readStudents('studentData.txt')
    printStudents(studentList)
    print()
    print('Highest GPA:')
    print(findHighestGpa(studentList))
    print()
    print('Sending to file:')
    writeToFile(studentList)  
    
main()