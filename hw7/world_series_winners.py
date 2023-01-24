# Manases Garcia
# CSCI 248 Homework#7 Problem#4
# world_series_winners.py
# 10-16-2020
#
# This program prompts the user to input a baseball team, then this program
# will read from world_series.txt, and say how many times that team won the
# world seires. 

def main():
    print('                 ***  WORLD SERIES WINNERS  ***')
    print('\nGiven the name of a team (e.g., Texas Rangers or New York Yankees),')
    print('this program will determin how many times that team won the')
    print('World Series in 1903-2019.')
   
        
    team_name = input('\nEnter the name of the team: ')

    try:
        in_file = open('world_series.txt','r')

        wins = 0
        
        for line in in_file:
            if team_name in line:
                wins += 1

        in_file.close()

        if wins > 0:
            print('\nThe %s won the World Series %d time.' % (team_name, wins))
        else:
            print('\nThe %s never won the World Series.' % team_name)

    except IOError:
        print('Could not open the file.')

main()
