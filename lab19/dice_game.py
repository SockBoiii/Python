# Manases Garcia, Tracy Garza, Aidyn Vargas, William Cucinotta, 
# Jackson Montgomery
# CSCI 248 Lab#19 Problem#1
# dice_game.py
#
# This program rolls a pair of dice between two players and keeps score of who
# wins.

import dice

def main():
    NUM_ROLLS = 10
    SNAKE_EYES = 2

    print('This program plays a dice game between two players, rolling a')
    print('pair of dice %d times counting score for each and reseting' \
        % NUM_ROLLS)
    print('when snake eyes is rolled.\n')

    pair = dice.PairOfDice()
    score1 = 0
    score2 = 0

    for i in range(NUM_ROLLS):
        roll1 = pair.roll()
        roll2 = pair.roll()
        if roll1 == SNAKE_EYES:
            score1 = 0
            print('SNAKE EYES')
            print('Player 1 rolled %s. Score1 = %d' \
                % (pair, score1))
        else:
            score1 += roll1
            print('Player 1 rolled %s. Score1 = %d' \
                % (pair, score1))
        if roll2 == SNAKE_EYES:
            score2 = 0
            print('SNAKE EYES')
            print('Player 2 rolled %s. Score2 = %d' \
                % (pair, score2))
        else:
            score2 += roll2
            print('Player 2 rolled %s. Score2 = %d' \
                % (pair, score2))
        
main()

