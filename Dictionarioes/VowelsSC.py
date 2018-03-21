# ---------------------------------------------
# Purpose: capitalize vowels in a given message
# Author: Schuyler Cantrell
# Date: 12/5/2016
# Filename: VowelsSC.py
# ---------------------------------------------
def readfile(file):
    infile = open(file, 'r')
    message = infile.read()
    infile.close()
    return message

def convert(message):
    vowels = 'aeiou'
    for item in message:
        if item in vowels:
            new = item.capitalize()
    return new
    
def main():
    file = input('Enter file name: ')
    print()
    message0 = readfile(file)
    print(message0)
    print()
    message1 = convert(message0)
    print(message1)
    
main()