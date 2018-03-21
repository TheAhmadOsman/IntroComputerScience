########################################################################
#
# CS 150 - Worksheet #11 --- Problem #1
# Purpose: Practicing User-Defined Classes.
# 
# Author: Ahmad M. Osman
# Date: December 9, 2016
#
# Filename: mOsmanWk11_Prob1.py
#
########################################################################

#Importing BankAccount class
from bankaccount import BankAccount

#main function - program execution instructions
def main():

	#Getting user's beginning balance through input
	balance = float(input("Enter beginning balance: "))
	#Making an object of the BankAccount class with the balance as he beginning value
	account = BankAccount(balance)
	#Getting user's desired amount to deposit
	deposit = float(input("How much were you paid this week? "))
	#Depositing the user's desired amount from the bank account object
	account.deposit(deposit)
	#Printing account's balance
	print(account)
	print()

	#Getting user's desired amount to withdraw
	withdraw = float(input("How much would you like to withdraw? "))
	#Withdrawing the user's desired amount from the bank account object
	account.withdraw(withdraw)
	#Printing account's balance
	print(account)

#Calling main function for program execution
main()