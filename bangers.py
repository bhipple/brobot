import random
import subprocess
import sqlite3
import os
import datetime
from initDatabase import createDB

def handle_response(text):
    '''Determines which function to call based on a message'''
    if 'add' in text.lower():
        return add_banger(text)
    elif 'count' in text.lower():
        return count()
    elif 'help' in text.lower():
        return banger_help()
    else:
        return select_banger()


def select_banger():
    '''Returns a random banger from the database'''
    # How it worked on the text file
    # return random.choice(load_bangers())

    conn = sqlite3.connect('iBangersBotDB.sqlite3')
    cur = conn.cursor()


    cur.execute('SELECT URL FROM Bangers order by Random() LIMIT 1;')
    url = cur.fetchone()
    conn.close()
    return url


def load_bangers():
    '''Loads the bangers from the text file'''
    with open('bangers.txt') as f:
        bangers = [banger.replace('\n','') for banger in f.readlines()]
    return bangers


def add_banger(text, userID):
    '''
    Adds a banger to the text file.
    proper input would be "add link"
    '''
    # Strips input text to just be the url
    text = text.split('add')[1].replace(' ', '').strip()

    # check = subprocess.check_output('curl -Isl ' + text, shell=True)
    # if '200' in check:

    # Append to bangers.txt
    with open('bangers.txt', 'a') as f:
        f.write(text)

    # Insert into SQLDB
    conn = sqlite3.connect('iBangersBotDB.sqlite3')
    cur = conn.cursor()

    cur.execute("INSERT INTO Bangers VALUES (?, ?, ?, ?, ?, ?)",
                1,
                text,
                'Title Placeholder',
                userID,
                datetime.datetime.now(),
                0)

    conn.commit()
    conn.close()


    return 'Successfully added banger'
    # else:
        # return "That didn't work"

def lookup_userID(user):
    '''Looks up the userID from the user which sent a message'''
    conn = sqlite3.connect('iBangersBotDB.sqlite3')
    cur = conn.cursor()
    cur.execute('SELECT UserID FROM Users WHERE Name = ?', (user,))
    userID =  cur.fetchone()[0]
    conn.close()
    return userID


def count():
    '''Returns a count of the bangers'''
    bangers = load_bangers()
    return 'You have ' + str(len(bangers)) + ' bangers'


def banger_help():
    '''Gives some quick help info for bangerBot'''
    return 'say something with banger to get a banger.  Say add <link> to add.'''


if __name__ == '__main__':
    if 'iBangersBotDB.sqlite3' not in os.listdir():
        createDB()
    string = r'''add https://www.youtube.com/watch?v=_4X-LNUL-tA'''
    add_banger(string, 5)
    # add_banger(r'''add https://www.youtube.com/watch?v=HIOxVovud88''', 5)
    # add_banger(r'''add https://www.youtube.com/watch?v=dTW2MxfqVLI''', 5)

    print(select_banger())
    # print(count())
    print(lookup_userID('Mike'))












