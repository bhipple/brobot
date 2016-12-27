import sqlite3

def createDB():
    '''Creates the Database, the tables, and fills in the user information.'''
    conn = sqlite3.connect('iBangersBotDB.sqlite3')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE Bangers(
    BangerID INT,
    Song TEXT,
    Artist TEXT,
    URL TEXT,
    UserID INT,
    Date TEXT,
    Plays INT,
    UNIQUE (BangerID, URL)
    );
    ''')

    cur.execute('''
    CREATE TABLE Users(
    UserID INT,
    Name TEXT,
    UNIQUE (UserID)
    );
    ''')

    conn.commit()

    # Insert the Names
    insert_sql = '''INSERT INTO Users (
    UserID, Name)
    VALUES (?, ?)
    '''
    Names = ['Adam', 'Alex', 'Austin', 'Ben', 'Chris B.', 'Chris H.', 'Jim',
            'John', 'Mike', 'Sean', 'Zach']
    for i, name in enumerate(Names):
        cur.execute(insert_sql, (i, name))

    conn.commit()
    conn.close()
