#!/usr/bin/python

import sys

def get_songs(filename):
    with open(filename, 'r') as f:
        songs = []
        for line in f:
            parts = line.split('\t')
            title = parts[0].strip('"')
            year = int(parts[1])
            album = parts[2]
            songwriter = parts[3]
            songs.append({
                "title": title,
                "year": year,
                "album": album,
                "songwriter": songwriter
            })
        return songs

def get_matching(songs, word):
    matching = []
    for song in songs:
        if any(word in part for part in song['title'].lower().split()):
            matching.append(song)
    return matching

if __name__ == '__main__':
    try:
        songs = get_songs(sys.argv[1])    
        matching = get_matching(songs, sys.argv[2])
        if len(matching) == 0:
            print 'no matches (%d total songs)' % len(songs)
        for i, song in enumerate(matching):
            print '%d: %s' % (i+1, song['title'])
    except Exception, e:
        print e
        print 'Usage: %s <songs> <matching phrase>' % __file__