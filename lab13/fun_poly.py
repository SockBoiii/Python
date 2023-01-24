# test

def polynomial(a, x):
    sum = 0
    for index in range(a):
        coefficient = a * x ** index
        sum += coefficient
    return sum
