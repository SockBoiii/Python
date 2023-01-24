# slots.py

# Put your import statement here

import random

class SlotMachine:

    """Represent a basic slot machine with 3 reels."""

    # symbols for the slot machine, unless otherwise specified
    __symbols = ['-----', '77777', '$$$$$', '*****',
        'XXXXX', 'OOOOO', '~~~~~', '!!!!!']

    def __init__(self, symbols=__symbols):
        """Initialize slot machine."""
        self.__list = [] + symbols
        self.pull_lever()

    def get_reel1(self):
        """Return symbol on the first reel."""
        return self.__reel1 

    def get_reel2(self):
        """Return symbol on the second reel."""
        return self.__reel2

    def get_reel3(self):
        """Return symbol on the third reel."""
        return self.__reel3

    def pull_lever(self):
        """Spin the reels and return the 3 values."""
        self.__reel1 = random.choice(self.__list)
        self.__reel2 = random.choice(self.__list)
        self.__reel3 = random.choice(self.__list)
       
    def is_jackpot(self):
        """Return true if jackpot (all 3 reels the same)."""
        return  self.__reel1 == self.__reel2 and self.__reel1 == self.__reel3

    def __str__(self):
        """Return string representation."""
        return '%s %s %s' \
            % (self.__reel1, self.__reel2, self.__reel3)

