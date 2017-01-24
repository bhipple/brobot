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

    def test_d20(self):
        x = runHandlers("Yo give me a d20")
        self.assertTrue(isinstance(x, str))
        i = int(x)
        self.assertTrue(i >= 0 and i <= 20)

        x = runHandlers("Yo nerdbot drop me a d20")
        self.assertTrue(isinstance(x, str))
        i = int(x)
        self.assertTrue(i >= 0 and i <= 20)

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
        if os.environ["DARKSKYKEY"] == "Test" or os.environ["LOCIQ"] == "Test":
            print "Export a valid DARKSKYKEY and LOCIQ in order to run the weather tests."
            return

        print runHandlers('!forecast "new york, ny"')
        print runHandlers('!forecast "philadelphia, pa"')
        print runHandlers('!forecast "boston"')
        print runHandlers('!forecast "levittown, pa"')


if __name__ == "__main__":
    unittest.main()
