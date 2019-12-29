 # prompt for a URL, read the XML data from that URL using urllib and then parse
 # and extract the comment counts from the XML data, compute the sum of the numbers
 # in the file.
import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET
import ssl
# from bs4 import BeautifulSoup

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('URL: ')
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/comments_42.xml'
print("Retrieving: ",url)

xmlString=urllib.request.urlopen(url,context=ctx).read()
# parsed_xml=BeautifulSoup(fhand,'html.parser')
xmlTree=ET.fromstring(xmlString)
tagList=xmlTree.findall('comments/comment')
# print(tagList)
count=list()
for tag in tagList:
    # print('Name: ',tag.find('name').text)
    # print('Count:',tag.find('count').text)
    count.append(int(tag.find('count').text))
print('Count:',len(count))
print('Sum: ',sum(count))
