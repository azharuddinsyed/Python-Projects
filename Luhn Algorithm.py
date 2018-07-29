# Luhn algorithm
# This algorithm validates the credit card number
# def Luhn(number):
# input1=str(number)
import sys
import re

input1 = input("Enter Credit Card/IMEI number:")
input2 = input1.strip().replace(' ', '')

# checks whether any alphabet is present in number
if any(a.isalpha() for a in input2) is True:
    print("Card/IMEI number is invalid ")
    sys.exit()  # terminates the program

# checks for special characters
# regex = re.compile('[@_!#$%^&*()<>?/\|}{~:+-`=;"./,]')
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if (regex.search(input2) != None):
    print("Card/IMEI number is invalid")
    sys.exit()

list1 = list(map(int, input2))
list2 = []
counter = 0

for digit in list1[::-1]:
    counter += 1
    if counter % 2 == 0:
        mult = digit * 2
        if mult > 9:
            l1 = list(map(int, str(mult)))
            sum1 = sum(l1)
            list2.append(sum1)
        else:
            list2.append(mult)
    else:
        list2.append(digit)

list3 = list2[::-1]
Final_sum = sum(list3)
if Final_sum % 10 == 0:
    print("Card/IMEI number is VALID")
else:
    print("INVALID Card/IMEI number")