import random
import re

def rollin():
    return random.randint(1, 20)

def rollOff(text):
    '''Does a rolloff for the listed bros'''
    rolls = []
    for name in text.split()[1:]:
        rolls += [(rollDice("d20"), name)]
    res = map(lambda (r, p): p + ": " + str(r), sorted(rolls, reverse=True))
    return "\r\n".join(res)


def rollDice(text):
    """matches xdy from input text and rolls that x dice of y size"""
    match = re.findall("[0-9]{0,50}d[1-9]{1,50}", text)
    # poor man's regex without matchgroups

    split = match[0].split("d")
    # If there's a number before the d, it reads it, else sets to 1
    try:
        numDice = int(split[0])
    except:
        numDice = 1
    diceSize = int(split[1])

    rolls = [random.randint(1, diceSize) for i in range(numDice)]
    total = sum(rolls)

    # Backwards compatible with old roller
    if numDice == 1:
        return total
    elif numDice == 0:
        return "No Dice!"
    else:
        res = "Total: " + str(total) + "\r\n" + "Rolls were:" + str(rolls)
        return res
    return total, rolls

if __name__ == "__main__":
    print(rollDice("1d6"))
