# Manases Garcia
# CSCI 248 Homework#15 Problem#1
# same_lists.py
# 12-7-2020
#
# This progarm test what the same function. 

def main():
    LIST1 = [2, 5, 7, 9]
    LIST2 = [2, 5, 7, 9]
    LIST3 = [5, 2, 9, 7]
    LIST4 = [2, 5, 7, 9, 10]

    print('This program tests the same function.\n')

    if same(LIST1, LIST2):
        print('Correct: LIST1 and LIST2 are the same')
    else:
        print('ERROR: LIST1 and LIST2 should be the same')

    if not same(LIST1, LIST3):
        print('Correct: LIST1 and LIST3 are not the same')
    else:
        print('ERROR: LIST1 and LIST3 should not be the same')

    if not same(LIST1, LIST4):
        print('Correct: LIST1 and LIST4 are not the same')
    else:
        print('ERROR: LIST1 and LIST4 should not be the same')

    if same(LIST1, LIST2) == None:
        print('ERROR: same should return a value of True')
    if same(LIST1, LIST4) == None:
        print('ERROR: same should return a value of False')

def same(list1, list2):
    """Return whether or not list1 == list2"""

    if list1 == list2:
        return True
    else:
        return False



main()
