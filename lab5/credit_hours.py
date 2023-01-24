# Manases Garcia, Aidyn Vargas, and Marcus Johnson
# CSCI 248 Lab #5, Problem #2
# credit_hours.py
# 9-10-2020
#
# This program determins a students class standing.

print("This program determines a student's class standing")
print('based on earned credit hours.\n')

num_hours = int(input('Enter credit hours: '))

if num_hours < 27:
    status = 'freshman'
elif num_hours < 60:
    status = 'sophomore'
elif num_hours < 90:
    status = 'junior'
else:
    status = 'senior'

print('\nA student with %d hours is a %s.' % (num_hours, status))
