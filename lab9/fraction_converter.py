# Manases Garcia, Jackson Montgomery, Klyde Jones
# CSCi 248 Lab#9 Problem #1
# fraction_converter.py
# 9-29-2020
#
# This program converts a fraction into a decimal

def main():
    print('This program tests the fraction_to_decimal function.\n')
    print('It actually does more testing than necessary, just because....\n')

    print('fraction_to_decimal(3, 4) should return 0.75.')
    print('fraction_to_decimal(3, 4) returns %.2f.\n' \
        % fraction_to_decimal(3, 4))

    print('fraction_to_decimal(-12.5, 4) should return -3.125.')
    print('fraction_to_decimal(-12.5, 4) returns %.3f.\n' \
        % fraction_to_decimal(-12.5, 4))

    print('fraction_to_decimal(8, -3.2) should return -2.50.')
    print('fraction_to_decimal(8, -3.2) returns %.2f.\n' \
        % fraction_to_decimal(8, -3.2))

    print('fraction_to_decimal(2.5) should return 2.5.')
    print('fraction_to_decimal(2.5) returns %.1f.\n' \
        % fraction_to_decimal(2.5))

    print('fraction_to_decimal(5) should return 5.0.')
    print('fraction_to_decimal(5) returns %.1f.' \
        % fraction_to_decimal(5))

def fraction_to_decimal(numerator, denominator=1):
    return numerator / denominator

main()

