import bankaccount

'''
Worksheet 11 - Classes - SOLUTION - Problem 1

Purpose: Create bank account object, deposit, withdraw, show balance
Author: Dr Carolyn Hardy
Date: December 6, 2016
Filename: Wk11 Solution BankAccount.py
'''

def main():
    # Get beginning balance
    begBalance = float(input('Enter beginning balance: '))

    # Create a BankAccount object
    account = bankaccount.BankAccount(begBalance)
    
    # Deposit
    pay = float(input('How much were you paid this week? '))
    print('${:.2f} will be deposited.'.format(pay))
    account.deposit(pay)
    
    # Display balance
    print('Account Balance:', account)
    print()
    
    # Withdraw
    cash = float(input('How much would you like to withdraw? '))
    if cash <= account.getBalance():
        print('${:.2f} will be withdrawn.'.format(cash))
    account.withdraw(cash)
    
    # Display balance
    print('Account Balance: ', account)
    
main()
        
    