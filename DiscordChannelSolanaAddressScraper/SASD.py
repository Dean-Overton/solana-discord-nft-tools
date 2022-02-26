import json
import os
import sys
import re

message_folder_name = 'messages'

def RemoveCrap (addressWithCrap):
	newAddress = re.sub(r'[\W_]+', '', addressWithCrap)
	return newAddress

# To allow for partitioned json files as too long json files cant be read
scraped_message_files = []
for filename in os.listdir(message_folder_name):
	with open(os.path.join(message_folder_name, filename), 'r', encoding='utf8') as f: # open in readonly mode
		scraped_message_files.append(json.load(f)['messages'])

data_dic = []
for x in scraped_message_files:
	for message in x:
		if (message['author']['name'] not in ["j0hn_sm1th.sol", "Dannyboy", "MEE6"]):
			words = message['content'].split()
			for word in words:
				filteredCrapWord = RemoveCrap(word)
				wordLength = len(filteredCrapWord)
				if(wordLength == 44):
					mention = f"{message['author']['name']}#{message['author']['discriminator']}"
					print(f"______{mention}______\n{filteredCrapWord}\n")
					if any(obj['mention'] == mention or obj['address'] == filteredCrapWord for obj in data_dic):
						continue
					data_dic.append({"mention": mention, "address": filteredCrapWord})

print (f"Addresses: {len(data_dic)}")
# Serializing json 
json_object = json.dumps(data_dic, indent = 4)

with open("AllUsernamesAddresses.json", "w") as mentionsFile:
    mentionsFile.write(json_object)