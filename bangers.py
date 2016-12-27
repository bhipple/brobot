import random
import subprocess
import sqlite3
import os
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
    '''Returns a random banger from the bangers text file'''
    return random.choice(load_bangers())


def load_bangers():
    '''Loads the bangers from the text file'''
    with open('bangers.txt') as f:
        bangers = [banger.replace('\n','') for banger in f.readlines()]
    return bangers


def add_banger(text, userID, DBConn):
    '''
    Adds a banger to the text file.
    proper input would be "add link"
    '''
    text = text.split('add')[1].replace(' ', '').strip()
    # check = subprocess.check_output('curl -Isl ' + text, shell=True)
    # if '200' in check:
    with open('bangers.txt', 'a') as f:
        f.write(text)

    conn = sqlite3.connect('iBangersBotDB.sqlite3')
    cur = conn.cursor()
    cur.execute('INSERT INTO Bangers VALUES ('



    return 'Successfully added banger'
    # else:
        # return "That didn't work"

def lookup_userID(user):
    '''Looks up the userID from the user which sent a message'''
    conn = sqlite3.connect('iBangersBotDB.sqlite3')
    cur = conn.cursor()

    cur.execute('SELECT UserID FROM Users WHERE Name = ?', (user,))
    return cur.fetchone()[0]


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
    print(select_banger())
    print(select_banger())
    print(select_banger())
    print(count())
    print(lookup_userID('Mike'))
