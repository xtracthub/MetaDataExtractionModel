import json
import time

MAX_BIT_SIZE = 256
index = 0
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

	index += 1
	if index % 1000 == 0:
		print("done with a thousand")


with open('3_grams_PP.json', 'w+') as fp:
    print('Dumping 3 grams json')
    start = time.time()
    json.dump(three_grams_dict, fp, indent=4, sort_keys=True)
    print("Time taken: ", time.time() - start, "seconds")
    fp.close()
    print("Dump done!")
  
three_grams_json.close()