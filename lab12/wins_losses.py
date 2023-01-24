# Manases Garcia, Christian Mitchell, Bryce Chimene
#CSCI 248 Lab#12 Problem#1
# wins_losses.py
# 10-13-2020
#
# This program displays information on the TLU Men's Basketball Team for the
# 2018-2019 season.

def main():
    FILE_NAME = 'MensBasketball18-19.txt'

    print('This program displays information on the TLU')
    print("Men's Basketball Team for the 2018-19 season.\n")


    try:
        in_file = open(FILE_NAME, 'r')
        opponent = in_file.readline().rstrip()
        while opponent != '':
            tlu_score = int(in_file.readline())
            opp_score = int(in_file.readline())
            opponent = in_file.readline().rstrip()
            if tlu_score > opp_score:
                print('TLU beat %s by a score of %d-%d.' \
                    % (opponent, tlu_score, opp_score))
            else:  # No tied in basketball
                print('TLU lost to %s by a score of %d-%d.' \
                  % (opponent, tlu_score, opp_score))
        in_file.close()

    except IOError:
        print('Could not open %s.' % FILE_NAME)

    except ValueError:
        print('Error in converting line to a integer.')
        in_flie.close()

main()
