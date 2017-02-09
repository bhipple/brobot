import random
import re

def rollin():
    return random.randint(1, 20)

def rollOff(text):
    '''Does a rolloff for the listed bros'''
    rolls = []
    for name in text.split()[1:]:
        rolls += [(rollin(), name)]
    res = map(lambda (r, p): p + ": " + str(r), sorted(rolls, reverse=True))
    return "\r\n".join(res)


def rollDice(text):
    """matches xdy from input text and rolls that x dice of y size"""
    match = re.match("?P([0-9])(d[0-9])", text)
    return match.group(0)


if __name__ == "__main__":
    print(rollDice("2d6"))
