import json
import requests
import sys

if len(sys.argv) != 2 :
    print("system will exit, invalid input.")
    sys.exit()


request=requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+ sys.argv[1])
#print(json.dumps(request.json(), indent=2))
s=request.json()

for result in s["results"]:
    print(result["trackName"])

#i'd like things to be nicely intended and according to the documentation, so i pass in a named paramter of indetn, which will provide me with double spaces.(you can space however you want depending on the value u give to the indent.)

#json.dumbs() this one format the the json type files in a nice and more readable way.