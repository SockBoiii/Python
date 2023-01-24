# Manases Garcia
# CSCI 248 Homework#4 Problem#5
# increased_tuition.py
# 9-25-2020
#
# This program calculates increased tuition for next 10 years. 

print('Given the current cost of tuition and the project yearly rate')
print('increase (as a precentage), this program will print a table of')
print('projected tuition cost for the next 10 years.')

tuition = int(input('\nEnter the current tuition: '))
rate = float(input('Enter the rate increase in percent: '))
annual_rate = rate * .01

print('\nYear    Tuition')

for years in range(1, 11):
    tuition += tuition * annual_rate
    print('%2d      $%8.2f' % (years, tuition))

