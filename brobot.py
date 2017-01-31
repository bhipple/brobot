#!/usr/bin/python
import os
import random
import re
import bangers
import weather
import nerdreply
import initDatabase
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
import pdb
import nerdreply
from telnetlib import Telnet
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

# Configuration
channel = "&bitlebee"
nickname = os.environ["NICKNAME"]
username = os.environ["USER"]
realname = os.environ["REALNAME"]
regpass = os.environ["IRCPASSWORD"]
fbchan = os.environ["FBCHAN"]
dskey = os.environ["DARKSKYKEY"]


def sendMsg(tn, msg):
    if not msg:
        return
    print("DEBUG: Sending msg=" + msg)
    tn.write(("PRIVMSG " + fbchan + " :" + msg + "\n").encode('utf-8'))

def cleanup(msg):
    return msg.split("PRIVMSG " + fbchan + " :")[1]

def telnetMain():
    print("DEBUG: Opening telnet handle")
    tn = Telnet("localhost", 6667)
    tn.set_debuglevel(5)
    tn.read_until("BitlBee-IRCd initialized, please go on")

    tn.write("NICK " + nickname + "\n")
    tn.write("USER " + username + " 8 *: " + realname + "\n")
    tn.read_until("identify yourself", 3)

    print("DEBUG: Joining bitlbee")
    tn.write("JOIN &bitlbee\n")
    tn.write("PRIVMSG &bitlbee :identify " + regpass + "\n")
    tn.read_until("facebook - Logging in: Logged in", 3)

    print("DEBUG: Joining channel")
    tn.write("JOIN " + fbchan + "\n")

    print("DEBUG: Telnetmain finished")
    regexes = nerdreply.regexes()
    while True:
        (idx, match, output) = tn.expect(regexes)
        print("DEBUG: idx=" + str(idx))
        print("DEBUG: match=" + match.group(0))
        cleaned = cleanup(match.group(0))
        print("DEBUG: cleanedUp=" + cleaned)

        sendMsg(tn, nerdreply.processRequest(idx, [cleaned, match.group(0)]))

if __name__ == '__main__':
    if bangersFile() not in os.listdir(os.getcwd()):
        initDatabase.createDB()
        initDatabase.loadFromText('test_bangers.txt')
        initDatabase.loadFromText('bangers.txt')
        sendMsg(tn, nerdreply.processRequest(idx, cleaned))
