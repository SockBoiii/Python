# Manases Garcia
# CSCI 248 Homework#7 #Problem2
# largest_factor.py
# 10-16-2020
#
# This program factors an integer and takes the largest factor from the integer

def main():
    print('This program demonstrates the largest_factor ' \
        + 'function.\n')

    print('The largest factor of 125 is %d.' \
        % largest_factor(125))
    print('The largest factor of 27 is %d.' \
        % largest_factor(27))
    print('The largest factor of 12 is %d.' \
        % largest_factor(12))
    print('The largest factor of 7 is %d.' \
        % largest_factor(7))

def largest_factor(num):
    """Returns largest factor of num that is less then num"""
    for i in range(num-1, 0, -1):
        if num % i == 0:
            return i
main()
