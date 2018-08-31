# Get all phone numbers from a web page using regular expressions
# urllib.request module contains functions and classes which helps in opening URLs

import urllib.request
from re import findall

url = "https://www.summet.com/dmsi/html/codesamples/addresses.html"

response = urllib.request.urlopen(url)
html = response.read()
htmlStr = html.decode()
phone_data = findall("\(\d{3}\) \d{3}-\d{4}", htmlStr)

for item in phone_data:
    print(item)