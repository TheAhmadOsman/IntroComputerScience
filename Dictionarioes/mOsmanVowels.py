#################################################################################
#
# CS 150 - Assignment #04 - Program 1
# Purpose: Capitalizing vowels of a string 
#          that was read from a file and 
#          saving it to another file.
#          File Input & Output Assignment Program.
#
# Author: Ahmad M. Osman
# Date: December 5, 2016
#
# Filename: mOsmanVowels.py
#
#################################################################################

#Reading file and storing its content to a string
def readfile(file):
    infile = open(file, 'r')
    message = infile.read()
    infile.close()
    return message

#Converting vowels in message to uppercase and saving converted message to a file
def convertAndWrite(message):
    #Initializing the vowels
    vowels = ('a', 'e', 'i', 'o', 'u')
    
    #Converting the vowels in message
    for ch in message:
        if ch in vowels:
            message = message.replace(ch, ch.capitalize())
    #Printing converted message
    print(message)

    #Saving converted message to a file
    outfile = open('vowelsUpper.txt', 'w')
    outfile.write(message)
    outfile.close()

#main function - program execution instructions
def main():
    
    #Getting user input on file name
    file = input('Enter file name: ')
    #Reading file's message
    message = readfile(file)

    #Printing new line
    print()
    
    #Printing the file's message
    print(message)
    
    #Printing new line
    print()

    #Converting vowels in message and saving them to another file
    convertAndWrite(message)

#Calling main function for program execution
main()