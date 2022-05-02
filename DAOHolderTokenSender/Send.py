######################################################################################################
# Title: DAO Token Sender                                                                            #
# Author: Dean Overton                                                                               #
# Github : https://github.com/Dean-Overton                                                           #
######################################################################################################

print (""" 
          ███████╗██████╗  █████╗  ██████╗ 
          ██╔════╝██╔══██╗██╔══██╗██╔═══██╗
          ███████╗██║  ██║███████║██║   ██║
          ╚════██║██║  ██║██╔══██║██║   ██║
          ███████║██████╔╝██║  ██║╚██████╔╝
          ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ 
                                                                                                                                                                                                                                                                                                            
                   Dean Overton
https://github.com/Dean-Overton/solana-discord-nft-tools

""")

from asyncio.windows_events import NULL
from colorama import init, Fore
init()
import os
import json
import sys

receivedFile = "cache/Live Received Addresses.txt"
mentionsAddressFile = "gib-holders.json"
outfile = "cache/AddressesToSend.json"


tokenaddress = input("Please enter the DAO token address (REQUIRED):").lower().strip()

if len(tokenaddress) != 44:
    sys.exit('\n !!! Ensure this is a valid token address. They are 44 chars long... !!!\n')


tokensAmountPerNFTInput = input("Enter the AMOUNT of DAO tokens to send per each NFT owned. (Default: 1):")
print(tokensAmountPerNFTInput)
if tokensAmountPerNFTInput != None:
    amountToSend = int(tokensAmountPerNFTInput)
else:
    tokensAmountPerNFT = 1
tokensAmountPerNFT = int(tokensAmountPerNFTInput)
if (tokensAmountPerNFT < 0):
    sys.exit('Amount must be bigger than zero.')


def askYesNoQuestion(question):
  YesNoAnswer = input(question).lower()
  if YesNoAnswer in ['yes', 'y', 'no', 'n']:
     return YesNoAnswer  
  else:
     return askYesNoQuestion(question)


G  = '\033[32m' # green
R  = '\033[31m' # red
allowUnfundedInput = askYesNoQuestion(f"{Fore.WHITE} Allow addresses with 0 SOL in them (unfunded recipients)? [{Fore.GREEN}y{Fore.WHITE}, {Fore.RED}n{Fore.WHITE}]")
if allowUnfundedInput.lower() in ['yes', 'y']:
    allowUnfunded = True
if allowUnfundedInput.lower() in ['no', 'n']:
    allowUnfunded = False



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
    biggestOwner = ""
    biggestOwnerAmount = 0
    data = json.load(data_file)
    count = 0
    for x in data:
        if (x['amount'] > biggestOwnerAmount):
            biggestOwner = tokenaddress
            biggestOwnerAmount = x['amount']
        amountToSend = x['amount'] * tokensAmountPerNFT
        count += amountToSend
        print (f"{x['address']} --- {amountToSend}")
        if (allowUnfunded):
            os.system(f"spl-token transfer --fund-recipient --allow-unfunded-recipient {tokenaddress} {amountToSend} {x['address']}")
        else:
            os.system(f"spl-token transfer --fund-recipient {tokenaddress} {amountToSend} {x['address']}")
    
    print (f""" 
#################################################

Sent a total of {count} tokens!

BIGGEST OWNER: {biggestOwner} with {biggestOwnerAmount} NFTs and sent {biggestOwnerAmount * tokensAmountPerNFT} tokens!

################################################
""")