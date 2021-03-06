import random
import os
import datetime
import sqlite3
from string import ascii_uppercase
from initDatabase import createDB


def bangersFile():
    return os.environ.get(
        'BANGERS_FILE') or '/home/brobot/brobot/brobotDB.sqlite3'


def selectBanger():
    '''Returns a random banger from the database'''
    conn = sqlite3.connect(bangersFile())
    cur = conn.cursor()
    cur.execute('SELECT URL FROM Bangers order by Random() LIMIT 1;')
    url = cur.fetchone()
    conn.close()
    return url[0]


def loadBangers():
    '''Loads the bangers from the text file'''
    with open(bangersFile()) as f:
        bangers = [banger.replace('\n', '') for banger in f.readlines()]
    return bangers


def addBanger(text):
    '''
    Adds a banger to the text file.
    proper input would be "add <link>"
    '''
    # Strips input text to just be the url
    text = text.split('add')[1].replace(' ', '').strip()

    # Insert into SQLDB
    conn = sqlite3.connect(bangersFile())
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO Bangers VALUES (?, ?, ?, ?, ?)", [
            text, 'Title Placeholder', random.randint(0, 10),
            datetime.datetime.now(), 0
        ])

        conn.commit()
        conn.close()
    except:
        return "Failed to add banger."
    return 'Successfully added banger'


def loadFromText(textFile):
    '''Loads the list of bangers from the old text file.'''
    with open(textFile) as f:
        for banger in f.readlines():
            try:
                addBanger('add ' + banger)
            except Exception as e:
                print(e)
                print('Banger already added')


def lookupUserId(name):
    '''Looks up the userID from the user which sent a message'''

    # normally split in the nerdreply script.
    if __name__ == '__main__':
        name = name.split(':')[1].split('!')[0]

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

    conn = sqlite3.connect(bangersFile())
    cur = conn.cursor()

    cur.execute('SELECT UserID FROM Users WHERE Name = ?', (name, ))
    userID = cur.fetchone()[0]

    if userID is None:
        userID = '11'

    conn.close()
    return userID


def count():
    '''Returns a count of the bangers'''
    conn = sqlite3.connect(bangersFile())
    cur = conn.cursor()
    num_bangers = cur.execute('SELECT COUNT(*) from Bangers').fetchone()[0]
    conn.close()
    return 'You have ' + str(num_bangers) + ' bangers'


def bangerHelp():
    '''Gives some quick help info for bangerBot'''
    return 'say something with banger to get a banger.  Say add <link> to add.'


if __name__ == '__main__':
    if bangersFile() not in os.listdir(os.getcwd()):
        createDB()

        with open('test_bangers.txt') as f:
            for banger in f.readlines():
                try:
                    addBanger('add ' + banger, 5)
                except Exception as e:
                    print(e)
                    print('Banger already added')

    print(selectBanger())
    print(count())
    print(lookupUserId('match:ChrisHolla!'))
    print(lookupUserId('match:MikeLevy!'))
