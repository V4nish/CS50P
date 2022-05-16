# JSON = JavaScript Object Notation

import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()

for result in o["results"]:        # Notice case matches raw JSON
    print(result["trackName"])     # Notice case matches raw JSON
