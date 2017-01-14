import json
import urllib
import os

dskey = os.environ["DARKSKYKEY"]

#Need to fix check to if not nyc and not philly prompt again

def handle_response(text):
    if 'philly' in text.lower():
        return philly_weather()
    elif 'nyc' in text.lower():
        return nyc_weather()
    elif 'philly' or 'nyc' not in text.lower():
        print "philly or nyc?"
    else:
        return 


def philly_weather():

    url = "https://api.darksky.net/forecast/" + dskey + "/39.95,-75.16"
    response = urllib.urlopen(url)
    parsed_json = json.loads(response.read())
    
    return(parsed_json['daily']['summary'])

def nyc_weather():

    url = "https://api.darksky.net/forecast/" + dskey + "/40.7128,-74.0059"
    response = urllib.urlopen(url)
    parsed_json = json.loads(response.read())

    return(parsed_json['daily']['summary'])

if __name__ == '__main__':
    print(handle_response())
