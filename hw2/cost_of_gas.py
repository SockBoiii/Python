# Manases Garcia 
# Problem # 4 Homework # 2 
# cost_of_gas,py
# 9-10-2020
#
# This program calculates the total cost of gas 
#    purchase.

print('This program will calculte the total cost ' \
    + 'of gas purchased.')

price_of_gas = float(input('\nEnter the price of gas: '))
num_of_gallons = float(input('\nEnter total number of '
    + 'gallons desired: '))
total_cost = price_of_gas * num_of_gallons

print('\nThe total cost is $%.2f' % (total_cost))
