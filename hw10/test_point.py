import point3

def main():
    print('This program tests a few methods of the Point class.\n')

    print('Testing the get_distance method...\n')

    pointA = point3.Point()
    pointB = point3.Point()

    distance = pointA.get_distance(pointB)
    if distance == 0:
        print('Correct: The distance between points A and B is 0')
    else:
        print('ERROR: The distance between points A and B ' \
            + 'should be 0')
        print('but your method returned %.2f.' % distance)

    pointC = point3.Point(1, 4)
    pointD = point3.Point(5, 1)
    distance = pointC.get_distance(pointD)
    if distance == 5:
        print('Correct: The distance between points C and D is 5')
    else:
        print('ERROR: The distance between points C and D ' \
            + 'should be 5')
        print('but your method returned %.2f.' % distance)

    print('\nTesting the move method...\n')

    pointA.set_point(3, -4)
    pointA.move(0.2, 1)
    print('After calling pointA.move(0.2, 1), point A should ' \
        + 'now be at (3.2, -3).')
    if pointA.get_x() == 3.2 and pointA.get_y() == -3:
        print('Correct: Point A is at %s.' % pointA)
    else:
        print('ERROR: Point A has the coordinates %s.' % pointA)

    pointB.set_point(5, 8)
    pointB.move(-1, -2)
    print('\nAfter calling pointB.move(-1, -2), point B should ' \
        + 'now be at (4, 6).')
    if pointB.get_x() == 4 and pointB.get_y() == 6:
        print('Correct: Point B is at %s.' % pointB)
    else:
        print('ERROR: Point B has the coordinates %s.' % pointB)

    # Checking for subtle error
    return_val = pointC.move(-0.5, 0.5)
    if isinstance(return_val, point3.Point) or return_val != None:
        print('ERROR: The move method should NOT return anything.')

    print('\nEnd of testing.')

main()
