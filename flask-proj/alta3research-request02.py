import json
import requests

url = "http://127.0.0.1:3333/the-truth"

resp = requests.get(url).json()

for goat in resp.keys():
    if resp[goat].get('up_there') == True:
        print('\n', goat, 'is one of the greatest bands of all time, they have', resp[goat].get('numberOnes'), 'number one hit singles!')
    
