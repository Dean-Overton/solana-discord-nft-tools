import json

mentionsAddressFile = "cache/AddressesToSend.json"
mentionsText = "MentionMessage.txt"

with open(mentionsAddressFile, 'r', encoding='utf8') as jsonfile:
	json_load = json.load(jsonfile)

with open (mentionsText, 'w+', encoding='utf8') as new:
    for x in json_load:
        new.write("@")
        new.write(x['mention'] + ", ")