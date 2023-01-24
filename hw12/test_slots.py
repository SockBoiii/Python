# test_slots.py
#
# Primitive program to perform basic testing
# of the SlotMachine class.
#
# Passing these tests does not necessarily
# guarantee that your SlotMachine is entirely
# correct, but these tests will check for
# SOME of the basic errors commonly made.

import slots

def main():
    print('This program performs basic testing')
    print('of the SlotMachine class.\n')

    machine = slots.SlotMachine()
    
    print('First, pulling the lever 20 times.')
    print('Should get random output for the different pulls.\n')
    for i in range(20):
        machine.pull_lever()
        if machine.is_jackpot():
            print('%s  JACKPOT!!' % machine)
        else:
            print(machine)

    print('\nLOOK carefully at the output above.')
    print('If all 3 symbols matched in any row,')
    print('the word JACKPOT should have appeared.\n')

    print('Now testing the get_reel and')
    print('string conversion methods.')
    reel1, reel2, reel3 = str(machine).split()

    if machine.get_reel1() == reel1:
        print('Correct for call to get_reel1')
    else:
        print('Something is wrong with either')
        print('string conversion or get_reel1.')
    if machine.get_reel2() == reel2:
        print('Correct for call to get_reel2')
    else:
        print('Something is wrong with either')
        print('string conversion or get_reel2.')
    if machine.get_reel3() == reel3:
        print('Correct for call to get_reel3')
    else:
        print('Something is wrong with either')
        print('string conversion or get_reel3.')

    print('\nEnd of basic testing of SlotMachine class.')
main()
