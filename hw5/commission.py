# Manases Garcia 
# CSCI 248 Homework#5 Problem#3
# commission.py
# 10-2-2020
#
# This program prompts the user for the value of a stock, validates that
# that the value is positive the prints corresponding commission.

def main():
    print('This program prompts the user to input the value of a stock, ')
    print('and validates that it is positive, then prints the corresponding ' \
    + 'commission.\n')

    stock_value = float(input('Enter the value of the stock: '))

    while stock_value <= 0:
        print('\nThis value is not positve.')
        stock_value = float(input('\nEnter the value of the stock: '))
    
    if stock_value > 0:
        commission = compute_commission(stock_value)
        
    print('\nThe commission earned is %6.2f.' % commission)


def compute_commission(value):
    if value < 100:
        commission = 20
    elif value < 1000:
        commission = 20 + (.01 * (value - 100))
    elif value < 1000:
        commission = 30 + (.005 * (value - 1000))
    else:
        commission = 75 + (.0025 * (value - 10000))
    return commission

main()
