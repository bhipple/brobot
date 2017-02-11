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

    def test_rip(self):
        self.assertEqual("rip", runHandlers("rip"))
        self.assertEqual("rip", runHandlers("RIP"))

    def test_inspiration(self):
        self.assertEqual(nerdreply.INSPIRATION, runHandlers("factory?"))
        self.assertEqual(nerdreply.INSPIRATION, runHandlers("factorio?"))
        self.assertEqual(nerdreply.INSPIRATION, runHandlers("Stop horsing around man!"))
        self.assertEqual(nerdreply.INSPIRATION, runHandlers("Stop horswing around man!"))

    def test_d20_returns_strings(self):
        x = runHandlers("Yo give me a d20")
        self.assertTrue(isinstance(x, str))

    def test_d20_range(self):
        i = int(runHandlers("Yo give me a d20"))
        self.assertTrue(i >= 1 and i <= 20)

    def test_d20_priority(self):
        i = int(runHandlers("Yo nerdbot drop me a d20"))
        self.assertTrue(i >= 1 and i <= 20)

    def test_bahp(self):
        for key in ["bahp", "BAHP", "Bahp!"]:
            i = int(runHandlers(key))
            self.assertTrue(i >= 1 and i <= 20)

    def test_bitcoin(self):
        s = runHandlers("bitcoin plz")
        self.assertRegexpMatches(s, r"Bitcoin: \$[0-9,]*.[0-9]{2}")

        s = runHandlers("are we going to the mOON nerdbot?")
        self.assertRegexpMatches(s, r"To the moon! \$[0-9,]*.[0-9]{2}")


class TestBangers(unittest.TestCase):

    # Create the bangers file
    if bangers.bangersFile() not in os.listdir(os.getcwd()):
        initDatabase.createDB()
        bangers.loadFromText('test_bangers.txt')

    def test_default_bangers_file(self):
        os.environ['BANGERS_FILE'] = ''
        self.assertEqual('/home/brobot/brobot/brobotDB.sqlite3', bangers.bangersFile())
        os.environ['BANGERS_FILE'] = 'brobotDB.sqlite3'

    def test_override_bangers(self):
        self.assertEqual('brobotDB.sqlite3', bangers.bangersFile())

    def test_count(self):
        x = runHandlers("banger count")
        self.assertTrue("You have" in x)

    def test_lookupUserID(self):
        self.assertEqual(5, bangers.lookupUserId("ChrisH"))
        self.assertEqual(8, bangers.lookupUserId("MikeL"))

    def test_getBangerLowercase(self):
        x = runHandlers("Drop a banger")
        self.assertTrue("youtube" in x)

    def test_getBangerUppcercase(self):
        x = runHandlers("Drop a Banger")
        self.assertTrue("youtube" in x)

    def test_add_redundent(self):
        self.assertEqual("Failed to add banger.",
                bangers.addBanger('banger add https://www.youtube.com/watch?v=2HQaBWziYvY'))


class Rolloff(unittest.TestCase):
    def test_rolloff(self):
        output = runHandlers("rolloff Alex John Chris")
        self.assertTrue("Alex" in output)
        numBros = 3
        count = 0
        for line in output.split("\r\n"):
            self.assertTrue(int(line.split(" ")[1]) in range(1, 21))
            count += 1
        self.assertEqual(numBros, count)


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
