# Manases Garcia
# Homework #3 Problem #4
# count_chars.py
# 9-19-2020
#
# This program counts searched characters in a string. 

print('Given a string and a character, this program will count')
print('the number of times the character appears in the string.\n')

string = input('Enter a string: ')
search_char = input('Enter a single character: ')

count = 0
for char in string:
    if char == search_char:
        count += 1

print('\nThere were %d occurrences of %s in the string.' \
    % (count, search_char))
