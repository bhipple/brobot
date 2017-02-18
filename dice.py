import random
import re

def rollin(diceSize):
    return random.randint(1, diceSize)

def rollOff(text):
    '''Does a rolloff for the listed bros'''
    rolls = []
    for name in text.split()[1:]:
        rolls += [(rollin(20), name)]
    res = map(lambda (r, p): p + ": " + str(r), sorted(rolls, reverse=True))
    return "\r\n".join(res)

def parseDice(text):
    """matches xdy from input text and rolls that x dice of y size"""
    match = re.findall("[0-9]{0,50}d[0-9]{1,50}", text)
    # poor man's regex without matchgroups

    split = match[0].split("d")
    # If there's a number before the d, it reads it, else sets to 1
    try:
        numDice = int(split[0])
    except:
        numDice = 1

    diceSize = int(split[1])
    return numDice, diceSize

def rollDice(text):
    numDice, diceSize = parseDice(text)

    if numDice == 0 or diceSize == 0:
        return "No Dice!"

    rolls = [rollin(diceSize) for i in range(numDice)]
    total = sum(rolls)

    if numDice == 1:
        return total
    else:
        r = "Rolls: " + str(rolls)
        t = "Total: " + str(total)
        return r + "\r\n" + t
