# Manases Garcia
# CSCI 248 Homework#12 Challenge Problem #12
# hilo_card_game.py
# 11-20-2020
#
# This program plays a high or low game with a deck of card where the user
# input if the next card is going to have a value high or lower then the
# current card. 

import cards

def main():
    print('This program lets you play a simple card game called High-Low.')
    print('A card will be dealt from a deck of cards. You must predict')
    print('whether the next card will be higher (H) or lower(L). If you guess')
    print('correctly, anothe card will be dealt and you will guess again.')
    print('Your score will be the number of correct predictions. Note that')
    print('a tie counts as an incorrect guess.')

    count = 0 
    lose = False

    deck = cards.DeckOfCards()
    
    current_card = deck.deal()
    print('\nThe current card is %s.' % current_card)
    next_card = deck.deal()
    while lose == False:
        next_face = next_card.get_face()
        current_face = current_card.get_face()
        guess = input('Enter your next guess (H or L): ').upper()
        print('\nThe next card was %s.' % next_card)
        if next_face > current_face:
            if guess == 'H':
                print('Your prediction was correct.')
                count += 1
                current_card = next_card
                next_card = deck.deal()
            else:
                print('\nYour prediction was incorrect.')
                lose = True
                print('\nGame over! Your score was %d.' % count)
        elif next_face < current_face:
            if guess == 'L':
                print('Your prediction was correct.')
                count += 1
                current_card = next_card
                next_card = deck.deal()
            else:
                print('\nYour prediction was incorrect.')
                lose = True
                print('\nGame over! Your score was %d.' % count)
        elif next_face == current_face:
            print('\nSorry, but you lose on ties!')
            lose = True
            print('\nGame over! Your score was %d.' % count)
        


main()
