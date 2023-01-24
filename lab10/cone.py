# Manases Garcia, William Cucinotta, Antonio Flores, Ashley Martinez
# CSCI 248 Lab#10 Problem#1
# cone.py
# 10-1-2020
#
# This program computes the volume of a cone.

import math

def main():
    print('This program computes the volume of a cone.\n')

    radius = float(input('Enter the radius: '))
    height = float(input('Enter the height: '))

    volume = compute_volume(radius, height)

    print('\nFor a radius of %.2f and height of %.2f, the cone has a volume of %.2f.' \
        % (radius, height, volume))

def compute_volume(radius, height):
    """Return volume for given radius and height."""

    return (1 / 3) * math.pi * (radius * radius) * height

main()
