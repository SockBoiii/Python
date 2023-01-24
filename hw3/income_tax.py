# Manases Garcia
# Homework #3 Probelm #3
# income_tax.py
# 9-19-2020
#
# This program computes the income tax given the income in the state 
#    of Vermont. 

print('\nThis program computes the income tax in the state of Vermont.')

income =  float(input('\nEnter your income: '))

if income < 36250:
    income_tax = income * .0355
elif income < 87850:
    income_tax = 1286.88 + .068 * (income - 36250)
elif income < 182250:
    income_tax = 4795.68 + .078 * (income - 87850)
elif income < 398350:
    income_tax = 12236.88 + .088 * (income - 183250)
else:
   income_tax = 31165 + .0895 * (income - 398350)

print('\nFor an income of %9.2f, the tax payable will be %9.2f.' % (income, income_tax))
