# Manases Garcia
# CSCI 248 Homework#5 Problem#4
# election_year.py
# 10-2-2020
#
# This program tells you whether or not the selected year was an 
# election year or not.

def main():
    print('This program tests the is_election_year() function')
    print('for determining presidential election years.\n')

    if is_election_year(1980):
        print('Correct: 1980 was an election year')
    else:
        print('ERROR: 1980 should have been an election year')

    if is_election_year(2000):
        print('Correct: 2000 was an election year')
    else:
        print('ERROR: 2000 should have been an election year')

    if is_election_year(2012):
        print('Correct: 2012 was an election year')
    else:
        print('ERROR: 2012 should have been an election year')

    if is_election_year(2016):
        print('Correct: 2016 was an election year')
    else:
        print('ERROR: 2016 should have been an election year')

    if is_election_year(2017) == None:
        # Catch a subtle error that students sometimes make
        print('ERROR: Function did not return a value for 2017')
    elif not is_election_year(2017):
        print('Correct: 2017 was not an election year')
    else:
        print('ERROR: 2017 should not have been an election year')

    if is_election_year(2018) == None:
        # Catch a subtle error that students sometimes make
        print('ERROR: Function did not return a value for 2018')
    elif not is_election_year(2018):
        print('Correct: 2018 was not an election year')
    else:
        print('ERROR: 2018 should not have been an election year')

    if is_election_year(2019) == None:
        # Catch a subtle error that students sometimes make
        print('ERROR: Function did not return a value for 2019')
    elif not is_election_year(2019):
        print('Correct: 2019 was not an election year')
    else:
        print('ERROR: 2019 should not have been an election year')

    if is_election_year(2020) == None:
        # Catch a subtle error that students sometimes make
        print('ERROR: Function did not return a value for 2020')
    elif is_election_year(2020):
        print('Correct: 2020 is an election year')
    else:
        print('ERROR: 2020 should have been an election year')

    if is_election_year(2021) == None:
        # Catch a subtle error that students sometimes make
        print('ERROR: Function did not return a value for 2021')
    elif not is_election_year(2021):
        print('Correct: 2021 is not an election year')
    else:
        print('ERROR: 2021 should not have been an election year')

    if is_election_year(2022) == None:
        # Catch a subtle error that students sometimes make
        print('ERROR: Function did not return a value for 2022')
    elif not is_election_year(2022):
        print('Correct: 2022 is not an election year')
    else:
        print('ERROR: 2022 should not have been an election year')

def is_election_year(year):
    """Reutrn whether or not year is an election year."""
    return year % 2 == 0 \
        and (year % 1 != 0 or year % 4 == 0 or year % 12 == 0) 


main()
