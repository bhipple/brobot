import random

def rollin():
    return random.randint(1, 20)

def rollOff(text):
    '''Does a rolloff for the listed bros'''
    rolls = []
    for name in text.split()[1:]:
        rolls += [(rollin(), name)]
    res = map(lambda (r,p): p + ": " + str(r), sorted(rolls))
    return "\r\n".join(res)
