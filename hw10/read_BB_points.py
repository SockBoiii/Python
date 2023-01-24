# read_BB_points.py

FILE_NAME = 'Womens-BBall-Points.csv'

def main():
    print('This program computes the average points per game')
    print("for the TLU Women's Basketball team for the last")
    print('several years.\n')

    try:
        array = build_2D_list()
        avg_list = compute_average(array)
        print_averages(avg_list)

    except IOError:
        print('Could not open the file for reading.')
    except ValueError:
        print('Error in converting item to a number.')


def build_2D_list():
    """Read the file and return 2-D list of TLU scores.

    Postcondition: First entry in each row indicates year."""

    in_file = open(FILE_NAME, 'r')
    points = []
    for line in in_file:
        row = line.split(',')
        for i in range(1, len(row)): # skip year in performing conversion
            row[i] = int(row[i])
        points.append(row)

    in_file.close()
    return points

def compute_average(array):
    """Return list of average points per game for each year in array.
    
    Postcondition: Each row is in form [year, ppg]."""
    avrg_lst = []
    sum = 0
    count = 0
    for row in len(array):
       print(len(array))

def print_averages(avg_list):
    """For each year in avg_list, print the average points per game (ppg)."""
    for row in avg_list:
        year = row[0]
        avg_ppg = row[1]
        print('For %s, the average ppg was %.1f.' % (year, avg_ppg))

main()
