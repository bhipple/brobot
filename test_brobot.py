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
os.environ["BANGERS_FILE"] = "test_bangers.txt"

import unittest
import brobot
import bangers
import nerdreply
import weather

import codecs
import sys
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

class TestNerdreply(unittest.TestCase):
    def test_regex_list(self):
        r = nerdreply.regexes()
        self.assertEqual(".*nerd.*\r\n", r[0])

    def test_lambda_lookup_works(self):
        hndlrs = nerdreply.handlers()
        self.assertEqual("nerd", hndlrs[0].func("unused"))

class TestBangers(unittest.TestCase):
    def test_default_bangers_file(self):
        os.environ['BANGERS_FILE'] = ''
        self.assertEqual('/home/brobot/iBangersBot/bangers.txt', bangers.bangersFile())
        os.environ['BANGERS_FILE'] = 'test_bangers.txt'

    def test_override_bangers(self):
        self.assertEqual('test_bangers.txt', bangers.bangersFile())

    def test_count(self):
        self.assertEqual("You have 2 bangers", bangers.count())

class TestWeather(unittest.TestCase):
    def test_nyc(self):
        print "\nWeather in NYC: " + weather.nyc_weather()

if __name__ == "__main__":
    unittest.main()
