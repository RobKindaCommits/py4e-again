'''
Created on Feb 10, 2024

@author: rob.fenoglio
'''
import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = input('Enter location: ')
print('Retrieving',serviceurl)
rawdata = urllib.request.urlopen(serviceurl).read()
data = rawdata.decode()
print('Retrieved', len(data), 'characters')
print(data)
#datajson = json.loads(data)
#print(json.dumps(datajson, indent = 2))
#print(datajson['comments'][0]['name'])
#print(datajson)