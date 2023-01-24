# Manases Garcia
# CSCI 248 Homework#12 Problem#2
# find_birthdays.py
#
# This program opens a file and finds the names of all people listed in given
# years inputed


import sys

def main():
    FILENAME = 'birthdays.csv'

    if len(sys.argv) != 3:
        print('python find_birthdays.py year1 year2')
        sys.exit(1)

    year1 = int(sys.argv[1])
    year2 = int(sys.argv[2])

    print('This program will print the names of all the people')
    print('listed in %s born from %d to %d.\n' \
        % (FILENAME, year1, year2))
    try:
        in_file = open(FILENAME, 'r')

        for line in in_file:
            name, month, day, string_year = line.strip().split(',', 3)
            year = int(string_year)
            if year1 <= year <= year2:
                print('%-22s %s %s, %d' % (name, month, day, year))
        in_file.close

    except IOError:
        print('Could not open %s for reading' % FILENAME)

    except ValueError:
        print('Could not convert year')
        in_file.close


main()
