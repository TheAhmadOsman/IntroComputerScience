#################################
#	Author: Ahmad M. Osman
#################################

def readFile(file):
	infile = open(file, "r")
	list = infile.readlines()
	list = [int(number) for number in list]
	infile.close()
	return list

def mergeAndSort(list1, list2):
	list = list1 + list2
	list.sort()
	return list

def countMultiplesOf3(list):
	list = [number for number in list if number % 3 == 0]
	outfile = open("multiplesOf3.txt", "w")
	list = [(str(number)) + '\n' for number in list]
	outfile.writelines(list)
	outfile.close()
	return len(list)

def cubeOdds(list):
	list = [number for number in list if number % 2 != 0]
	outfile = open("cubeOdds.txt", "w")
	list = [(str(number)) + '\n' for number in list]
	outfile.writelines(list)
	outfile.close()
	return len(list)

def main():
	list1 = readFile("numbers1.txt")
	list2 = readFile("numbers2.txt")
	print("List 1:", list1)
	print("List 2:", list2)
	print()

	listMerged = mergeAndSort(list1, list2)
	print("Merged and Sorted:", listMerged)
	print()

	print("Merged list has %d numbers" %(len(listMerged)))
	multiplesOf3 = countMultiplesOf3(listMerged)
	print(multiplesOf3, "numbers were divisible by 3 and sent to a file")
	cubedOdds = cubeOdds(listMerged)
	print(cubedOdds, "numbers were odd and their cubes were sent to a file")

main()