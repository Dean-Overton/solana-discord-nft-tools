# SOLANA Address Token Sender Tool (SAKS)

These simple python based scripts helps to send tokens to SOLANA addresses in a json file as collected in [SASD](https://github.com/Dean-Overton/solana-discord-nft-tools/tree/main/DiscordChannelSolanaAddressScraper) along with creating mention messages who have not received tokens.

## Prerequisites
- Have a 'AllUsernamesAddresses.json' located in this directory: 'WhitelistTokenSender/AllUsernamesAddresses.json'. Structure: [{"mention": "username#2541", "address": "thisisanexampleaddressthatis44characterslong"}]. NOTE: mention values are not required for sending tokens and can be left blank.
- Have python installed.
- Solana CLI tools with wallet that contains SOL hooked up. This will be debited for each whitelist token transfer fee.

## Guide

### ___________ Send.py ___________
1) ```python3 Send.py "thisisanexampleaddressthatis44characterslong" 1``` This will send 1 token of address "thisisanexampleaddressthatis44characterslong" to each owner.

NOTES:
- Allowing for accounts with 0 SOL in their wallet. By default, tokens will NOT send to SOLANA wallet addresses with 0 SOL in their wallet otherwise known as an '-unfunded-recipient'. You will need to open and edit 'Send.py' to change this.

### Search Current Token Holders 
1) ```python SearchReceivedAddresses.py "thisisanexampleaddressthatis44characterslong"```
2) Outputs holders addresses to 'cache/Live Received Addresses.txt'
3) To get the owners mentions continue below with ['mentioning holders'](https://github.com/Dean-Overton/solana-discord-nft-tools/tree/main/WhitelistTokenSender/README.md#Mention-Token-Holders)

NOTES: 
- Utilising Solscan public API (5 requests/second)

### Mention Token Holders 
1) ```python MentionHolders.py```
2) Creates 'MentionMessage.txt' message with @usernames list.