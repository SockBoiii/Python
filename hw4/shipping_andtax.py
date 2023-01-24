# Manases Garcia
# Homework #4 Problem #3
# shipping_andtax.py
# 9-23-2020
#
# This program prompts the user to enter a subtotal 
# and it will ask if the user is from Texas, then it will
# calculate shipping and sales tax. 

print('This program computes the total cost of a purchase.\n')
subtotal = float(input('Enter the subtotal: '))
tx_resident = input('Is the customer a Texas resident? (Y/N): ')

if tx_resident == 'Y' or tx_resident == 'y':
    sales_tax = subtotal * .0825 
else:
    sales_tax = 0

if subtotal < 100:
    shipping = 5.25
else:
    shipping = 0

total_cost = subtotal + sales_tax + shipping

print('\nSubtotal   $%6.2f' % subtotal)
print('Shipping   $%6.2f' % shipping)
print('Tax        $%6.2f' % sales_tax)
print('Total cost $%6.2f' % total_cost)

