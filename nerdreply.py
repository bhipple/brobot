#!/usr/bin/python
import bangers
import weather
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

INSPIRATION = "When you're out there...partying...horswing around...someone out there at the same time is working hard. Someone is getting smarter and someone is winning, just remember that!"

class Handler():
    def __init__(self, r, f):
        self.regex = r
        self.func = f

# For every regular expression that can match, attach a function to handle the
# business logic. Note that while some functions do not require an argument,
# it's simpler to just pass the unused message in.
def handlers():
    return [ Handler(".*[Nn]erd.*\r\n", lambda m: "nerd")
           , Handler(".*[Dd]ale.*\r\n", lambda m: "daaale")
           , Handler(".*(horsw?ing around|factor[iy]).*\r\n", lambda m: INSPIRATION)

           # Weather currently disabled due to UTF-8 issues.
           , Handler(".*!forecast.*\r\n", lambda m: weather.encoding(m))


           , Handler(".*banger count.*\r\n", lambda m: bangers.count())
           , Handler(".*banger add https.*\r\n", lambda m: bangers.add_banger(m))
           , Handler(".*banger help.*\r\n", lambda m: bangers.banger_help())

           # Since this is a default, it has to be after the other banger cmds
           , Handler(".*banger.*\r\n", lambda m: bangers.select_banger())
           ]

def regexes():
    return map(lambda h: h.regex, handlers())

def processRequest(idx, inp):
    return handlers()[idx].func(inp)
