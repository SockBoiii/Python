# Manases Garcia 
# CSCI 248 #2, Problem #3
# ticket_cost.py
# 9/3/2020
#
#This program computes the total cost for theater tickets.

CHILD_PRICE = 3
ADULT_PRICE = 5

print('Given the number of child and adult tickets desired,')
print('this program will compute the total cost of the tickets.\n')

num_children = int(input('Enter the number of children: '))
num_adults = int(input('Enter the number of adults: '))
cost = CHILD_PRICE * num_children + ADULT_PRICE * num_adults

print('\nFor %d children and %d adults, the cost is $%.2f'\
    % (num_children, num_adults, cost))
