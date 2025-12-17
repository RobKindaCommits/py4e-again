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
    line=line.strip()
    #print(line)
    pieces = line.split(',')
    if len(pieces) < 6 : continue
    title = (pieces[0])
    artist = (pieces[1])
    albumtitle = (pieces[2])
    genre = (pieces[6])
    #print (name, artist, album, genre)
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( albumtitle, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (albumtitle, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id) 
        VALUES ( ?, ?, ?)''', 
        ( title, album_id, genre_id ) )

    conn.commit()

    
