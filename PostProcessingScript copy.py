import json


MAX_BIT_SIZE = 256
two_grams_json = open('test.json', 'r')
two_grams_dict = json.load(two_grams_json)

for key in two_grams_dict:
	for i in range(MAX_BIT_SIZE):
		for j in range(MAX_BIT_SIZE):
			key = str(hex(i)) + '-' + str(hex(j))
			if key not in two_grams_dict:
				two_grams_dict[key] = 0

with open('testPP.json', 'w+') as fp:
    print('Starting dump...')
    json.dump(two_grams_dict, fp, indent=4, sort_keys=True)
    fp.close()
    print("Dump done!")