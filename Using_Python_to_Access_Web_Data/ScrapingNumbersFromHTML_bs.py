# use urllib to read the HTML from the data files below, and parse the data,
# extracting numbers and compute the sum of the numbers in the file.
# http://py4e-data.dr-chuck.net/comments_42.html is where we should get data from
# This file is written so I'm able to refer back to remind myself

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

num=list()

# to ignore certificate errors for https
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

# Urlopen will return a sort of file handle we can then read. read() will read
# the entire document into a one string
# html_object is a clean html version of the page which has been parsed by bs
# tags here outputs a list that include the entire span tag with content inside
url=input("Enter URL: ")
if len(url)<1:
    url= 'http://py4e-data.dr-chuck.net/comments_42.html'

html=urllib.request.urlopen(url,context=ctx).read()
# #testing
# print('\n===OUTPUT OF HTML FROM READ()===\n',html)

html_object=BeautifulSoup(html, 'html.parser')
# #testing
# print('\n===HTML OBJECT RETURNED FROM BeautifulSoup===\n',html_object)
html_tags=html_object('span')
# #testing
# print('\n===TAGS WITH \'span\'===\n',html_tags)
for tag in html_tags:
    # # testing
    # print('\n===TAG\n',tag)
    num.append(int(tag.contents[0]))
print(sum(num))
