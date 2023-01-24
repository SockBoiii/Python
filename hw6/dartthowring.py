# Manases Garcia
# CSCI 248 Homework#6 Problem#3
# dartthrowing.py
# 10-10-2020
# 
# This program simulates a large number of darts being thrown at a 
# dart borderm, and then it will tell you how many hit on the board. 

import math
import random

def main():
    print('\nThis program simulates a large number of darts being thrown at a')
    print('dart board, then tells you pi and the approximation.')
    count = 0 
    num_trials = int(input('\nEnter the number of dart to be thrown: '))

    for i in range(num_trials):
        x, y = throw_dart()
        if in_circle(x, y):
            count += 1
    apporximation_of_pie = 4 * (count / num_trials)
    print('\n%7.5f of pi and approximation of %7.5f.' \
    % (math.pi, apporximation_of_pie))

def throw_dart():
    """Return the ramdanly generted values of x and y ranging from [-1. 1)"""
    x = random.uniform(-1, 2)
    y = random.uniform(-1, 2) 
    return x, y

def in_circle(x, y): 
    """Return whether or not (x, y) is in the unit circle."""
    distance = math.sqrt((x * x) + (y * y))
    return (distance < 1) 

main()

