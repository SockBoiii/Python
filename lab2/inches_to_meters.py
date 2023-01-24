# Manases Garcia
#CSCI 248 Lab #2, Problem #2
#inches_to_meters.py

INCHES_PER_METER = 39.37

print('Given a value in inches, this program will compute the')
print('corresponding value in meters.\n')

inches = float(input('Enter the value in inches: '))
meters = inches / INCHES_PER_METER

print('\n%.2f inches = %.2f meters' % (inches, meters))
