# Manases Garcia
# CSCI 248 Homework#9 Problem #3
# alt_sum.py
# 10-30-2020
#
# This program test the alternating_sum function, which reutnrs the alternating
# sum of elements in a list.


def main():
    DESIRED_SUM1 = -2
    DESIRED_SUM2 = 1
    DESIRED_SUM3 = -3

    print('This program tests the alternating_sum function.\n')

    list1 = [1, 4, 9, 16, 9, 7, 4, 9, 11]
    list2 = [5, 2, 8, 6, 3, 7]
    list3 = [1, 2, 3, 4, 5, 6]

    sum1 = alternating_sum(list1)
    sum2 = alternating_sum(list2)
    sum3 = alternating_sum(list3)

    print('The alternating sum of list1 = %d.' \
        % sum1)
    if sum1 == DESIRED_SUM1:
        print('The alternating sum of list1 is correct.')
    else:
        print(('ERROR: The alternating sum of list1 '
            + 'should be %d.') % DESIRED_SUM1)

    print('\nThe alternating sum of list2 = %d.' \
        % sum2)
    if sum2 == DESIRED_SUM2:
        print('The alternating sum of list2 is correct.')
    else:
        print(('ERROR: The alternating sum of list2 '
            + 'should be %d.') % DESIRED_SUM2)

    print('\nThe alternating sum of list3 = %d.' \
        % sum3)
    if sum3 == DESIRED_SUM3:
        print('The alternating sum of list3 is correct.')
    else:
        print(('ERROR: The alternating sum of list3 '
            + 'should be %d.') % DESIRED_SUM3)

def alternating_sum(num_list):
    """Return the sum of sum1 and sum2 
       while sum1's list is alternating starting index  0 and stepping by 2
       while sum2's list is alternating starting index 1 and stepping by 2"""

    sum1 = 0
    sum2 = 0 
    for num in num_list[::2]: 
        sum1 += num
    for num in num_list[1::2]:
        sum2 += num
    
    return sum1 - sum2

main()
