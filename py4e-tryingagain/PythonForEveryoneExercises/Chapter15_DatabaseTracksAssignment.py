'''
Created on Dec 13, 2025

@author: rob.fenoglio
'''
import sqlite3

conn = sqlite3.connect('MusicTracksDatabase.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('DROP TABLE IF EXISTS Album')
cur.execute('DROP TABLE IF EXISTS Track')

cur.execute('CREATE TABLE Artist (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,name    TEXT UNIQUE)');
cur.execute ('CREATE TABLE Genre (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,name    TEXT UNIQUE)');
cur.execute ('''CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE)'''
);
cur.execute ('''CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER)'''
);

fh=open('tracks.csv')
for line in fh:
    #if line.startswith('From: '): print(line)
    pieces = line.split(',')
    print (pieces[0])
