def main():
	phonebook = {'Chris' : '555-1111', 'Katie' : '555-2222', 'Joanne' : '555-3333'}
	print(phonebook)

	#update method
	phonebook.update({'Chris' : '999-9999'})
	print(phonebook)
	myphonebook = {'Tonya' : '123-1234', 'Jeff' : '567-6789'}
	phonebook.update(myphonebook)
	print()
	print(phonebook)
	print(myphonebook)
	print()

	#find min and max keys if all keys are the same data type
	print(min(phonebook))
	print(max(phonebook))

	print()
	#find min and max values
	print(min(item for item in phonebook.values()))
	print(max(item for item in phonebook.values()))

	#find min and max key with values
	print()
	print(min(item for item in phonebook.items()))
	print(max(item for item in phonebook.items()))

	#popping
	print()
	print(phonebook)
	print(phonebook.pop('Katie'))

	print()
	print(phonebook.pop('Tonya', 'Entry not found'))
	print(phonebook)

	print()
	print(phonebook.pop('Amy', 'Amy not found'))
	print(phonebook)

	print()
	print(phonebook.popitem())
	print(phonebook)

main()