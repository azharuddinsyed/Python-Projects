# Luhn algorithm
# This algorithm validates the credit card/IMEI number

import sys
import re
def validate(number):
    user_input_raw = str(number)
    # removing white spaces between numbers if entered
    user_input = user_input_raw.strip().replace(' ', '')

# checks whether any alphabet is present in number
    if any(a.isalpha() for a in user_input) is True:
        print("Card/IMEI number is invalid ")
        sys.exit()  # terminates the program

# checks for special characters
# regex = re.compile('[@_!#$%^&*()<>?/\|}{~:+-`=;"./,]')
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if (regex.search(user_input) != None):
        print("Card/IMEI number is invalid")
        sys.exit()

    list1 = list(map(int, user_input))
    list2 = []
    counter = 0

    for digit in list1[::-1]:
        counter += 1
        if counter % 2 == 0:
            even_element = digit * 2
            if even_element > 9:
                even_element_to_list = list(map(int, str(even_element)))
                list_to_sum = sum(even_element_to_list)
                list2.append(list_to_sum)
            else:
                list2.append(even_element)
        else:
            list2.append(digit)

    list3 = list2[::-1]
    total_sum = sum(list3)
    if total_sum % 10 == 0:
        print("Card/IMEI number is VALID")
    else:
        print("INVALID Card/IMEI number")

validate(358634-0-7-325-88982)

'''
Visa - 4111111111111111
MasterCard  - 5500000000000004
American Express - 340000000000009 
Diner's Club - 30000000000004 
Carte Blanche - 30000000000004 
Discover - 6011000000000004 
en Route - 201400000000009 
JCB - 3088000000000009 
'''