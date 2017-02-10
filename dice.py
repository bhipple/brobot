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
    match = re.findall("[0-9]{0,50}d[0-9]{0,50}", text)
    # poor man's regex without matchgroups

    split = match[0].split("d")
    numDice = int(split[0])
    diceSize = int(split[1])

    rolls = [random.randint(1,diceSize) for i in range(numDice)]
    total = sum(rolls)

    return total, rolls


if __name__ == "__main__":
    roll = rollDice("d6")
    print(roll[0])
    print(roll[1])
