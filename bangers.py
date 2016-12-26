import random

def handle_response(text):
    '''Determines which function to call based on a message'''
    if ':add' in text.lower():
        return add_banger(text)
    elif 'count' in text.lower():
        return count()
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


def add_banger(text):
    '''
    Adds a banger to the text file.
    proper input would be "banger add:link"
    '''
    text = text.split('add:')[1].replace(' ', '')
    with open('bangers.txt', 'a') as f:
        f.write(text)

def count():
    '''Returns a count of the bangers'''
    bangers = load_bangers()
    return 'You have ' + str(len(bangers)) + ' bangers'


if __name__ == '__main__':
    print(select_banger())
    print(select_banger())
    print(select_banger())
    print(count())
