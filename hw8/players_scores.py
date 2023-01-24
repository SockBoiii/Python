# Manases Garcia
# CSCI 248 Homework#8 Problem#3
# players_scores.py
# 10-23-2020
#
# This program displays the name and score for all players who achieved a
# minimum score of 30,000 points.

minimum_score = 30000

def main():
    print('\nThis program displays information form the Hogwarts')
    print('video game tournament. All players with a score of')
    print('%d or higher are listed below.\n' % minimum_score)

    try:
        in_file = open('scores.txt','r')

        name = in_file.readline().rstrip()
        while name != '':
            player_score = int(in_file.readline())
            if player_score >= minimum_score:
                print('%-20s %d' % (name, player_score))

            name = in_file.readline().rstrip()
        
        in_file.close
           
    except IOError:
        print('Could not open "scores.txt"')

    except ValueError:
        print('Error converting player_score into an integer.')
        in_file.close

main()
