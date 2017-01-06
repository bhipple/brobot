import json
import urllib
import os
import requests

dskey = os.environ["DARKSKYKEY"]
lociq = "4257610dd0aadeaaece4"
locurl = "http://locationiq.org/v1/search.php?key="
locvar = "&limit=1&countrycodes=US&format=json&q="


text = raw_input()


def handle_response(text):
#    for text in text.lower():
#       return coord_get()
    for text in text.lower():   
       return weather()

def coord_get(): 
    r = requests.get(locurl + lociq + locvar + text )  
    parsed_json = json.loads(r.text)
    for i in parsed_json:

         print "DEBUG coord_get"
         return i['lat'], i['lon'], i['display_name']

def just_coord(): 
    r = requests.get(locurl + lociq + locvar + text )  
    parsed_json = json.loads(r.text)
    for i in parsed_json:
         print "DEBUG just_coord"
         return i['lat'] + ',' +  i['lon']


def weather():
    coord = str(just_coord())
    print "DEBUG weather"
    coord =  coord.translate(None, ' u()')
    url = "https://api.darksky.net/forecast/" + dskey + "/" + coord
    response = urllib.urlopen(url)
    parsed_json = json.loads(response.read())
    return(parsed_json['daily']['summary'])
    

print (handle_response(text))

#if __name__ == '__main__':
#    print(handle_response())
