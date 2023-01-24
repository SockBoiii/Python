# Manases Garcia, Simon Carandang, William Cucinotta, Marcela Juarez
# CSCI 248 Lab#24
# awards.py
# 12-8-2020
#
# This program will prompt the user to enter a name and will look through a
# file to find if that person has one an academy award.  

def main():
    FILENAME = 'academy_awards-small.csv'

    print('Given a name, this program will determine if that person')
    print('has won the Academy Award for acting.\n')

    target_name = input('Enter the name: ')
    found = False  # Have not yet found the target in the file
    print()        # Separate input from resulting output
    
    try:
        in_file = open(FILENAME, 'r')

        for line in in_file:
            year_str, role, name = line.rstrip().split(',', 2)
            if target_name == name:
                found = True
                print('%s won for %s in %s.' % (name, role, year_str))
        if not found: 
            print('%s has never won the academy award for acting.' \
                % target_name)
        in_file.close() 

    except IOError: 
        print('Could not open %s for reading' % FILENAME)

main()


