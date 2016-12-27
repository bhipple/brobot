import json
import urllib


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
    url = "https://api.darksky.net/forecast/c1f5c11e353be5c7d8783190719a37c1/39.9526,-75.1652"
    response = urllib.urlopen(url)
    parsed_json = json.loads(response.read())
    
    return(parsed_json['daily']['summary'])

def nyc_weather():
    url = "https://api.darksky.net/forecast/c1f5c11e353be5c7d8783190719a37c1/40.7128,-74.0059"
    response = urllib.urlopen(url)
    parsed_json = json.loads(response.read())

    return(parsed_json['daily']['summary'])

if __name__ == '__main__':
    print(handle_response())
