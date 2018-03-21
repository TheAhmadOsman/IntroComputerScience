########################################################################
#
# CS 150 - Worksheet #11 --- Problem #1
# Purpose: Practicing User-Defined Classes.
# 
# Author: Ahmad M. Osman
# Date: December 9, 2016
#
# Filename: bankaccount.py
#
########################################################################

class BankAccount:
	#Bank Account Class

	#Creating account and initiating balance value
	def __init__(self, balance=0):
		self.balance = balance

	#Returning the account's current balance value
	def getBalance(self):
		return self.balance

	#Setting the account's balance to the value of amount
	def setBalance(self, amount):
		self.balance = amount

	#Depositing the value of amount into the account's balance
	def deposit(self, amount):
		print("$%.2f will be deposited." %(amount))
		self.balance += amount

	#Withdrawing the value of amount from the account if the balance is sufficient
	def withdraw(self, amount):
		if self.balance >= amount:
			print("$%.2f will be withdrawn." %(amount))
			self.balance -= amount
		else:
			print("Insufficient funds")

	#Printing account balance
	def __str__(self):
		display = "Account Balance: " + ("$%.2f" %(self.balance))
		return display