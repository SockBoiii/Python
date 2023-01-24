# dice_game.py

import random    # This line is needed by the roll_die function

def main():
    print('This program plays a simple dice game')

    die1 = roll_die()
    die2 = roll_die()

    print('\nYou rolled %d and %d.' % (die1, die2))
    if die1 == die2: 
        print('You win $5.')
    else:
        print('You lose $1.')

def roll_die():
    """Return roll from 6-sided die."""
    return random.randint(1, 6)

main()
