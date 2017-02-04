#!/usr/bin/python
import bangers
import weather
import sys
import codecs
import dice
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


# Python2 garbage
# sys.setdefaultencoding("utf-8")

INSPIRATION = "When you're out there...partying...horswing around...someone out there at the same time is working hard. Someone is getting smarter and someone is winning, just remember that!"

class Handler():
    def __init__(self, r, f):
        self.regex = r
        self.func = f

# For every regular expression that can match, attach a function to handle the
# business logic. Note that while some functions do not require an argument,
# it's simpler to just pass the unused message in.
def handlers():
    return [ Handler(".*[Dd]20.*\r\n", lambda m: dice.rollin())
           , Handler(".*[Nn]erd.*\r\n", lambda m: "nerd")
           , Handler(".*[Dd]ale.*\r\n", lambda m: "daaale")
           , Handler(".*(horsw?ing around|factor[iy]).*\r\n", lambda m: INSPIRATION)

           # Weather currently disabled due to UTF-8 issues.
           # , Handler(".*philly*.\r\n", lambda m: weather.philly_weather())
           # , Handler(".*nyc*.\r\n", lambda m: weather.nyc_weather())
           , Handler(".*!forecast.*\r\n", lambda m: weather.encoding(m))

           # Droppin' bangers
           , Handler(".*[Bb]anger count.*\r\n", lambda m: bangers.count())
           , Handler(".*[Bb]anger add https.*\r\n", lambda m: bangers.add_banger(m))
           , Handler(".*[Bb]anger help.*\r\n", lambda m: bangers.banger_help())
           # Since this is a default, it has to be after the other banger cmds
           , Handler(".*[Bb]anger.*\r\n", lambda m: bangers.select_banger())
           , Handler(".*[Rr]olloff.*\r\n", lambda m: dice.rollOff(m))
           ]

def regexes():
    return list(map(lambda h: h.regex, handlers()))

def processRequest(idx, inp):
    return handlers()[idx].func(inp)
