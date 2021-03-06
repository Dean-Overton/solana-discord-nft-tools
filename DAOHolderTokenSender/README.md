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
- By default, wallet addresses with 0 SOL (unfunded recipients) are flagged and not sent.

### Search Current Token Holders 
1) ```python SearchReceivedAddresses.py```
2) Outputs holders addresses to 'cache/Live Received Addresses.txt'
3) To get the owners mentions continue below with ['mentioning holders'](https://github.com/Dean-Overton/solana-discord-nft-tools/tree/main/WhitelistTokenSender/README.md#Mention-Token-Holders)

NOTES: 
- Utilising Solscan public API (5 requests/second)
- These current holders include your own addresses (You may not want to send WL to yourself)!

### Mention Token Holders 
1) ```python MentionHolders.py```
2) Creates 'MentionMessage.txt' message with @usernames list.