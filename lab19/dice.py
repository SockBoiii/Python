# dice.py

"""Provide the Die and PairOfDice classes.

Die -- a single 6-sided die
    __init__(self) -- initialize die with random face value
    __int__(self) -- return integer representation of die
    get_value(self) -- return the die's face value
    roll(self) -- roll the die and return its new face value
    __str__(self) -- return the face value as a string

PairOfDice -- two 6-sided dice
    __init__(self) -- initialize dice with random face values
    get_value1(self) -- return face value of first die as an int
    get_value2(self) -- return face value of second die as an int
    get_total(self) -- return sum of the face values
    roll(self) -- roll the dice and return the new sum
    __str__(self) -- return the face values as a string
"""

import random

class Die:

    """Represent a 6-sided die."""

    def __init__(self):
        """Initialize die with random face value."""
        self.roll()

    def __int__(self):
        """Return integer representation of the die."""
        return self.__value
    
    def get_value(self):
        """Return the die's face value."""
        return self.__value
    
    def roll(self):
        """Roll the die and return its new face value."""
        self.__value = random.randint(1, 6)
        return self.__value

    def __str__(self):
        """Return the face value as a string."""
        return str(self.__value)

class PairOfDice:

    """Represent two 6-sided dice."""

    def __init__(self):
        """Initialize dice with random face values."""
        self.__die1 = Die()
        self.__die2 = Die()

    def get_value1(self):
        """Return face value of first die as an int."""
        return self.__die1.get_value()

    def get_value2(self):
        """Return face value of second die as an int."""
        return self.__die2.get_value()

    def get_total(self):
        """Return the sum of the face values."""
        return self.__die1.get_value() + self.__die2.get_value()

    def roll(self):
        """Roll the dice and return the new sum."""
        return self.__die1.roll() + self.__die2.roll()

    def __str__(self):
        """Return the face values as a string."""
        return '%s %s' % (self.__die1, self.__die2)

        # Alternate solution: 
        # return str(self.__die1) + ' ' + str(self.__die2)

