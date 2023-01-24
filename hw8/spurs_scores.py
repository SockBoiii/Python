# Manases Garcia
# CSCI 248 Homework#8 Problem#1
# spurs_scores.py
# 10-21-2020
#
# This program prompts the user to enter a minimum and maximum score values
# then the program will return the number of games in which the Suprs scores
# was between the two values. 

def main():
    print('This program finds the number of games the Spurs played between')
    print('the input minimum and maximum entered by a user.')
    print('The minimum and maximum can be equal.')

    minimum = int(input('\nEnter a minimum score: '))
    maximum = int(input('\nEnter a maximum score: '))
    while minimum >  maximum or maximum < minimum:
        print('Your minimum cannot be greater then your maximum and your maximum')
        print('cannot be less then your minimum.')
        minimum = int(input('\nEnter a minimum score: '))
        maximum = int(input('\nEnter a maximum score: '))

    count = 0 

    try:
        in_file = open('Spurs-19-20.txt', 'r')

        for line in in_file:
            score = int(line)
            if score >= minimum and score <= maximum:
                count +=1
        in_file.close()

        print('\nThe Spurs scored between %d and %d points %d times.' \
            % (minimum, maximum, count))

    except IOError:
        print('Error: Could not open the file.')

    except ValueError:
        print('Error: Could not convert score into an integer.')
        in_file.close()

main()

    
