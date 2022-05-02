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
import sys
from colorama import init, Fore, Back
init()

receivedFile = "cache/Live Received Addresses.txt"
mentionsAddressFile = "AllUsernamesAddresses.json"
outfile = "cache/AddressesToSend.json"

def askYesNoQuestion(question):
  YesNoAnswer = input(question).lower()
  if YesNoAnswer in ['yes', 'y', 'no', 'n']:
     return YesNoAnswer  
  else:
     return askYesNoQuestion(question)

def main():
    tokenAddressInput = input("Please enter the whitelist token address (REQUIRED):")

    if tokenAddressInput == False or len(tokenAddressInput) != 44:
        sys.exit('\n !!! Ensure this is a valid token address. They are 44 chars long... !!!\n')

    tokenaddress = tokenAddressInput.lower().strip()

    amountInput = input("Enter the AMOUNT of whitelist tokens to send to each address (Default: 1):")
    if amountInput:
        amountToSend = int(amountInput)
    else:
        amountToSend = 1
        print("Setting to DEFAULT amount of 1")
    if (amountToSend < 0):
        sys.exit('Amount must be bigger than zero.')

    G  = '\033[32m' # green
    R  = '\033[31m' # red
    allowUnfundedInput = askYesNoQuestion(f"{Fore.WHITE} Allow addresses with 0 SOL in them (unfunded recipients)? [{Fore.GREEN}y{Fore.WHITE}, {Fore.RED}n{Fore.WHITE}]")
    if allowUnfundedInput.lower() in ['yes', 'y']:
        allowUnfunded = True
    if allowUnfundedInput.lower() in ['no', 'n']:
        allowUnfunded = False


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
            if (allowUnfunded):
                os.system(f"spl-token transfer --fund-recipient --allow-unfunded-recipient {tokenaddress} {amountToSend} {x['address']}")
            else:
                os.system(f"spl-token transfer --fund-recipient {tokenaddress} {amountToSend} {x['address']}")

if __name__ == "__main__":
	main()