####################################
#	Author Name: Ahmad M. Osman
####################################

def calInterestEarned(principal, interestRate, time):
	interestEarned = principal * interestRate * time
	return interestEarned

def calCurrentBalance(principal, interestEarned):
	currentBalance = principal + interestEarned
	return currentBalance

def display(time, interestEarned, balance):
	print("In %d year you will earn $%.2f of interest for a balance of $%.2f" %(time, interestEarned, balance))

def main():
	principal = float(input("Enter principal: "))
	interestRate = float(input("Enter rate as decimal: "))
	time = int(input("Enter time as years: "))

	print()
	
	interestEarned = calInterestEarned(principal, interestRate, time)
	currentBalance = calCurrentBalance(principal, interestEarned)

	display(time, interestEarned, currentBalance)

main()