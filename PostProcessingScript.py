import json
import time
import dask.dataframe as dd

MAX_BIT_SIZE = 256
index = 0
two_grams_json_df = dd.read_json('2_grams.json')
for key in two_grams_dict:
	file_dict = two_grams_dict[key]
	for i in range(MAX_BIT_SIZE):
		for j in range(MAX_BIT_SIZE):
			hex_key = hex(i) + '-' + hex(j)
			if hex_key not in file_dict:
				file_dict[hex_key] = 0

	index += 1
	if index % 1000 == 0:
		print("done with a thousand")


with open('2_grams_PP.json', 'w+') as fp:
    print('Dumping 2 grams json')
    start = time.time()
    json.dump(two_grams_dict, fp, indent=4, sort_keys=True)
    print("Time taken: ", time.time() - start, "seconds")
    fp.close()
    print("Dump done!")
  
two_grams_json.close()