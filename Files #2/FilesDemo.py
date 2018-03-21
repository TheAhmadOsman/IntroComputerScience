import random

# for loop -- read each line as a string, then splits to a list
def readFile(file):
    infile = open(file, 'r')
    for line in infile:
        #print(line)
        student = line.rstrip().split(', ')
        print(student)
        print(student[1] + ' ' + student[0])
        print('------------------')
    infile.close()
    
# read() -- places entire contents of the file into a single string
def readFileUsingRead(file):
    infile = open(file, 'r')
    studentStr = infile.read()
    infile.close()
    return studentStr

# readline() -- read each line as a string
def readFileUsingReadline(file):
    infile = open(file, 'r')
    line = infile.readline()        # priming read
    while line:                     # while content of line is not empty
        print(line.rstrip())
        line = infile.readline()
    infile.close()
    
# readlines() -- reads each line as a str into a list -- including \n
def readFileToList(file):
    infile = open(file, 'r')
    studentList = infile.readlines()
    infile.close() 
    return studentList

# list comprehension -- reads into a list -- strip off \n
def readFileUsingListComprehension(file):
    infile = open(file, 'r')
    studentList = [line.rstrip() for line in infile]
    infile.close()
    return studentList


# create file using write()
def createFileUsingWrite(file):
    outfile = open(file, 'w')
    outfile.write("Sue Smith\n")
    outfile.write("John Jones\n")
    outfile.write("Brian Black\n")
    outfile.write('Joe Brown\n')
    outfile.close()

# create file using writelines() 
def createFileUsingWritelines(file):
    outfile = open(file, 'w')
    family = ['Grayson Hardy', 'Paige Hardy', 'Milo Hardy', 'Colton Hardy']
  
    # append endline character using list comprehension
    family = [name + '\n' for name in family]
    
    # write to file
    outfile.writelines(family)
    outfile.close()
    

# read, process, output    
def readAndWrite(fileIn, fileOut):
    infile = open(fileIn, 'r')
    outfile = open(fileOut, 'w') 
    
    line = infile.readline()
    while line:
        name = line.rstrip().split(', ')
        student = name[1] + ' ' + name[0]
        outfile.write(student + '\n')
        line = infile.readline()   
    infile.close()
    outfile.close()
    

# read, process, output using list comprehension    
def convertNames(fileIn, fileOut):
    infile = open(fileIn, 'r')
    outfile = open(fileOut, 'w') 
    
    studentList = [line.rstrip().split(', ') for line in infile]
    studentList = [name[1] + ' ' + name[0] + '\n' for name in studentList]
    outfile.writelines(studentList)
    
    infile.close()
    outfile.close()    

# add to existing file
def addToFile(file):
    outfile = open(file, 'a')
    outfile.write('Pat  Adams\n')
    newStudents = ['Bugs Bunny\n', 'Snow White\n', 'Mickey Mouse\n']
    outfile.writelines(newStudents)
    outfile.close()
    
# file of random numbers
def createFileOfNumbers(file):
    outfile = open('numbers.txt', 'w')
    for i in range(50):
        outfile.write(str(random.randint(1,100))+ '\n')
    outfile.close()

def main():
    file = 'CS150B_Fa16_students.txt'
    print(' ************ for Loop ************')
    readFile(file)
   
    print()
    print(' ************ read  -- reads as one long string ************')
    print(readFileUsingRead(file))

    print()
    print(' ************ readline ************')
    readFileUsingReadline(file)

    print()
    print(' ************ readlines ************')
    print(readFileToList(file))
    
    print()
    print(' ************ list comprehension ************')
    print(readFileUsingListComprehension(file))
    
    # write to files
    createFileUsingWrite('friends.txt')
    createFileUsingWritelines('family.txt')
    

    # read and write
    readAndWrite(file, 'students.txt')
    convertNames(file, 'students2.txt')
    
    # appending to end of existing file
    addToFile('students2.txt')
    
    createFileOfNumbers('numbers.txt')
    
main()
    
    
    