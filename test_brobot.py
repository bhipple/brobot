#!/usr/bin/env python
import os
os.environ["DARKSKYKEY"] = os.getenv("DARKSKYKEY", "Test")
os.environ["NICKNAME"] = "Test"
os.environ["REALNAME"] = "Test"
os.environ["NICKNAME"] = "Test"
os.environ["USER"] = "Test"
os.environ["REALNAME"] = "Test"
os.environ["IRCPASSWORD"] = "Test"
os.environ["FBCHAN"] = "Test"
os.environ["BANGERS_FILE"] = "brobotDB.sqlite3"
os.environ["LOCIQ"] = "Test"

import unittest
import bangers
import nerdreply
# import weather
import re
import initDatabase

requiredEnv = ["BANGERS_FILE"
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
    os.environ["BANGERS_FILE"] = "brobotDB.sqlite3"
    map(setDefaultEnv, requiredEnv)

initEnv()

import codecs
import sys
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

# Helper function to run all handlers in order against an input msg
# Behaves identically to how the telnet listener will behave.

def runHandlers(msg, hndlrs=nerdreply.handlers()):
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

    # Create the bangers file
    if bangers.bangersFile() not in os.listdir(os.getcwd()):
        initDatabase.createDB()

        with open('test_bangers.txt') as f:
            for banger in f.readlines():
                try:
                    banger.add_banger('add ' + banger, 5)
                except Exception as e:
                    print(e)
                    print('Banger already added')

    def test_default_bangers_file(self):
        os.environ['BANGERS_FILE'] = ''
        self.assertEqual('/home/brobot/brobot/brobotDB.sqlite3', bangers.bangersFile())
        os.environ['BANGERS_FILE'] = 'brobotDB.sqlite3'

    def test_override_bangers(self):
        self.assertEqual('brobotDB.sqlite3', bangers.bangersFile())

    def test_d20(self):
        x = runHandlers("Yo give me a d20")
        self.assertTrue(isinstance(x, str))
        i = int(x)
        self.assertTrue(i >= 0 and i <= 20)

        x = runHandlers("Yo nerdbot drop me a d20")
        self.assertTrue(isinstance(x, str))
        i = int(x)
        self.assertTrue(i >= 0 and i <= 20)

    def test_count(self):
        self.assertTrue("You have" in bangers.count())

    def test_lookupUserID(self):
        self.assertEqual(5, bangers.lookup_userID("ChrisH"))
        self.assertEqual(8, bangers.lookup_userID("MikeL"))

    def test_getBanger(self):
        self.assertTrue('youtube' in bangers.select_banger())

    def test_add_redundent(self):
        self.assertEqual("Failed to add banger.",
                bangers.add_banger('banger add https://www.youtube.com/watch?v=ifi6SqAAH7s'))

class TestWeather(unittest.TestCase):
    def test_weather(self):
        if os.environ["DARKSKYKEY"] == "Test" or os.environ["LOCIQ"] == "Test":
            print("Export a valid DARKSKYKEY and LOCIQ in order to run the weather tests.")
            return

            print(runHandlers('!forecast "new york, ny"'))
            print(runHandlers('!forecast "philadelphia, pa"'))
            print(runHandlers('!forecast "boston"'))
            print(runHandlers('!forecast "levittown, pa"'))


if __name__ == "__main__":
    unittest.main()
