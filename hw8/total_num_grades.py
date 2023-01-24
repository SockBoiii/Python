# Manases Garcia
# CSCI 248 Homework#8 Problem #2
# total_num_grades.py
# 10-23-2020
#
# This program prompts the user to enter a file to read the data from the file,
# and then will determine and print the total number of grads and number of A's
# B's and C's using the standard grading scale. 

def main():
    print('\nThis program will prompt the user to enter a file, the program')
    print('will read the file and print the total numbers of grades in')
    print('the file and print the number of letter grades using the')
    print('standard grading scale.')

    total_grades = 0
    gradeA = 0
    gradeB = 0
    gradeC = 0
    gradeD = 0
    gradeF = 0

    filename = input('\nEnter the file name: ')

    try:
        in_file = open(filename, 'r')

        for line in in_file:
            total_grades += 1
            grade = float(line)
            if grade >= 90:
                gradeA += 1
            elif grade >= 80:
                gradeB += 1
            elif grade >= 70:
                gradeC += 1
            elif grade >= 60:
                gradeD += 1
            else:
                gradeF += 1

        in_file.close()
        print('\nTotal number of grades = %d' % total_grades)
        print("Number of A's = %d" % gradeA)
        print("Number of B's = %d" % gradeB)
        print("Number of C's = %d" % gradeC)
        print("Number of D's = %d" % gradeD)
        print("Number of F's = %d" % gradeF)

    except IOError:
        print('\nError:Could not open file')

    except ValueError:
        print('\nError:Could not convert line into a float')
        in_file.close()

main()

