# Manases Garcia
# CSCI 248 Homework#9 Problem#2
# count_evens.py
# 10-28-2020
#
# This program calls a function that returns how many even numbers are in 
# the given list.

def main():
    print('This program tests the count_evens function.\n')

    list1 = [0, 1, 3, 5, 9]
    list2 = [2, 8, 15, 4, 12, 24, 7, 20]
    list3 = [16, 20, 8, 14, 11, 19, 15, 7, 10]
    list4 = []

    count1 = count_evens(list1)
    count2 = count_evens(list2)
    count3 = count_evens(list3)
    count4 = count_evens(list4)

    if count1 == 1:
        print('Correct: 1 even number in list1')
    else:
        print('Should be 1 even number in list1, but function returned %d.' \
            % count1)

    if count2 == 6:
        print('Correct: 6 even numbers in list2')
    else:
        print('Should be 6 even numbers in list2, but function returned %d.' \
            % count2)

    if count3 == 5:
        print('Correct: 5 even numbers in list3')
    else:
        print('Should be 5 even numbers in list3, but function returned %d.' \
            % count3)

    if count4 == 0:
        print('Correct: 0 even numbers in list4')
    else:
        print('Should be 0 even numbers in list4, but function returned %d.' \
            % count4)


def count_evens(num_list):
    even_count = 0
    for num in num_list:
        if num % 2 == 0:
            even_count += 1
    return even_count
main()
