from asyncio.windows_events import NULL
from lib2to3.pgen2 import token
import os
import json
import sys, getopt

receivedFile = "cache/Live Received Addresses.txt"
mentionsAddressFile = "gib-holders.json"
outfile = "cache/AddressesToSend.json"

tokenaddress = input("Please enter the DAO token address (REQUIRED):")

if (len(tokenaddress) != 44):
    sys.exit('\n !!! Ensure this is a valid token address. They are 44 chars long... !!!\n')

tokensAmountPerNFTInput = input("Enter the AMOUNT of DAO tokens to send per each NFT owned. (Default: 1):")
tokensAmountPerNFT = int(tokensAmountPerNFTInput)
if (tokensAmountPerNFT < 0):
    sys.exit('Amount must be bigger than zero.')
if (tokensAmountPerNFTInput == ""):
    tokensAmountPerNFT = 1
  
print (f"Sending {tokensAmountPerNFT} {tokenaddress} DAO tokens per each NFT held...")

with open(receivedFile, "r") as received:
    lines = received.readlines()

loadedReceived = []
for line in lines:
    loadedReceived.append(line.strip('\n'))

addressesToSend = []

with open(mentionsAddressFile, 'r', encoding='utf8') as jsonfile:
	json_load = json.load(jsonfile)

addresses = 0
for address, value in json_load.items():
    addresses +=1
    if (address not in loadedReceived):
        addressesToSend.append({"address": address, "amount": value['amount']})
print(addresses)

with open(outfile, "w+") as un:
    json.dump(addressesToSend, un)

with open(outfile) as data_file:    
    data = json.load(data_file)
    count = 0
    for x in data:
        amountToSend = x['amount'] * tokensAmountPerNFT
        count += amountToSend
        print (f"{x['address']} --- {amountToSend}")
        # By default, this sends a token and funds creating the token account in the receiving account
        # but does not send the token if the receiving has 0 SOL in their wallet.
        #os.system(f"spl-token transfer --fund-recipient {tokenaddress} {amountToSend} {x['address']}")
        
        # To send tokens and allow for wallets with 0 SOL. Comment out the above and uncomment
        # below:
        # os.system(f"spl-token transfer --fund-recipient --allow-unfunded-recipient {tokenaddress} {amountToSendPerNFT} {x['address']}")
    
    print (count)