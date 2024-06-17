import requests
import sys

if len(sys.argv) != 2 :
    print("system will exit, invalid input.")
    sys.exit()
request=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+ sys.argv[1])
print(request.json())

#what we are seeing here is that this has been standarized  as a python dictionary what indeed apple's returning is a JSON response (JavaScript Object Notation) but python, the requests library is converting it to a python dictionary which happens to use wonderfully concidentaly almost the same syntax. It uses curly curly braces { to represent the dictionary and a close curly brace to represent the ending }, for any lists therein it uses square bracket [ and a close square bracket].

#we have a double quotes/single quote to represent the keys in the dictionary and after a colong it represents the value of that key 'resultCount': 1

#same goes for results, but in results; the value is the entire list of data, very long.