# Manases Garcia
# CSCi 248 Homework #4 Problem #4
# kph_to_mph.py
# 9-25-2020
#
# This program prints a table of speeds in kph to mph.

KPH = 1.60935

print('    This program prints a table of speeds in')
print('\nkilometers per hour (KPH) and miles per hour (MPH).')

print('\nKPH    MPH')
print('---    ---')

for kph in range(30, 131, 5):
    mph = kph / KPH
    print('%3d    %4.1f' % (kph, mph))
