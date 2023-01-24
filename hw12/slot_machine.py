# Manases Garcia
# CSCI 248 Homework #12 Probelm #1
# 11-18-2020
# 
# This program plays a slot machine game.

import slots

BAR_JACKPOT = ('-----')


def main():
    print('         *** Slot Machine ***')
    print('This game simulates a slot machine, where you')
    print('will pay $1 for each play of the machine.')
    print('Matching all 3 symbols earns the jackpot,')
    print('where the payout is 100 for 3 bars and')
    print('$25 for any other jackpot.\n')

    machine = slots.SlotMachine()
    
    num_spins = 0

    machine.pull_lever()
    while not  machine.is_jackpot():
        num_spins += 1
        print('%3d. %s.' % (num_spins, machine))
        machine.pull_lever()
    
    if machine.is_jackpot():
        reel1,reel2,reel3 = str(machine).split()
        if (reel1 and reel2 and reel3) == BAR_JACKPOT:
            num_spins += 1
            prize = 100
            print('%3d. %s.' % (num_spins, machine))
            print('\nYour prize money is $ %d' % prize)
            print('Since you played %d times,' % num_spins)
            outcome = compute_outcome(prize, num_spins)
        else:
            num_spins += 1
            prize1 = 25
            print('%3d. %s.' % (num_spins, machine))
            print('\nYour prize money is $ %d' % prize1)
            print('Since you played %d times,' % num_spins)
            outcome = compute_outcome(prize1, num_spins)

def compute_outcome(prize, spins):
    outcome = prize - spins
    if outcome > 0:
        return print('you actually won $%d.' % outcome)
    if not outcome > 0:
        outcome = spins - prize
        return print('you actually lost $%d.' % outcome)

    
main()
