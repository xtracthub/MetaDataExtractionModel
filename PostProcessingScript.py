import json
import time

MAX_BIT_SIZE = 256
two_grams_json = open('2_grams.json', 'r')
two_grams_dict = json.load(two_grams_json)

for key in two_grams_dict:
	file_dict = two_grams_dict[key]
	for i in range(MAX_BIT_SIZE):
		for j in range(MAX_BIT_SIZE):
			key = str(hex(i)) + '-' + str(hex(j))
			if key not in two_grams_dict:
				file_dict[key] = 0

with open('2_grams_PP.json', 'w+') as fp:
    print('Starting dump of 2_grams_PP')
    start = time.time()
    json.dump(two_grams_dict, fp, indent=4, sort_keys=True)
    print("Time taken: ", time.time() - start, "seconds")
    fp.close()
    print("Dump done!")
 
two_grams_json.close()

three_grams_json = open('3_grams.json', 'r')
three_grams_dict = json.load(three_grams_json)

for key in three_grams_dict:
	file_dict = three_grams_dict[key]
	for i in range(MAX_BIT_SIZE):
		for j in range(MAX_BIT_SIZE):
			for k in range(MAX_BIT_SIZE):
				key = str(hex(i)) + '-' + str(hex(j)) + '-' + str(hex(k))
				if key not in three_grams_dict:
					file_dict[key] = 0

with open('3_grams_PP.json', 'w+') as fp:
    print('Dumping 3 grams json')
    start = time.time()
    json.dump(three_grams_dict, fp, indent=4, sort_keys=True)
    print("Time taken: ", time.time() - start, "seconds")
    fp.close()
    print("Dump done!")
  
three_grams_json.close()