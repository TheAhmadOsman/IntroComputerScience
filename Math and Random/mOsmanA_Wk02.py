######################################
#
# CS 150 - Worksheet #02
# Purpose: Practicing Math and Random Modules - Revising Previous Concepts and Functions
# 
# Author Ahmad M. Osman
# Date: September 28, 2016
#
# Filename: mOsmanA_Wk02.py
#
#####################################

#Importing modules
import math
import random

#Questions 1-3 - Revising round() and pow() through printing statements
print("Solutions for 1 - 3")
print(round(62.583, 2))
print(round(12345.6789, 3))
print(pow(25, 4))
print()

#Questions 4-9 - Using the Math Module Functions through printing statements - Revising type conversion
print("Solutions for 4 - 9")
print(math.sqrt(144))
print(math.pow(25, 3))
print(math.ceil(62.3))
print(math.floor(36.9))
print(math.pi)
print(math.trunc(145.975))
print(int(145.975))
print()

#Question 10 - Printing 5 random values between 0 and 1 rounded(formatted) to 5 decimals - 'i' is used as the loop index variable name
print("Solution for 10")
for i in range(5):
	print("%.5f" %random.random())
print()

#Question 11 - Using randint() to print 10 random integers between 15 and 50 - 'i' is used as the loop index variable name
print("Solution for 11")
for i in range(10):
	print(random.randint(15, 50), end=" ")
print()
print()

#Question 12 - Using randrange() to print 10 random integers between 15 and 50 - 'i' is used as the loop index variable name
print("Solution for 12")
for i in range(10):
	print(random.randrange(15, 51), end=" ")
print()
print()

#Questions 13-15 - Applying Random Module Functions on a list of defined even numbers called 'numbers'
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print("Solutions for 13 - 15")
print(random.choice(numbers))
print(random.sample(numbers, 3))
print("Original list:", numbers)
random.shuffle(numbers)
print("Shuffled list:", numbers)