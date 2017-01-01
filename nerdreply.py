#!/usr/bin/python
import os
import random
import re
import bangers as bng
import weather as wthr
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
import pdb
from telnetlib import Telnet

channel = "&bitlebee"
nickname = "brobot"
realname = "Bro"
regpass = os.environ["IRCPASSWORD"]
fbchan = "#the"

def sendMsg(tn, msg):
    if not msg:
        return
    print "DEBUG: Sending msg=" + msg
    tn.write(("PRIVMSG " + fbchan + " :" + msg + "\n").encode('utf-8'))

def cleanup(msg):
    return msg.split("PRIVMSG " + fbchan + " :")[1]

def telnetMain():
    print "DEBUG: Opening telnet handle"
    tn = Telnet("localhost", 6667)
    tn.set_debuglevel(5)
    tn.read_until("BitlBee-IRCd initialized, please go on")

    tn.write("NICK brobot\n")
    tn.write("USER brobot 8 *: Alex\n")
    tn.read_until("identify yourself", 3)

    print "DEBUG: Joining bitlbee"
    tn.write("JOIN &bitlbee\n")
    tn.write("PRIVMSG &bitlbee :identify " + regpass + "\n")
    tn.read_until("facebook - Logging in: Logged in", 3)

    print "DEBUG: Joining channel"
    tn.write("JOIN " + fbchan + "\n")

    print "DEBUG: Telnetmain finished"

    expressions = [".*nerd.*\r\n", ".*bang.*\r\n", ".*philly*.\r\n", ".*nyc*.\r\n", ".dale.*\r\n"]
    while True:
        (idx, match, output) = tn.expect(expressions)
        print "DEBUG: idx=" + str(idx)
        print "DEBUG: match=" + match.group(0)
        print "DEBUG: cleanedUp=" + cleanup(match.group(0))
        #print "DEBUG: output=" + output
        if idx == 0:
            sendMsg(tn, "nerd")
        if idx == 1:
            sendMsg(tn, bng.handle_response(cleanup(match.group(0))))
        if idx == 2 or idx == 3:
            sendMsg(tn, wthr.handle_response(cleanup(match.group(0))))
        if idx == 4:
            sendMsg(tn, "daaale")

if __name__ == '__main__':
    telnetMain()
