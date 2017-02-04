import dice
import random as rand

# matchcase passes rolloff Ben Chris Alex

def rollOff(text):
    '''Does a rolloff for the listed bros'''
    result = ""
    for name in text.split(" ")[1:]:
        result += name + " " + dice.rollin() + "\n"
    return result[0:-1]  # Remove the last newline char

if __name__ == "__main__":
    print(rollOff("rolloff Ben Chris Alex"))
    print("-----")
    print(rollOff("rolloff Austin Zach Jim"))
