# iBangersBot
Drops bangers from Youtube into your favorite messenger platform via bitlbee irc.

To use:
* Setup bitlbee and configure it to connect to facebook
* export IRCPASSWORD with the bitlbee identify password
* export DARKSKYKEY with the DarkSky API key
* Start nerdreply.py



You'll need a Facebook user profile for the bot. If a phone number is needed to complete the Facebook signup a Google voice number will suffice. Under Settings > Security you can generate an app password. This will allow you to connect to Facebook without using your account password. 


## Installation

```
apt-get update
apt-get upgrade
```

Add jgeboski(insert version), nightly, and backport repos

```
deb http://download.opensuse.org/repositories/home:/jgeboski/<version> ./
deb http://code.bitlbee.org/debian/master/jessie/amd64/ ./
deb http://ftp.debian.org/debian jessie-backports main
```

```
apt-get update
apt-get install irssi bitlbee bitlebee-dev bitlbee-libpurble bitlbee-facebook
```
In /etc/bitlbee/bitlbee.conf set the following 

```
RunMode = ForkDaemon

DaemonInterface = 127.0.0.1
DaemonPort = 6667

PingInterval = 0
PingTimeOut = 0
```

Start bitlbee & irssi

```
systemctl start bitlbee.service
systemctl start irssi
```

Irssi is just used to simplify creating the account and joining channels

```
irssi
/connect localhost
#alt+2 to change to &bitlbee
register <password>
identify <password>
account add facebook <email> <app password>
account facebook on

#list fbchats 
fbchat list
fbjoin facebook <ID> <channel>
account facebook set mark_read true
account facebook set mark_reply true
account facebook set show_unread false
account facebook set group_chat_open true
```




## Further Reference:
* https://jgeboski.github.io/#debian-and-ubuntu
* https://wiki.bitlbee.org/Packages
* https://wiki.bitlbee.org/ChangingPasswords
* https://darksky.net/dev/

