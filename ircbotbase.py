import socket
import sys
 
 
class IRC:
 
    irc = socket.socket()
  
    def __init__(self):  
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    def send(self, chan, msg):
        self.irc.send("PRIVMSG " + chan + " " + msg + "n")
 
    def connect(self, server, channel, botnick, realname, regpass):
        #defines the socket
        print "connecting to:"+server
        self.irc.connect((server, 6667))                                                         #connects to the server
        self.irc.send("USER " + botnick + " 8 *: " + realname + " :This is a fun bot!n") #user authentication
        self.irc.send("NICK" + botnick + "n")               
        self.irc.send("JOIN" + channel + "n")        #join the chan
	self.irc.send("PRIVMSG " + channel + " :identify " + regpass + "n")  
	
 
    def get_text(self):
        text=self.irc.recv(2040)  #receive the text
# ping/pong disabled in /etc/bitlbee/bitlbee.conf 
#        if text.find('PING') != -1:                      
#           self.irc.send('PONG ' + text.split() [1] + 'rn') 
 
        return text
