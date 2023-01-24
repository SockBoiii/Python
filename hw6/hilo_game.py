# Manases Garcia
# CSCI 248 Homework#6 Problem#2
# hilo_game.py
# 10-8-2020
# 
# This program is a game, in which the user will guess a number and
# will see if it is matches with the randomly selected number the program
# has chosen. It is not matched, the program will say the number is
# higher or lower. 

import random

QUIT = 0
MAXIMUM_VALUE  = 100

def main():
    print('This is the high or low game!')
    print('\nGuess a number and this program will tell if you are correct,')
    print('or if you need to guess higher, or guess lower!.')
    print('\nFrom 1 to %d. What number did I pick?' % MAXIMUM_VALUE)
    print('\nTo quit the game enter: 0')

    random_num = random.randint(1, MAXIMUM_VALUE + 1)
    
    guess = int(input('\nGuess a number: '))

    while guess != random_num and guess != QUIT:
        if guess < random_num:
            print('Your guess is too low!')
            guess = int(input('\nGuess a number: '))
        else:
            print('Your guess is too high!')
            guess = int(input('\nGuess a number: '))
    if guess == random_num:
        print('Your guess of %d is correct!' % random_num)
    else:
        print('The correct guess was %d! Come and play again soon!' % random_num)

main()
