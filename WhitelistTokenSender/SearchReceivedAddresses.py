import requests
import json
import os
import sys

tokenaddress = sys.argv[1]

AllAddressFile = "AllUsernamesAddresses.json"
realReceived = "cache/Live Received Addresses.txt"

with open(AllAddressFile, 'r', encoding='utf8') as jsonfile:
	address = json.load(jsonfile)

payload = {'tokenAddress': tokenaddress, 'offset': '0', 'limit': f'{len(address)}'}
r = requests.get('https://public-api.solscan.io/token/holders', params=payload)

try:
    os.makedirs('cache')
except OSError:
    pass # already exists

with open (realReceived, 'w+') as new:
    for x in r.json()['data']:
        new.write(x['owner'] + "\n")
