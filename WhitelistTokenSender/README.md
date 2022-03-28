# SOLANA Address Token Sender Tool (SAKS)

These simple python based scripts helps to send tokens to SOLANA addresses in a json file as collected in [SASD](https://github.com/Dean-Overton/solana-discord-nft-tools/tree/main/DiscordChannelSolanaAddressScraper) along with creating mention messages who have not received tokens.

## Prerequisites
- Have a __'AllUsernamesAddresses.json'__ located in this directory: 'WhitelistTokenSender/AllUsernamesAddresses.json'. [^structureofallusernames]
- Have python installed [Install python here](https://www.python.org/downloads/)
- Solana CLI tools with wallet that contains SOL hooked up. This will be debited for each whitelist token transfer fee. [Get started here](https://docs.solana.com/cli/install-solana-cli-tools#windows), create a wallet and other documentation [here](https://docs.solana.com/cli)

## Guide

### Send.py
1) ```python3 Send.py``` and follow the prompts.

NOTES:
- By default, wallet addresses with 0 SOL (unfunded recipients) are flagged and not sent.

### Search Current Token Holders 
1) ```python SearchReceivedAddresses.py``` and follow the prompts.
2) Outputs holders addresses to 'cache/Live Received Addresses.txt'
3) To get the owners mentions continue below with ['mentioning holders'](https://github.com/Dean-Overton/solana-discord-nft-tools/tree/main/WhitelistTokenSender/README.md#Mention-Token-Holders)

NOTES: 
- Slow in-depth search process due to solscan public API request limits [^solscanlimits]
- These current holders include your own addresses!

### Mention Token Holders 
1) ```python MentionHolders.py```
2) Creates 'MentionMessage.txt' message with @usernames list.[^message]

[^structureofallusernames]: __Structure:__ [{"mention": "username#2541", "address": "thisisanexampleaddressthatis44characterslong"} , {"mention": ...}]. <br> __NOTE:__ mention values are not required for sending tokens and can be left blank.
[^solscanlimits]: Solscans public API limits requests to 5 requests/second. Searching the current receivers utilizes their public program which is very popular. May update this in the future to use a custom program for much faster results.
[^message]: This is helpful for creating a message for discord with large amounts of holders that have 0 SOL in their wallet. Many NFT buyers commonly have burner wallets which may mean you want to follow changing to allow sending whitelist to them. [^0sol]
