import json
import urllib
import os

DSKEY = os.environ["DARKSKYKEY"]

def lookupCoords(gps):
    try:
        url = "https://api.darksky.net/forecast/" + DSKEY + "/" + gps
        print url
        response = urllib.urlopen(url)
        parsed_json = json.loads(response.read())
        return(parsed_json['daily']['summary'])
    except:
        return "Failed to lookup weather"

def philly_weather():
    return lookupCoords("39.95,-75.16")

def nyc_weather():
    return lookupCoords("40.7128,-74.0059")
