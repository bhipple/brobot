import random
import os

def bangersFile():
    return os.environ.get('BANGERS_FILE') or '/home/brobot/brobot/bangers.txt'

def select_banger():
    '''Returns a random banger from the bangers text file'''
    return random.choice(load_bangers())

def load_bangers():
    '''Loads the bangers from the text file'''
    with open(bangersFile()) as f:
        bangers = [banger.replace('\n', '') for banger in f.readlines()]
    return bangers

def add_banger(text):
    '''
    Adds a banger to the text file.
    proper input would be "add <link>"
    '''
    try:
        text = text.split('add')[1].replace(' ', '').strip()
        with open(bangersFile(), 'a') as f:
            f.write(text)
        return 'Successfully added banger'
    except:
        return "That didn't work"

def count():
    '''Returns a count of the bangers'''
    bangers = load_bangers()
    return 'You have ' + str(len(bangers)) + ' bangers'

def banger_help():
    '''Gives some quick help info for bangerBot'''
    return 'say something with banger to get a banger.  Say add <link> to add.'''
