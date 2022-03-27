# SOLANA DAO Token Sender Tool (SDAO)

These simple python scripts helps to create a DAO!

## Prerequisites
- Have a 'gib-holders.json' located in this directory: 'DAOHolderTokenSender/'. [Get the file here by entering the mint IDs.](https://pentacle.tools/holder-snapshot)
- Have python installed.
- Solana CLI tools with wallet that contains SOL hooked up. This will be debited for each whitelist token transfer fee.

## Guide

### ___________ Send.py ___________
1) ```python3 Send.py``` and follow the prompts.

NOTES:
- Allowing for accounts with 0 SOL in their wallet. By default, tokens will NOT send to SOLANA wallet addresses with 0 SOL in their wallet otherwise known as an '-unfunded-recipient'. You will need to open and edit 'Send.py' to change this.

### Search Current Token Holders 
1) ```python SearchReceivedAddresses.py```
2) Outputs holders addresses to 'cache/Live Received Addresses.txt'
3) To get the owners mentions continue below with ['mentioning holders'](https://github.com/Dean-Overton/solana-discord-nft-tools/tree/main/WhitelistTokenSender/README.md#Mention-Token-Holders)

NOTES: 
- Utilising Solscan public API (5 requests/second)

### Mention Token Holders 
1) ```python MentionHolders.py```
2) Creates 'MentionMessage.txt' message with @usernames list.