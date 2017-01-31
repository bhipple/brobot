import sqlite3
import random as rand
import bangers


Names = ['Adam', 'Alex', 'Austin', 'Ben', 'Chris B.', 'Chris H.', 'Jim',
        'John', 'Mike', 'Sean', 'Zach', 'Guest']

def createDB():
    '''Creates the Database, the tables, and fills in the user information.'''
    conn = sqlite3.connect('brobotDB.sqlite3')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE Bangers(
    URL TEXT,
    Title TEXT,
    UserID INT,
    Date TEXT,
    Plays INT,
    UNIQUE (URL)
    );
    ''')

    cur.execute('''
    CREATE TABLE Users(
    UserID INT,
    Name TEXT,
    UNIQUE (UserID)
    );
    ''')

    cur.execute('''
    CREATE TABLE Quotes(
    Author TEXT,
    Quote TEXT);''')

    conn.commit()

    # Insert the Names
    insert_sql = '''INSERT INTO Users (
    UserID, Name)
    VALUES (?, ?)
    '''

    for i, name in enumerate(Names):
        cur.execute(insert_sql, (i, name))

    conn.commit()
    conn.close()

def loadFromText(textFile):
    '''Loads the list of bangers from the old text file.'''
    with open(textFile) as f:
        for banger in f.readlines():
            try:
                bangers.add_banger('add ' + banger, rand.randint(0, len(Names) + 1))
            except Exception as e:
                print(e)
                print('Banger already added')
