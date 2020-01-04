#read a textfile from a website
import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
import sqlite3
import ssl
import re

# to ignore certificate errors for https
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

#ask for url
url=input('Enter URL for txt file: ')
if len(url)<1:
    url='https://www.py4e.com/code3/mbox.txt'

#create db
connection=sqlite3.connect('organizationalCount.sqlite')
cur=connection.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts(org TEXT,count INTEGER)')
connection.commit()

#this wont work on this site so pretend to be a browser since spidering is blocked
req = Request('https://www.py4e.com/code3/mbox.txt', headers={'User-Agent': 'Mozilla/5.0'})
fhand = urlopen(req,context=ctx).read().decode()
fhand=fhand.splitlines()
count=0

#Parse data by lines then extract the org name then run SQL to either increment
#existing organizational count or to add new organization
for elements in fhand:
    if elements.startswith('From '):
        elements=elements.split()
        element=elements[1].split('@')
        org=element[1]
        cur.execute('SELECT count FROM Counts WHERE org=?',(org,))
        row=cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts(org,count) VALUES(?,1)',(org,))
        else:
            cur.execute('UPDATE Counts SET count=count+1 WHERE org=?',(org,))
connection.commit()

#print out the result
for row in cur.execute('SELECT org, count FROM Counts ORDER BY count DESC'):
    print(str(row[0]), row[1])

#close connection
cur.close()
