# Manases Garcia, Hailey Stahl, Marcus Johnson
# CSCI 248 Lab#15 Problem#1
# username.py
# 10-27-2020
#
# This program prompts the user to give you first name and last name, and will 
# return a corresponding username given in lowercase letters. 

def main():
    print('Given your first and last names, this program')
    print('will determine your corresponding username.\n')

    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')

    user_name = get_username(first_name, last_name)

    print('\nFor the name %s %s, the username is %s.' \
        % (first_name, last_name, user_name.lower()))

def get_username(first, last):
    """Return the corresponding username."""
    combined = first+ last
    username = first[0] + last[:8]
    return username

main()
