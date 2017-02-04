import random

def rollin():
    roll = random.randint(1, 20)
    return str(roll)


# matchcase passes rolloff Ben Chris Alex
def rollOff(text):
    '''Does a rolloff for the listed bros'''
    result = ""
    for name in text.split()[1:]:
        result += name + " " + rollin() + "\r\n"
    return result
