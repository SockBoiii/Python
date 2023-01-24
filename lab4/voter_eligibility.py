# Manases Garcia and Klyde Jones

# CSCI 248 Lab #4 Problem #2
# voter_eligibility.py
# 9-8-2020
#
# the program determines voter eligibility and displays if the
#    voter is eligible.

print('This program determines your voter eligibility.\n')

age = int(input('Enter you age: '))

if age >= 18:
    status = input('\nAre you registered to vote? (Y/N) ')
    if status == 'Y' or status == 'y':
        print('\nYou can vote.')
    else:
        print('\nYou must register before you can vote.')
else:
    print('\nYou are too young to vote.')

