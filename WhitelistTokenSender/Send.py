######################################################################################################
# Title: Whitelist Token Sender                                                                      #
# Author: Dean Overton                                                                               #
# Github : https://github.com/Dean-Overton                                                           #
######################################################################################################

print (""" 
        ███████╗ █████╗ ██╗  ██╗███████╗
        ██╔════╝██╔══██╗██║ ██╔╝██╔════╝
        ███████╗███████║█████╔╝ ███████╗
        ╚════██║██╔══██║██╔═██╗ ╚════██║
        ███████║██║  ██║██║  ██╗███████║
        ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝                                                                                                                                                                                                   
                                                                            
                   Dean Overton
https://github.com/Dean-Overton/solana-discord-nft-tools

""")

from asyncio.windows_events import NULL
import os
import json
import sys, getopt

receivedFile = "cache/Live Received Addresses.txt"
mentionsAddressFile = "AllUsernamesAddresses.json"
outfile = "cache/AddressesToSend.json"

tokenaddress = input("Please enter the whitelist token address (REQUIRED):")

if (len(tokenaddress) != 44):
    sys.exit('\n !!! Ensure this is a valid token address. They are 44 chars long... !!!\n')

amountInput = input("Enter the AMOUNT of whitelist tokens to send to each address (Default: 1):")
if amountInput != "":
    amountToSend = int(amountInput)
else:
    amountToSend = 1
if (amountToSend < 0):
    sys.exit('Amount must be bigger than zero.')
    

print (f"Sending {amountToSend} {tokenaddress} tokens to each reciever.")

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

with open(outfile) as data_file:    
    data = json.load(data_file)
    for x in data:
        # By default, this sends a token and funds creating the token account in the receiving account
        # but does not send the token if the receiving has 0 SOL in their wallet.
        #os.system(f"spl-token transfer --fund-recipient {tokenaddress} {amountToSend} {x['address']}")
        #print (x)
        # To send tokens and allow for wallets with 0 SOL. Comment out the above and uncomment
        # below:
        os.system(f"spl-token transfer --fund-recipient --allow-unfunded-recipient {tokenaddress} {amountToSend} {x['address']}")