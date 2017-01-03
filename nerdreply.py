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
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

channel = "&bitlebee"
nickname = os.environ["NICKNAME"]
username = os.environ["USER"]
realname = os.environ["REALNAME"]
regpass = os.environ["IRCPASSWORD"]
fbchan = os.environ["FBCHAN"]

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

    tn.write("NICK " + nickname +"\n")
    tn.write("USER " + username + " 8 *: " + realname + "\n")
    tn.read_until("identify yourself", 3)

    print "DEBUG: Joining bitlbee"
    tn.write("JOIN &bitlbee\n")
    tn.write("PRIVMSG &bitlbee :identify " + regpass + "\n")
    tn.read_until("facebook - Logging in: Logged in", 3)

    print "DEBUG: Joining channel"
    tn.write("JOIN " + fbchan + "\n")

    print "DEBUG: Telnetmain finished"

    expressions = [".*nerd.*\r\n", ".*bang.*\r\n", ".*philly*.\r\n", ".*nyc*.\r\n", ".*dale.*\r\n"]
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
<<<<<<< HEAD
            sendMsg(tn, "daaaale")
=======
            sendMsg(tn, "daaale")
>>>>>>> 540599105c2484c37211d1307f10fa9a0961dff5

if __name__ == '__main__':
    telnetMain()
