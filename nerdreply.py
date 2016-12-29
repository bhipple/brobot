#!/usr/bin/python
import os
import random
import re
import bangers as bng
import pdb
from telnetlib import Telnet
from initDatabase import createDB

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
    tn.write("PRIVMSG " + fbchan + " :" + msg + "\n")

def cleanup(msg):
    return msg.split("PRIVMSG " + fbchan + " :")[1]

def grabName(msg):
    '''name is between the : and the ! on the match string.'''
    return msg.split(':')[1].split('!')[0]

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


    expressions = [".*nerd.*\r\n", ".*bang.*\r\n"]
    while True:
        (idx, match, output) = tn.expect(expressions)
        print "DEBUG: idx=" + str(idx)
        print "DEBUG: match=" + match.group(0)
        print "DEBUG: cleanedUp=" + cleanup(match.group(0))
        #print "DEBUG: output=" + output
        if idx == 0:
            sendMsg(tn, "nerd")
        if idx == 1:
            sendMsg(tn, bng.handle_response(cleanup(match.group(0)),
                                            grabName(match.group(0))))

if __name__ == '__main__':
    # Check to make sure database exists
    if 'iBangersBotDB.sqlite3' not in os.listdir(os.getcwd()):
        createDB()
        with open('bangers.txt') as f:
            for banger in f.readlines():
                try:
                    add_banger(banger, 5, False)
                except Exception as e:
                    print(e)
                    print('Banger already added')


    # Run the bot
    telnetMain()
