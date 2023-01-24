# Manases Garcia
# CSCI 248 Homework#10 Problem#3
# computing_average.py
# 11-5-2020
#
# This program computes the average of a given list, line by line, by
# converting each line to a integer.

import sys

def main():

    if len(sys.argv) != 2:
        print('Usage: python computing_average.py filename')
        sys.exit(1)

    file_name = sys.argv[1]

    print('\nThis program computes the average number for %s\n' \
        % file_name)

    try:
        num_count = 0
        sum = 0
        in_file = open(file_name, 'r')


        for line in in_file:
            num_list = line.split()
            for item in num_list:
                num_count += 1
                sum += float(item)

        in_file.close

        results = sum / num_count
        print('The average of the %d values was %.1f' % (num_count, results))

    except IOError:
        print('Error: Could not open or read from the file %s.' % file_name) 

    except ValueError:
        print('Error: Could not convert %s to a number.' % item)
        in_file.close

main()
