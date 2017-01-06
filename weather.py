import json
import urllib
import os
import requests
import subprocess

dskey = os.environ["DARKSKYKEY"]
lociq = os.environ["LOCIQ"]
locurl = "http://locationiq.org/v1/search.php?key="
locvar = "&limit=1&countrycodes=US&format=json&q="


def handle_response(text):
    if 'forecast' in text.lower():
       return weather()
    elif 'help' in text.lower():
       return weather_help()

def just_coord(): 
    text = text.split('forecast')[1].replace(' ', '').strip()
    r = requests.get(locurl + lociq + locvar + text )  
    parsed_json = json.loads(r.text)
    for i in parsed_json:
         return i['lat'] + ',' +  i['lon']

def weather():
    coord = str(just_coord())
    print "DEBUG weather"
    coord =  coord.translate(None, ' u()')
    url = "https://api.darksky.net/forecast/" + dskey + "/" + coord
    response = urllib.urlopen(url)
    parsed_json = json.loads(response.read())
    return(parsed_json['daily']['summary'])

def weather_help():
    return 'Please use the format "forecast city"'


if __name__ == '__main__':
    print(handle_response())
