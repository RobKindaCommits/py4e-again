'''
Created on Feb 6, 2024

@author: rob.fenoglio
'''

'''
#Following along in lecture
import xml.etree.ElementTree as ET
inputthing = ''''''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>''''''

stuff = ET.fromstring(inputthing)
lst = stuff.findall('users/user')
print(lst)
for item in lst:
    print('Name:', item.find('name').text, 'ID:', item.find('id').text, 'Attribute:', item.get("x"))
'''


#Exercise 13.x reading a page of html and summing values from particular nested tags
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ' )
print ('Retrieving', url)
xmldata = urllib.request.urlopen(url).read()

print('Retrieved',len(xmldata),'characters')
#print(xmldata.decode())
tree = ET.fromstring(xmldata)
# Now collect up all the <count></count> elements
counts = tree.findall('.//count')
totalcount=0
totalcountsum=0
for count in counts:
    #print(count.text)
    totalcount=totalcount+1
    totalcountsum=totalcountsum + int(count.text)
print('Count:',totalcount)
print('Sum:',totalcountsum)



