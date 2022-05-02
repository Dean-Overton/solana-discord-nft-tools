from hashlib import blake2b
import json
from operator import add
import os
import sys
import re
from colorama import init, Fore
init()

message_folder_name = 'messages'

def RmNonSolAddressChars (addressWithCrap):
	newAddress = re.sub(r'[\W_]+', '', addressWithCrap)
	return newAddress

def MessagesFolderToArray():
	# To allow for partitioned json files as too long json files cant be read
	messages = []
	for filename in os.listdir(message_folder_name):
		with open(os.path.join(message_folder_name, filename), 'r', encoding='utf8') as f:
			messages.append(json.load(f)['messages'])
	return messages

def WriteCollectedAddresses(dict):
	# Serializing json 
	json_object = json.dumps(dict, indent = 4)

	with open("AllUsernamesAddresses.json", "w") as mentionsFile:
		mentionsFile.write(json_object)

def askYesNoQuestion(question):
  YesNoAnswer = input(f"{Fore.WHITE}{question} [{Fore.GREEN}y{Fore.WHITE}, {Fore.RED}n{Fore.WHITE}]").lower()
  if YesNoAnswer in ['yes', 'y', 'no', 'n']:
     return YesNoAnswer  
  else:
     return askYesNoQuestion(question)

def CheckBlacklist():
	if os.path.exists(os.path.join(os.pardir, 'blacklist.txt')):
		print("\nBlacklist file located in parent directory...\n")
		answer = askYesNoQuestion("Use blacklist.txt?")
		if (answer in ['yes', 'y']):
			return os.path.join(os.pardir, 'blacklist.txt')
		if (answer in ['no', 'n']):
			return False
	else:
		return False

def CreateBlacklistedAddressArray ():
	with open(os.path.exists(os.path.join(os.pardir, 'blacklist.txt')), 'r') as f:
		blacklist = f.readlines
		print (blacklist)
		return blacklist

def MentionAndPrintAddressInfo(message, address):
	mention = f"{message['author']['name']}#{message['author']['discriminator']}"
	print(f"______{mention}______\n{address}\n")
	return mention

def CheckAndPrintSuspectingMentions(data, address, mention):
	if (data == []):
		return False
	for obj in data:
		if (obj['mention'] in data):
			print(f"{mention} sent another address...")
			if (obj['address'] in data):
				print(f"which is already in the database.")
				return True
			else:
				print(f"which is not already in the database. SUSPICIOUS")
				return True
		else:
			if (obj['address'] in data):
				print(f"Address: {obj['address']} being sent again by a DIFFERENT USER {obj['mention']}! HIGHLY SUSPICIOUS")
				return True
			else:
				return False
	return False

def CheckMessageAuthor(message, blacklist):
	if (blacklist):
		if(message['author']['name'] in blacklist):
			return False
		else:
			return True
	else:
		return True

def CheckBlacklistedAddress(address, blacklist):
	if (blacklist):
		if (address not in blacklist):
			return False
		else:
			return True
	else:
		return False

def main():
	scraped_message_files = MessagesFolderToArray()

	blacklist = False
	useBlacklist = CheckBlacklist()
	if (useBlacklist != False):
		blacklist = CreateBlacklistedAddressArray()
	
	data_dic = []
	for x in scraped_message_files:
		for message in x:
			if (CheckMessageAuthor(message, blacklist)):
				words = message['content'].split()
				for word in words:
					filteredWordForAddress = RmNonSolAddressChars(word)
					wordLength = len(filteredWordForAddress)
					if(wordLength == 44):
						if (CheckBlacklistedAddress(filteredWordForAddress, blacklist) == False):
							mention = MentionAndPrintAddressInfo(message, filteredWordForAddress)
							if (CheckAndPrintSuspectingMentions(data_dic, filteredWordForAddress, mention) == False):
								data_dic.append({"mention": mention, "address": filteredWordForAddress})
							
	print (f"Addresses: {len(data_dic)}")

	WriteCollectedAddresses(data_dic)

if __name__ == "__main__":
	main()