# prompt for a URL, read the JSON data from that URL using urllib and then parse
# and extract the comment counts from the JSON data, compute the sum of the
# numbers in the file
import urllib.request, urllib.parse,urllib.error
import json
import ssl

#ignore cert
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter URL: ')
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/comments_42.json'
fhand=urllib.request.urlopen(url,context=ctx).read().decode()
formattedJson=json.loads(fhand)
countNum=list()

for counts in formattedJson['comments']:
    countNum.append(counts['count'])
print(countNum)
print(sum(countNum))
