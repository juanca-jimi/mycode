#!/usr/bin/env python3

import requests
from pprint import pprint

url = "http://127.0.0.1:2224/"

resp = requests.get(url).json()

pprint(resp)
