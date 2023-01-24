# Manases Garcia    
# CSCI 248 Homework#7 Problem#3
# file_max.py
# 10-16-2020
#
# This program computes the maximum vaule in a file. 

def main():
    print('Given a file name, this program will')
    print('find the maximum value in the file.\n')

    filename = input('Enter the file name: ')

    try:
        in_file = open(filename, 'r')
        max = float(in_file.readline())
        for line in in_file:
            max += float(line)
        
        in_file.close()
        print('\nThe maximum value is %.2f.' % max)

    except IOError:
        print('Could not open file')

    except ValueError:
        print('Could not convert %s to a number' % line)
        in_file.close()

main()

