# odd_digits.py

def main():
    print('This program tests the all_digits_odd function.\n')
    
    if all_digits_odd(7):
        print('Correct: The digits in 7 are all odd')
    else:
        print('ERROR: The digits in 7 are all odd, ' \
            + 'but the function returned False')

    if not all_digits_odd(2):
        print('Correct: The digit in 2 is not odd')
    else:
        print('ERROR: The digit in 2 is not odd, ' \
            + 'but the function returned True')

    if all_digits_odd(13957):
        print('Correct: The digits in 13957 are all odd')
    else:
        print('ERROR: The digits in 13957 are all odd, ' \
            + 'but the function returned False')

    if not all_digits_odd(7136):
        print('Correct: Some digit in 7136 is not odd.')
    else:
        print('ERROR: Some digit in 7136 is not odd, but ' \
            + 'the function returned True.')

    if not all_digits_odd(69513):
        print('Correct: Some digit in 69513 is not odd.')
    else:
        print('ERROR: Some digit in 69513 is not odd, but ' \
            + 'the function returned True.')

    if not all_digits_odd(12345):
        print('Correct: Some digits in 12345 are not odd.')
    else:
        print('ERROR: Some digits in 12345 are not odd, but ' \
            + 'the function returned True.')

    if not all_digits_odd(2468):
        print('Correct: The digits in 2468 are not odd.')
    else:
        print('ERROR: The digits in 2468 are not odd, but ' \
            + 'the function returned True.')

    # This testing will catch a subtle error that some students make
    if all_digits_odd(25) == None:
        print('ERROR: all_digits_odd failed to return a value for 25')
    elif all_digits_odd(25) == False:
        print('Correct: The digits in 25 are not all odd.')
    else:
        print('ERROR: The function returned True for 25')

    # This testing will catch a subtle error that some students make
    if all_digits_odd(15) == None:
        print('ERROR: all_digits_odd failed to return a value for 15')
    elif all_digits_odd(15) == False:
        print('ERROR: The function returned False for 15')
    else:
        print('Correct: The digits in 15 are all odd')

def all_digits_odd(num):
    count = 0
    while num % 1 == 0:
        digit = num % 10
        count += digit
        return count == True
        if num % 2 == 0:
            return count == False 

main()
