# Manases Garcia
# CSCI 248 Homework#9 Challenege Problem#7
# prime_factors.py
# 10-31-2020
#
# This program prompts the user to enter a positive interger and then will
# return a listen with the prime factors given. 

def main():
    print('This program promts the user to enter a postive integer and')
    print('returns a list with prime fractors of the given integer.')

    num = int(input('\nEnter a postive integer: '))

    while num < 0:
        print('\nYou entered a negitive interger. Enter a postive integer!')
        num = int(input('\nEnter a postive integer: '))

    prime_list = prime_factorization(num)

    print(prime_list)

def prime_factorization(num):
    prime_list = []
    
    while num % 2 == 0:
        prime_list.append(2)
        num //= 2
    for factor in range(3, num):
        while  num % factor == 0:
            prime_list.append(factor)
            num //= factor
    if num > 2:
        prime_list.append(num)
    return prime_list

main()
