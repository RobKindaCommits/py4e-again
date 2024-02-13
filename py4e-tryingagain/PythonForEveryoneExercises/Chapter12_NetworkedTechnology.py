'''
Created on Feb 4, 2024

@author: rob.fenoglio
'''
'''
# make a socket connection
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80))
'''

'''
# following along
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(1024)
    #if you set the data length to 512 bits, it cuts off the 4th line
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
'''
'''
# same as above but using urllib
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts=dict()
for line in fhand:
    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0)+1
print(counts)
'''

'''
# Example script to pull all the links from a page
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -' )
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
'''

'''
#Exercise 12.x
#The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1735176.html (Sum ends with 93)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter -' )
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
#print(tags)
sumoftags = 0
for tag in tags:
    #print('Contents:', tag.contents[0])
    currenttagvalue = int(tag.contents[0])
    sumoftags = sumoftags + currenttagvalue
print(sumoftags)
'''


#Exercise 12.x
#In this assignment you will write a Python program that expands on 
#http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from 
#the data files below, extract the href= vaues from the anchor tags, scan for a tag that 
#is in a particular position relative to the first name in the list, follow that link and 
#repeat the process a number of times and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter -' )
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')    

tags = soup('a')
iterationcount = 6
#print(tags[17].contents[0])
#print(tags[2].get('href', None))
newurl = tags[17].get('href', None)
while iterationcount > 0:
    newhtml = urllib.request.urlopen(newurl).read()
    newsoup = BeautifulSoup(newhtml, 'html.parser')
    newtags = newsoup('a')
    #print(newtags[17].contents[0])
    newurl = newtags[17].get('href', None)
    iterationcount = iterationcount - 1
print(newtags[17].contents[0])



