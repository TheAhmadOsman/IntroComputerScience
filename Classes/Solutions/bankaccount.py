'''
Worksheet 11 - Classes - SOLUTION - Problem 1

Purpose: BankAccount class
Author: Dr Carolyn Hardy
Date: December 6, 2016
Filename: bankaccount.py
'''

class BankAccount:
    '''The BankAccount class simulates a bank account'''
    
    def __init__(self, balance=0):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient funds')
    
    def getBalance(self):
        return self.balance
    
    def __str__(self):
        displayStr = '${:.2f}'.format(self.balance)
        return displayStr