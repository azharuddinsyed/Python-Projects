import re

# To print the matching string, we should use group(), else nothing will be displayed
# r'' represents a python raw string

# re.search => match pattern anywhere in the string
patterns = ['this', 'that']
text = 'Does this text match the pattern'
for pattern in patterns:
    print("Looking for '{}' in string '{}'".format(pattern, text))
    if re.search(pattern, text):
        print("Match found")
    else:
        print("Match not found")

# (.) A period => matches any character except for new line character
# group() function returns the string matched by re
print(re.search(r'Co.k.e', 'Cookie').group())

# \w (lower case w) - Matches any single character, digit or underscore
print(re.search(r'Co\wk\we', 'Cookie').group())
print(re.search(r'A\wha\w', 'A2ha_').group())

#       \W(upper case w) - Matches any character which is not part of \w (lower case w)
print(re.search(r'Azh\Wr', 'Azh@r').group())

# \s(lower case s) - Matches a single whitespace character like space, newline, tab, return
print(re.search(r'Eat\sCake', 'Eat Cake').group())

pattern1 = r'Eat\sCake'
if re.search(pattern1, 'Eat Cake'):
    print("found")
else:
    print("not found")

#  \S(upper case s) - Matches any character which is not part of \s (lower case s)
print(re.search(r'Cook\Se', 'Cookie').group())

# \t (lower case t) matches tab --------NOT WORKING-----NOT WORKING----NOT WORKING---
#print(re.search(r'Eat\tCake', 'Eat  Cake').group())

pattern2 = r'Eat\tCake'
if re.search(pattern2, 'Eat  Cake'):
    print("tab match found")
else:
    print("tab match not found")

# \n (lower case n) Matches new line
# \r (lower case r) Matches return

# \d (lower case d) Matches decimal digit (0-9)
print(re.search(r'C\d\dkie', 'C00kie').group())

pattern3 = r'C\d\dkie'
if re.search(pattern3, 'C00kie'):
    print("digit match found")
else:
    print("digit match not found")

# ^ (Carat) matches pattern at the start of a string ------------------------------------

print(re.search(r'^Eat', 'Eat Cake').group())

pattern4 = r'^Eat'
if re.search(pattern4, 'Eat Cake'):
    print("Carat match found")
else:
    print("Carat match not found")

# $ matches pattern at the end of a string --------------------------------------

print(re.search(r'Cake$', 'Eat Cake').group())

pattern5 = r'Cake$'
if re.search(pattern5, 'Eat Cake'):
    print("$ match found")
else:
    print("$ match not found")

# [a-zA-Z0-9] - Matches any character lower/upper case and any number from 0-9
print(re.match(r'Number:[0-9]', 'Number:5').group())

pattern5 = r'Number:[0-9]'
if re.search(pattern5, 'Number:5'):
    print("[a-zA-Z0-9] match found")
else:
    print("[a-zA-Z0-9] match not found")

# if the first character in a set is ^, all the characters that are not in the set will be matched
print(re.match(r'Number:[^5]', 'Number:4').group()) # here, except 5 all the other characters will be matched

# \A Upper case a, Matches only at the start of a string. Works for multiple lines

print(re.search(r'\A[A-C]ookie', 'Cookie').group())
# result - Cookie

pattern5 = r'\A[A-C]ookie'
if re.search(pattern5, 'Cookie'):
    print("\A match found")
else:
    print("\A match not found")

# \b lower case b, matches only the beginning or end of the word
print(re.search(r'\b[A-C]ookie', 'Cookie').group())

pattern5 = r'\b[A-C]ookie'
if re.search(pattern5, 'Cookie'):
    print("b match found")
else:
    print("b match not found")

# '+' checks for one or more characters towards its left
print(re.search(r'Co+kie','Cooookie').group())

# '*' checks for zero or more characters towards its left
print(re.search(r'Ca*o*kie','Caokie').group())

# '?' Checks for exactly zero or one character to its left
print(re.search(r'Colou?r', 'Color').group())

# to check the exact number of sequence repetition. For example, to check the valid phone number
# {x} - Repeat exactly x number of times
# {x,} - Repeat at least x times or more
# {x,y} - Repeat at least x times, but not more than 'y' times

print(re.search(r'\d{9,10}', '9742359375').group())

pattern5 = r'\d{9,10}'
if re.search(pattern5, '9742359375'):
    print("Phone number valid")
else:
    print("Invalid phone number")

# When a special character matches as much of search sequence(string) as possible is called greedy match
heading = r'<h1>TITLE</h1>'
print(re.match(r'<.*>', heading).group())

# if we want to match only the first <h1>, use *? which matches as little as possible
print(re.match(r'<.*?>', heading).group())

# match() checks for the match only at the beginning of the string
# search() checks for the match anywhere in the string
print(re.match(r'C','Cream').group())
print(re.search(r'C','IceCream').group())

# findall - finds all the possible matches in the entire sequence and returns them as a list of strings
# Each return string represents one match

result = re.findall(r'AV', 'AV Analytics Vidhya AV')
print(result)

email_address="Please contact me at azharuddinsd@gmail.com, azharuddinsyed1986@gmail.com"
addresses = re.findall(r'[\w\.-]+@[\w\.-]+', email_address)
for address in addresses:
    print(address)

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
    print(match.group())  ## 'b@google'

result = re.match(r'AV', 'AV Analytics Vidhya AV')
print(result.group())
#result - AV

# start() and end() represents start and end position of matched pattern in a string

result = re.match(r'AV', 'AV Analytics Vidhya AV')
print("start =", result.start())
print("end =", result.end())

# re.split() splits a string by the occurrence of given patten

result = re.split(r'y', 'Analytics')
print('re.split =', result)

# maxsplit parameter in re.split() limit the number of splits on a string

result = re.split(r'i','Analytics Vidhya')
print("without maxsplit=", result)

result = re.split(r'i','Analytics Vidhya', maxsplit=1) # defining maxsplit as 1
print("with maxsplit=", result)

# re.sub used to replace on substring with another
result = re.sub(r'Bangalore','NUZVID','I am from Bangalore')
print(result)

# re.compile() to be used the defined pattern later in the program without defining it again

pattern = re.compile('AV')
result = pattern.findall('AV Analytics Vidhya AV')
print('re.compile example :', result)
result2 = pattern.findall('AV is the largest analytic community in india')
print('re.compile example2 :', result2)



