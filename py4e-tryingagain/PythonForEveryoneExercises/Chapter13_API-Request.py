'''
Created on Feb 9, 2024

@author: rob.fenoglio
'''

'''
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print a JSON out pretty-like with indenting based on indent parameter
    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
'''

'''
#   Extract Data from JSON exercise

import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = input('Enter location: ')
print('Retrieving',serviceurl)
rawdata = urllib.request.urlopen(serviceurl).read()
data = rawdata.decode()
print('Retrieved', len(data), 'characters')
#print(data)
datajson = json.loads(data)
print(json.dumps(datajson, indent = 2))
#print(datajson['comments'][0]['name'])
#print(datajson)
# When dealing with a multi-level JSON, you apparently have to be specific when defining the iteration variable
# When I left it as 'for item in datajson' the iteration variable instances were just strings
totalcount=0
totalsum=0
for item in datajson['comments']:
    #print(item['count'])
    iterationvalue = int(item['count'])
    totalsum = totalsum + iterationvalue
    totalcount=totalcount+1
print('Count:', totalcount)
print('Sum:',totalsum)
'''

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    #address = 'University of Colorado at Boulder'
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print a JSON out pretty-like with indenting based on indent parameter
    #print(json.dumps(js, indent=4))
 
    #print(location)
    placeid = js['results'][0]['place_id']
    print(placeid)