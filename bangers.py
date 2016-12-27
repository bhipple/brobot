import random
import subprocess
import sqlite3
import os
import datetime
from string import ascii_uppercase
from initDatabase import createDB

def handle_response(text, name):
    '''Determines which function to call based on a message'''
    if 'add' in text.lower():
        return add_banger(text, name)
    elif 'count' in text.lower():
        return count()
    elif 'help' in text.lower():
        return banger_help()
    else:
        return select_banger()


def select_banger():
    '''Returns a random banger from the database'''
    conn = sqlite3.connect('iBangersBotDB.sqlite3')
    cur = conn.cursor()
    cur.execute('SELECT URL FROM Bangers order by Random() LIMIT 1;')
    url = cur.fetchone()
    conn.close()
    return url[0]


def add_banger(text, userID, add=True):
    '''
    Adds a banger to the text file.
    proper input would be "add link"
    '''
    # Strips input text to just be the url
    if add is True:
        text = text.split('add')[1].replace(' ', '').strip()

    # Insert into SQLDB
    conn = sqlite3.connect('iBangersBotDB.sqlite3')
    cur = conn.cursor()

    cur.execute("INSERT INTO Bangers VALUES (?, ?, ?, ?, ?, ?)", [
                1,
                text,
                'Title Placeholder',
                userID,
                datetime.datetime.now(),
                0])

    conn.commit()
    conn.close()


    return 'Successfully added banger'
    # else:
        # return "That didn't work"

def lookup_userID(name):
    '''Looks up the userID from the user which sent a message'''

    # normally split in the nerdreply script.
    if __name__ == '__main__':
        name =  name.split(':')[1].split('!')[0]

    # Why are we friends with two Chris?
    if 'Chris' in name:
        if 'B' in name:
            name = 'Chris B.'
        else:
            name = 'Chris H.'

    # CIP get some regex up in here
    else:
        first_name = name[0]
        for char in name[1:]:
            if char not in ascii_uppercase:
                first_name += char
            else:
                break
        name = first_name

    conn = sqlite3.connect('iBangersBotDB.sqlite3')
    cur = conn.cursor()

    cur.execute('SELECT UserID FROM Users WHERE Name = ?', (name,))
    userID =  cur.fetchone()[0]
    conn.close()
    return userID


def count():
    '''Returns a count of the bangers'''
    conn = sqlite3.connect('iBangersBotDB.sqlite3')
    cur = conn.cursor()
    num_bangers = cur.execute('SELECT COUNT(*) from Bangers').fetchone()[0]
    return 'You have ' + str(num_bangers) + ' bangers'


def banger_help():
    '''Gives some quick help info for bangerBot'''
    return 'say something with banger to get a banger.  Say add <link> to add.'''


if __name__ == '__main__':
    if 'iBangersBotDB.sqlite3' not in os.listdir(os.getcwd()):
        createDB()

        with open('bangers.txt') as f:
            for banger in f.readlines():
                try:
                    add_banger(banger, 5, False)
                except Exception as e:
                    print(e)
                    print('Banger already added')

    print(select_banger())
    print(count())
    print(lookup_userID('match:ChrisHolla!'))
    print(lookup_userID('match:MikeLevy!'))
