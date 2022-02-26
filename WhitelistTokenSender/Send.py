from asyncio.windows_events import NULL
import os
import json
import sys, getopt

receivedFile = "cache/Live Received Addresses.txt"
mentionsAddressFile = "AllUsernamesAddresses.json"
outfile = "cache/AddressesToSend.json"

tokenaddress = sys.argv[1]
amountToSend = sys.argv[2]
        
print (tokenaddress + "  -  " + amountToSend)

with open(receivedFile, "r") as received:
    lines = received.readlines()

loadedReceived = []
for line in lines:
    loadedReceived.append(line.strip('\n'))

addressesToSend = []

with open(mentionsAddressFile, 'r', encoding='utf8') as jsonfile:
	json_load = json.load(jsonfile)

for x in json_load:
    if (x['address'] not in loadedReceived):
        addressesToSend.append({"mention": x['mention'], "address": x['address']})

with open(outfile, "w+") as un:
    json.dump(addressesToSend, un)

if (len(tokenaddress) != 44):
    print("\n !!! Ensure this is a token address. They are 44 chars long... This error may depreciate.  !!!\n")
    sys.exit(2)

with open(outfile) as data_file:    
    data = json.load(data_file)
    for x in data:
        # By default, this sends a token and funds creating the token account in the receiving account
        # but does not send the token if the receiving has 0 SOL in their wallet.
        os.system(f"spl-token transfer --fund-recipient {tokenaddress} {amountToSend} {x['address']}")
        
        # To send tokens and allow for wallets with 0 SOL. Comment out the above and uncomment
        # below:
        # os.system(f"spl-token transfer --fund-recipient --allow-unfunded-recipient {tokenaddress} {amountToSend} {x['address']}")