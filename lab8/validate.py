# Manases Garcia, Aidyn Vargas, Antonio FLores, Ashley Martinez Rodriguez
# CSCI 248 Lab 8 Problem 2 
# validate.py
# 9-24-2020
#
# This program validates a number with a range. 

def main():
    print('This program demonstrates the get_input function.\n')

    result = get_input()

    print('\nThe validated input was %.2f.' % result)

def get_input():
   num = float(input('Enter a number in [1, 5]: ')) 
   while num < 1 or num > 5: 
       print('\nThis is not in the range [1, 5]')
       num = float(input('Enter a number in [1, 5]: ')) 
   return num

main()
