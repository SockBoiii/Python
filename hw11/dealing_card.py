# Manases Garcia
# CSCI 248 Homework#11 Challenge Problem #10
# dealing_card.py
# 11-12-2020
# 
# This program deals cards, while counting them, and stops when both an ace
# card or a face card is found. 

import cards

def main():
    print('This program will print and count each card that is being dealt')
    print('until an ace card and face card are found, then it will stop')
    print('and print the total number of cards dealt.\n')
    
    deck = cards.DeckOfCards()
    card_count = 0 
    ace_card = False
    face_card = False
    
    card = deck.deal()
    while (ace_card and face_card) == False:
        card_count += 1
        print('The card was %s.' % card)
        if card.is_ace():
            ace_card = True
        elif card.is_face_card():
            face_card = True
        if ace_card and face_card == True:
            print('\nThere were %d total cards dealt.\n' % card_count)
        card = deck.deal()
main()
