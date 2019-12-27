# The program will use urllib to read the HTML from the data files below, extract
# the href= vaues from the anchor tags, scan for a tag that is in a particular
# position relative to the first name in the list, follow that link and repeat
# the process a number of times and report the last name you find.

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
loop_count=1
url=input('Enter URL: ')
# below is to allow for testing using default url
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
    count=4
    position=3
else:
    count=input('Enter Count: ')
    position=input('Enter Position: ')
while True:
    html=urllib.request.urlopen(url,context=ctx).read()
    parsed_html_File=BeautifulSoup(html,'html.parser')

    linkL=list()
    anchor_tags=parsed_html_File('a')
    for tag in anchor_tags:
        link=tag.get('href',None)
        linkL.append(link)
    url=linkL[(int(position)-1)]
    loop_count=loop_count+1
    if loop_count>int(count):
        break
print(url)
print("Name of the person: ",re.findall('by_(.*).html',url)[0])
