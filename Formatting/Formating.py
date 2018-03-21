name = "Ahmad"
age = 20

#Old way 
print("Hello, %s!" %(name))
print("%s is %d years old" %(name, age))
print("----------------------------------------------------------")

#New way
print("Hello, {:s}!".format(name))
print("{:s} is {:d} years old.".format(name, age))
print("----------------------------------------------------------")


firstName = "john"
lastName = "Doe"
balance = 53.44

print("Hello, {:s} {:s}. Your current balance is ${:.2f}." .format(firstName, lastName, balance))
print("Hello, %s %s. Your current balance is $%.2f." %(firstName, lastName, balance))

print("----------------------------------------------------------")

test = "test"
num1 = 123
num2 = 123.456

# old way - default right justify
print('%10s' %test)
print('%10d' %num1)
print('%10.2f' %num2)
print('%10.2f' %num2)
print()
print('%-10s' %test)
print('%-10d' %num1)
print('%-10.2f' %num2)
print('%-10.2f' %num2)
print("----------------------------------------------------------")

# newer way
print('new way')
print('{:>10s}'.format("test:", test))
print('{:<10d}'.format(num1))
print('{:<10f}'.format(num2))
print('{:<10.2f}'.format(num2))
print("----------------------------------------------------------")

# ^ centers in field width
print()
print('1234567890')
print('{:^10s}'.format(test))

# comma seperator
num1 = 123456789012987
num2 = 123456.7890
print('{:,d}'.format(num1))
print('{:,.2f}'.format(num2))