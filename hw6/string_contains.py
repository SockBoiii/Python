# Manases Garcia
# CSCI 248 Homework #6 Problem#1
# string_contains.py
# 10-8-2020
#
# This program tells the user to give a sting, and a character, then 
# say is if the string contains the given character. 

def main():
    print('Given a string and a character, this program will')
    print('tell you if the string contains the character.\n')

    string = input('Enter the string: ')
    char = input('Enter the character: ')

    if contains(string, char):
        print('\nThe string contains the character.')
    else:
        print('\nThe string does not contain the character.')

def contains(string, desired_char):
    """Return whether or not desired_char is in string."""
    found = False
    for char in string:
        if char == desired_char:
            found = True
    return found

main()
