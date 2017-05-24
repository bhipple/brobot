#!/usr/bin/python
import os
import nerdreply
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
from telnetlib import Telnet

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

        resp = nerdreply.processRequest(idx, cleaned)
        for r in resp.split("\r\n"):
            sendMsg(tn, r)


if __name__ == '__main__':
    telnetMain()
