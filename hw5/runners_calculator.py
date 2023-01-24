# Manases Garcia
# CSCI 248 Homework#5 Problem#1
# runners_calculator.py
# 9-30-2020
#
# This progarm computes weights given in pounds and distance given in miles
# and gives total calories burned. 

def main():
    print('This program estimates the calories burned by a runner.\n')

    weight = float(input('Enter the weight in pounds: '))
    distance = float(input('Enter the distance in miles: '))

    total_calories = calories_burned(weight, distance)

    print('\nA runner weighing %.1f pounds who runs %.1f miles' 
        % (weight, distance))
    print('will burn approximately %d calories.' % total_calories)

def calories_burned(weight, distance):
    calories_burned  = 0.653 * weight * distance
    return calories_burned

main()
