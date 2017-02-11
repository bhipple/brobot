#!/usr/bin/python
import bangers
import currency
import weather
import sys
import codecs
import dice
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

INSPIRATION = "When you're out there...partying...horswing around...someone out there at the same time is working hard. Someone is getting smarter and someone is winning, just remember that!"

class Handler():
    def __init__(self, r, f):
        self.regex = r
        self.func = f

# For every regular expression that can match, attach a function to handle the
# business logic. Note that while some functions do not require an argument,
# it's simpler to just pass the unused message in.
def handlers():
    return [ Handler(r"(?i).*(bitcoin|to the moon).*\r\n", lambda m: currency.bitcoinValue(m))
           , Handler(r"(?i).*d20.*\r\n", lambda m: str(dice.rollin()))
           , Handler(r"(?i).*bahp.*\r\n", lambda m: str(dice.rollin()))
           , Handler(r"(?i).*nerd.*\r\n", lambda m: "nerd")
           , Handler(r"(?i).*dale.*\r\n", lambda m: "daaale")
           , Handler(r"(?i).*rip.*\r\n", lambda m: "rip")
           , Handler(r"(?i).*(horsw?ing around|factor[iy]).*\r\n", lambda m: INSPIRATION)

           # Weather
           , Handler(".*!forecast.*\r\n", lambda m: weather.encoding(m))

           # Droppin' bangers
           , Handler(".*[Bb]anger count.*\r\n", lambda m: bangers.count())
           , Handler(".*[Bb]anger add https.*\r\n", lambda m: bangers.addBanger(m))
           , Handler(".*[Bb]anger help.*\r\n", lambda m: bangers.bangerHelp())
           # Since this is a default, it has to be after the other banger cmds
           , Handler(".*[Bb]anger.*\r\n", lambda m: bangers.selectBanger())

           , Handler(".*[Rr]olloff.*\r\n", lambda m: dice.rollOff(m))
           ]

def regexes():
    return list(map(lambda h: h.regex, handlers()))

def processRequest(idx, inp):
    return handlers()[idx].func(inp)
