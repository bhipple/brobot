#!/usr/bin/env python
import os

requiredEnv = [
      "BANGERS_FILE"
    , "DARKSKYKEY"
    , "FBCHAN"
    , "IRCPASSWORD"
    , "LOCIQ"
    , "NICKNAME"
    , "REALNAME"
    , "USER"
]

def setDefaultEnv(k):
    os.environ[k] = os.getenv(k, "Test")

def initEnv():
    os.environ["BANGERS_FILE"] = "test_bangers.txt"
    map(setDefaultEnv, requiredEnv)

initEnv()
import unittest
import bangers
import nerdreply
import re
import weather
import dice
import codecs
import sys
sys.stdout = codecs.getwriter('utf8')(sys.stdout)


# Helper function to run all handlers in order against an input msg
# Behaves identically to how the telnet listener will behave.
def runHandlers(msg, hndlrs = nerdreply.handlers()):
    msg += "\r\n"
    for h in hndlrs:
        if re.match(h.regex, msg):
            return h.func(msg)

class TestNerdreply(unittest.TestCase):
    def test_regex_list(self):
        r = nerdreply.regexes()
        self.assertEqual(".*[Nn]erd.*\r\n", r[0])

    def test_lambda_lookup_works(self):
        hndlrs = nerdreply.handlers()
        self.assertEqual("nerd", hndlrs[0].func("unused"))

    def test_none(self):
        self.assertEqual(None, runHandlers("This does not match anything."))

    def test_nerd_case_insensitive(self):
        self.assertEqual("nerd", runHandlers("I see a Nerd in here"))
        self.assertEqual("nerd", runHandlers("I see a nerd in here"))

    def test_inspiration(self):
        self.assertEqual(nerdreply.INSPIRATION, runHandlers("factory?"))
        self.assertEqual(nerdreply.INSPIRATION, runHandlers("factorio?"))
        self.assertEqual(nerdreply.INSPIRATION, runHandlers("Stop horsing around man!"))
        self.assertEqual(nerdreply.INSPIRATION, runHandlers("Stop horswing around man!"))


class TestBangers(unittest.TestCase):
    def test_default_bangers_file(self):
        os.environ['BANGERS_FILE'] = ''
        self.assertEqual('/home/brobot/brobot/bangers.txt', bangers.bangersFile())
        os.environ['BANGERS_FILE'] = 'test_bangers.txt'

    def test_override_bangers(self):
        self.assertEqual('test_bangers.txt', bangers.bangersFile())

    def test_count(self):
        self.assertEqual("You have 2 bangers", bangers.count())

class TestWeather(unittest.TestCase):
    def test_weather(self):
        if os.environ["DARKSKYKEY"] == "Test":
            print "Export a valid DARKSKYKEY in order to run the weather tests."
            return
        print weather.encoding('!forecast "new york, ny')
        print weather.encoding('!forecast nyc')
        print weather.weather('!forecast "philadelphia, pa"')
        print weather.encoding('!forecast "philadelphia, pa"')
        print weather.encoding('!forecast "boston"')
        print weather.ecoding("!forecast levittown, pa").encode('utf-8')

class TestD20(unittest.TestCase):
        print dice.rollin('!d20')

if __name__ == "__main__":
    unittest.main()
