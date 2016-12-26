with open('bangers.txt') as f:
    bangers = f.readlines()
    bangers = [banger.replace('\n','') for banger in bangers]



def add_banger(text):
    '''
    Adds a banger to the text file.
    proper input would be "banger add:link"
    '''
    text = text.split('add:')[1]
    text.replace(' ', '')
    print(text)
    with open('bangers.txt', 'a') as f:
        f.write(text + '\n')


if __name__ == '__main__':
    # add_banger('add:https://www.youtube.com/watch?v=tlpcXYkJa9I')
    add_banger('add: https://www.youtube.com/watch?v=E0COe99xJnw')
