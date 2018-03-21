######################################
#
# CS150 LAB 1
# Purpose: Calculating Payroll
# 
# Author: Ahmad M. Osman
# Date: September 9, 2016
#
# Filename: mOsmanPayroll.py
#
#####################################

#Getting user input for different variable factors and making sure they're in the right variable types
#str input conversion isn't required yet being used to aid in coding style convention readability
emp_name = str(input("Enter employee's name: "))
hrs_worked = float(input("Enter number of hours worked in a week: "))
hr_pay_rate = float(input("Enter hourly pay rate: "))
fed_tax = float(input("Enter federal tax withholding rate: "))
state_tax = float(input("Enter state tax withholding rate: "))

#Assigned tax rates for both Medicare Tax and Social Security Tax
med_tax = 0.0145
soc_sec_tax = 0.062

#Calculating gross pay
gross_pay = hrs_worked * hr_pay_rate

#Calculating tax deductions
fed_ded = gross_pay * fed_tax
state_ded = gross_pay * state_tax
med_ded = gross_pay * med_tax
soc_sec_ded = gross_pay * soc_sec_tax

#Calculating total deduction
total_ded = fed_ded + state_ded + med_ded + soc_sec_ded

#Calculating net pay
net_pay = gross_pay - total_ded

#Printing output starting with an empty line; the employee input; the gross pay; the deductions; and the net pay
#Float formatting is used for decimals' precision
print("")
print("Employee Name: %s" % emp_name)
print("Hours Worked: %.1f" % hrs_worked)
print("Pay Rate: $%.2f" % hr_pay_rate)
print("Gross Pay: $%.2f" %gross_pay)
print("Deductions:")
print("   Federal: $%.2f" % fed_ded)
print("   State: $%.2f" % state_ded)
print("   Medicare: $%.2f" %med_ded)
print("   Social security: $%.2f" % soc_sec_ded)
print("   Total Deductions: $%.2f" % total_ded)
print("Net Pay: $%.2f" % net_pay)