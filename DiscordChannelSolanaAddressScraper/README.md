# SOLANA Address Scraper Discord Tool (SASD)

This simple python based scripts helps to scrape SOLANA addresses into a json file with the owners discord mention included. Helpful for NFT projects that need to create whitelists or mass airdrops.

## Prerequisites
- Have python installed
- Have a discord channel set up where whitelisted roles can send addresses. Preferably message history disabled to avoid addresses being public to everyone.

## Guide
1) Open 'Scrape' shortcut and follow the instructions as given
2) Locate and click on the channel holding all your Solana addresses to be collected.
3) Click download icon. Settings as shown: ![Example Settings: Partition limit = 200. Json format](https://github.com/Dean-Overton/solana-discord-nft-tools.git/DiscordChannelSolanaAddressScraper/Settings.PNG)
4) Export into the 'messages' folder.
5) ```python SASD.py```
6) 'AllUsernamesAddresses.json' contains all SOLANA addresses dropped in that channel!

## NOTE
- This script does not verify they are real solana addresses on the blockchain.
- Using [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter)

