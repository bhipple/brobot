import json
import urllib
import os
import requests


dskey = os.environ["DARKSKYKEY"]
lociq = os.environ["LOCIQ"]
locurl = "http://locationiq.org/v1/search.php?key="
locvar = "&limit=1&countrycodes=US&format=json&q="
dskyurl = "https://api.darksky.net/forecast/"

#work in progress...

#def handle_response():
#    for text in text.lower():   
#       return weather()


def just_coord(): 
    r = requests.get(locurl + lociq + locvar + text )  
    parsed_json = json.loads(r.text)
    for i in parsed_json:
         print "DEBUG just_coord"
         print "DEGUG " +  i['lat'], i['lon'], i['display_name']
         return i['lat'] + ',' +  i['lon']


def weather():
    while True:    
        try:
            coord = str(just_coord())
            print "DEBUG weather"
            coord =  coord.translate(None, ' u()')
            url = dskyurl + dskey + "/" + coord
            response = urllib.urlopen(url)
            parsed_json = json.loads(response.read())
            return(parsed_json['daily']['summary'])
        except ValueError:
            return "Location not found, please use 'City, ST'"


#if __name__ == '__main__':
#    print(handle_response())
