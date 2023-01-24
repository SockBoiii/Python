# Manases Garcia
# CSCI #248 Homework#7 Problem#5
# cynlinder.py
# 10-16-2020
#
# This is a module for computing volume and surface area of a cylinder. 

import math

def compute_volume(radius, height):
    """Return the volume of the cylinder.

    Precondition: Radius > 0 and Height > 0
    Raise: ValueError if Radius < 0 or Height < 0"""
    if radius > 0 or height > 0:
        return math.pi * (radius ** 2) * height
    else:
        raise ValueError('Radius or Height cannot be negative.')
        # I know this isn't right but I am running short on time. 
        
def compute_surface_area(radius, height):
    """Return the surface area of the cylinder.

    Precondition: Radius > 0 and Height > 0:
    Raise: ValueError if Radius < 0 or Height < 0"""
    if radius > 0 or height > 0:
        return 2 * math.pi * (radius ** 2) + 2 * math.pi * radius * height
    else:
        raise ValueError('Radius or Height cannot be negative.')
        # I know this isn't right but I am running short on time. 



    
