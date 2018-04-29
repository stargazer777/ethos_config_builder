# Pull data from json source
import urllib2
import json
import ast

def poll_json(url, has_unicode):
    try:
        poller = urllib2.build_opener()
        poller.addheaders = [('User-Agent', 'Mozilla/5.0')]
        response = poller.open(url)
        data = json.loads(response.read())
    except:
        print("Unable to get URL: " + str(urllib2.HTTPError))
        exit(1)

    if has_unicode == True:
        # remove unicode
        data = ast.literal_eval(json.dumps(data))

    return data

