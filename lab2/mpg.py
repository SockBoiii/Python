# mpg.py

print('This program computes the miles per gallons used.\n')

miles = float(input('Enter the miles driven:'))
gallons = float(input('Enter gallons of gas used:'))
mpg = miles / gallons

print('\nUsing %.1f gallons over %.1f miles' \
    % (gallons, miles))
print('\nyou obtained %.1f miles per gallon.' %mpg)
