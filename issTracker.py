import requests

URL = "http://api.open-notify.org/iss-now.json"

issInfo = requests.get(URL).json()

print('current location of the iss is:')

print(issInfo['iss_position'])

