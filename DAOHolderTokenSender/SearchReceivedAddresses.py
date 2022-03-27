import requests
import json
import os
import sys

tokenaddress = input("Please enter the whitelist token address (REQUIRED):")

if (len(tokenaddress) != 44):
    sys.exit('\n !!! Ensure this is a valid token address. They are 44 chars long... !!!\n')

AllAddressFile = "gib-holders.json"
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
