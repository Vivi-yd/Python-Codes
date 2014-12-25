import json
import requests

def pretty_print(data, indent=4):
    """
    prints a python dictionary in more readable indented format.
    The default indent levels is set at four.
    """
    if type(data) == dict:
        return json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data

def api_get_request(url):
    """
    In this exercise, you want to call the last.fm API to get a list of the
    top artists in Spain.
    
    Once you've done this, return the name of the number 1 top artist in Spain.
    """
    
    # this url specifically access data from website, pinpointing Spain as country.
    url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=c0871d3a08f3a1a3525b9e2c3dd2ecd7&format=json'
    
    
    # extract data from url and assign it to variable named "data".
    data = requests.get(url).text
    
    # convert data to python dict format in order to be able to access data with keys.
    data = json.loads(data)
    
    # better readability
    pretty_print(data)
    
    # extract wanted info by penatrating multi-level dict in the data
    # index zero because topartist ranked first
    topartist_spain = data['topartists']['artist'][0]['name']

    # return the top artist in Spain
    return topartist_spain