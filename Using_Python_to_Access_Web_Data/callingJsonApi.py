# prompt for a location, contact a web service and retrieve JSON for the web
# service and parse that data, and retrieve the first place_id from the JSON.
# A place ID is a textual identifier that uniquely identifies a place as within
# Google Map
import urllib.request,urllib.parse,urllib.error
import ssl
import json
API_URL='http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    location=input('Enter a Location: ')
    if len(location)<1:
        location='South Federal University'
        print('retrieving default Location: South Federal University')
    url=API_URL+urllib.parse.urlencode({'address':location,'key':42})
    reqHandApi=urllib.request.urlopen(url)
    data=reqHandApi.read().decode()
    # print(data)

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print("ERROR, can't retrieve location")
        # print(data)
        continue
    place_id=js['results'][0]['place_id']
    print(place_id)

    break
