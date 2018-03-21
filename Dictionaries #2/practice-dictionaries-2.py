# read from a file to a list
def readFile(file):
	infile = open(file, 'r')
	list = infile.readlines()
	list = [item.strip().split() for item in list]
	infile.close()
	return list

#convert list to dictionary
def convertListToDict1(numList):
	numDictionary = {}
	for item in numList:
		#print(item)
		numDictionary[item[0]] = item[1]
	return numDictionary

#convert list to dictionry with key: tuple of values
def convertListToDict2(numList):
	numDictionary = {}
	for item in numList:
		#print(item)
		numDictionary[item[0]] = {'English' : item[1], 'Spanish' : item[2]}
	return numDictionary

def main():
	numList = readFile('numbers.txt')
	print(numList)

	numDictionary = convertListToDict1(numList)
	print(numDictionary)

	print()
	numList = readFile('numbersSpanish.txt')
	numDictionary2 = convertListToDict2(numList)
	print(numDictionary2)

	num = input('Enter number to convert:')
	print(num + ' in English: ' + numDictionary2[num]['English'])
	print(num + ' in Spanish: ' + numDictionary2[num]['Spanish'])

main()