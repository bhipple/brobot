#!/usr/bin/python
from ircbotbase import *
import os
import random
import bangers as bng

channel = "&bitlebee"
server = "localhost"
nickname = "brobot"
realname = "Bro"
regpass = os.environ["IRCPASSWORD"]

irc = IRC()
irc.connect(server, channel, nickname, realname, regpass)
 
while True:
    text = irc.get_text()
    print text
 
    if "PRIVMSG" in text and channel in text and "nerds" in text:
        irc.send(channel, "nerds")
    elif "PRIVMSG" in text and channel in text and "bang" in text.lower():
        irc.send(channel, bng.handle_response(text))

