# Manases Garcia
# CSCI 248 Homework#8 Challenge Probelm#6
# popular_names_2000_2009.py
# 10-23-2020
#
# This program prompts the user to enter a name and the program will read both
# files, boys_names2000s.txt and girls_names2000s.txt, to find the name and
# rank of the given name. 

def main():
    print('\nThis program will prompt the user to enter a name and then search')
    print('the given files to find the name and rank in the files.')

    name = input('\nEnter a name: ')
    boys_rank = 0
    girls_rank = 0
    
    found = False

    try:
        in_file = open('boys_names2000s.txt', 'r')
        in_file2 = open('girls_names2000s.txt','r')

        for line in in_file:
            name_in_file = line.rstrip()
            boys_rank += 1
            if name == name_in_file:
                found = True
                print("\n%s was #%d for boys' name." % (name, boys_rank))
        if not found:
             print("\n%s did not appear in the list of boy's names" % name)

        for line in in_file2:
            name_in_file2 = line.rstrip()
            girls_rank += 1
            if name == name_in_file2:
                found = True
                print("%s was #%d for girls' name." % (name, girls_rank))
        if not found:
             print("%s didn not appear in the list of girls' names" % name)

        in_file.close()


    except IOError:
        print('\nError:Could not open files')
main()
