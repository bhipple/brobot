import json
import urllib
import os
import re
import requests
import codecs


dskey = os.environ["DARKSKYKEY"]
lociq = os.environ["LOCIQ"]
locurl = "http://locationiq.org/v1/search.php?key="
locvar = "&limit=1&countrycodes=US&format=json&q="
dskyurl = "https://api.darksky.net/forecast/"


def encoding(text):
    json = weather(text).encode('utf-8')
    return json

def just_coord(text):
    text = re.findall(r'"([^"]*)"', text)
    text = str(text)
    text = text.translate(None, " ['] ")
    r = requests.get(locurl + lociq + locvar + text)
    parsed_json = json.loads(r.text)
    for i in parsed_json:
         return i['lat'] + ',' +  i['lon']

def weather(text): 
        try:    
            coord = str(just_coord(text)) 
            coord =  coord.translate(None, ' u()')
            url = dskyurl + dskey + "/" + coord
            response = urllib.urlopen(url)
            parsed_json = json.loads(response.read())
            return (parsed_json['daily']['summary'])
        except ValueError:
            return 'Please use format: "City, St"'



