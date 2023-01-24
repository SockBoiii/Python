# Manases Garcia
# Homework #3
# major_feedback.py
# 9-16-2020
# 
# This program promts the user to enter their major and will give feed back
#     accordingly.

print('\nGiven you major as a four-letter code in CAPITAL letters' \
    + ', this program will give you valuable feedback.')

major = input('\nPlease enter your major: ')

if major == 'CSCI' or major == 'ISYS':
    print("\nThat's a great major! Remember that the profesors" \
        + ' are happy to help you learn the material.')
elif major == 'MATH':
    print('\nMath and computer science make a great combination.')
elif major == 'BUSI':
    print('\nBusiness and information systems make a great combination.')
else:
    print('\nHave you considered computer sceince or information systems? They' \
        + ' require hard work but are very worthwhile.')
