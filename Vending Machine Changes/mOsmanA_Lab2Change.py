######################################
#
# CS150 LAB 2
# Purpose: Calculating Change For Vending Machines & Its Coins' Distribution
# 
# Author: Ahmad M. Osman
# Date: September 21, 2016
#
# Filename: mOsmanA_Lab2Change.py
#
#####################################

#Getting User Input
money = float(input("Enter value of money inserted: "))
item_price = float(input("Enter item price: "))

#Calculating Change
change = money - item_price

#Getting Number Of Dollar Coins
dollar_coins = int(change)

#Calculating Pennies Left After Subtracting Dollar Coins
pennies_left = change - dollar_coins

#Getting Number Of Quarter Coins
quarters = pennies_left // 0.25

#Calculating Pennies Left After Subtracting Quarter Coins
pennies_left -= (quarters * 0.25)

#Getting Number Of Dime Coins
dimes = pennies_left // 0.10

#Calculating Pennies Left After Subtracting Dime Coins
pennies_left -= (dimes * 0.10)

#Getting Number Of Nickel Coins
nickels = pennies_left // 0.05

#Printing Change & Coins Distribution
print("Change: $%.2f" %change)
print("     %-15s %4d" %("Dollar coin(s):", dollar_coins))
print("     %-15s %4d" %("Quarter(s):", quarters))
print("     %-15s %4d" %("Dime(s):", dimes))
print("     %-15s %4d" %("Nickel(s):", nickels))