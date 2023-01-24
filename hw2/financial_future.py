# Manases Garcia
# Problem #5 Homework #2
# financial_future.py
# 9-11-2020
#
# This program calculates the future value of an investment. 

print('\nThis program calculated the futur value of an investment.')

principal_amount = float(input('\nEnter inital amount invested: '))
interest_rate = float(input('\nEnter annual rate of return: '))
num_years = int(input('\nEnter number of years invested: '))

amount_accumlated = principal_amount * (1+(interest_rate / 100)) ** num_years

print('\nThis is the total amount accumlated $%7.2f.' % (amount_accumlated))
