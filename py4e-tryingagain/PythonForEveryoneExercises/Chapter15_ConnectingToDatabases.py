'''
Created on Feb 23, 2024

@author: rob.fenoglio
'''


import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname)<1): fname='mbox-short.txt'
fh=open(fname)
for line in fh:
    #if line.startswith('From: '): print(line)
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    print(email)
    cur.execute('Select count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()
    #print(row)
    if row is None:
        cur.execute('INSERT INTO Counts (email,count) VALUES (?,1)',(email,))
    else:
        cur.execute('UPDATE Counts SET count = count +1 WHERE email = ?',(email,))
    conn.commit()
    
    
'''This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)'''

'''    
import re
import sqlite3

conn = sqlite3.connect('Chapter15Exercise.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
    
fh = open('mbox.txt')
lst=[]
for line in fh:
    if re.search('^From ',line):
        line = line.rstrip()
        #print(line)
        sendingorg=re.findall(r'\S+@(\S+)', line)
        sendingorg=sendingorg[0]
        cur.execute('SELECT count FROM Counts WHERE org =?', (sendingorg,))
        row = cur.fetchone()
        #print(row)
        if row is None:
            cur.execute('INSERT INTO Counts (org,count) VALUES (?,1)',(sendingorg,))
        else:
            cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',(sendingorg,))
        conn.commit()
        #print(x)
        #lst=lst+sendingorg
#print(lst)
'''