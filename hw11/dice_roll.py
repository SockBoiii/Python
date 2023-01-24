# Manases Garcia 
# CSCI 248 Homework #11 Problem #1
# dice_roll.py
# 11-9-2020
#
# This program roll two die 1000 times, counting the number of times that a sum
# of 2, 3, or 12 occurred.

import dice

MAX_ROLLS = 1000

def main():

    print('This progarm rolls two die 1000 times, counting the number')
    print('of times 2, 3, or 12 occurred.\n')

    die1 = dice.Die()
    die2 = dice.Die()
    
    count = 0

    for i in range(1, MAX_ROLLS + 1):
        value1 = die1.roll()
        value2 = die2.roll()
        results = value1 + value2
        if results == 2:
            count += 1
        elif results == 3:
            count += 1
        elif results == 12:
            count += 1

    print('You rolled %d times, and the numbers 2, 3, and 12 occured'\
         ' %d times.\n' % (MAX_ROLLS, count))

main()
