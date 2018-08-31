import re

NameAge = '''
Azhar is 32 and Sai is 34
Sasi is 33 and Pushkar is 31
'''
ages = re.findall(r'\d{1,3}', NameAge)
names = re.findall(r'[A-Z][a-z]*', NameAge)


ageDict = {}
x = 0

for eachname in names:
    ageDict[eachname] = ages[x]
    x += 1

print(ageDict)

#re.search -> check the word in a string

if re.search("inform", "We need to inform him with the latest information"):
  print("word found")

# re.findall - > finds the occurrances of a word in a string

all_inform=re.findall("inform", "We need to inform him with the latest information")

for i in all_inform:
  print(i)

# to get the starting and ending index of a particular string

string = "We need to inform him with the latest information"

for i in re.finditer('inform',string):
  print(i.span())

# Match words with particular pattern

str="Sat, hat, mat, pat"
all_strings=re.findall("[Shmp]at", str)

for i in all_strings:
  print(i)

# Match series of range of characters

str1="sat, hat, mat, pat"
all_strings=re.findall("[h-m]at",str1)

for i in all_strings:
  print(i)

# Replace a string

food = "hat rat mat pat"
regex=re.compile('[r]at')
food = regex.sub("food", food)
print(food)

#\d matches any number which is present
#\D matches any thing other than number
randstr='12345'
randstr1='1a2b3C'
print("Matches:", len(re.findall('\d', randstr)))
print("Matches:", len(re.findall('\D', randstr1)))

# to match specific digit

randstr='12345'
print("Matches:", len(re.findall('\d{5}', randstr)))

# Matching digits at certain range

randstr2 = '123 1234 12345 123456 1234567'
print("Matches:",re.findall('\d{5,7}',randstr2))
print("Matches:",len(re.findall('\d{5,7}',randstr2)))

# validating phone number

#\w matches anything in [a-zA-z0-9_]
#\W matches anything other than [a-zA-z0-9_]

Phone = '974-235-9375'

if re.search("\w{3}-\w{3}-\w{4}", Phone):  # also works if u give \d instead of \w
  print("It is a phone number")


# To check full name is valid or not. This checks space between First name and Last name
# \f - formfeed \n new line \r carriage return \t tab \v vertical tab
# \s [\f\n\r\t\v]
# \S not of [\f\n\r\t\v]

if re.search("\w{2,20}\s\w{2,20}", "Azharuddin Syed"): # First name(2 to 20 char) + \f\n\r\t\v + last name(2 to 20 char)
    print("full name is valid")

# email address validation

email = "azharuddinsd@gmail.com md@.com @seo.com dc@.com"

print("Email matches:", len(re.findall('[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}', email)))
