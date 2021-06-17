import os, json

"""
First iterate through Image Predictions
"""
img_dir_path = "CDIACImgPredictions"
mega_extract_dict = dict()
for file_name in os.listdir(img_dir_path):
	file_path = os.path.join(img_dir_path, file_name)
	data = open(file_path, 'r')
	data = json.load(data)		# try to conserve some memory here?
	parsed_file_name = file_name.split("ImgXtract", 1)
	file_index_key = parsed_file_name[1].split(".json")[0]
	key = parsed_file_name[0] + "kEy" + file_index_key
	if bool(data):
		mega_extract_dict[key] = ['Img']
	else:
		mega_extract_dict[key] = []

keyword_dir_path = "CDIACKeywordExtract"
for file_name in os.listdir(keyword_dir_path):
	file_path = os.path.join(keyword_dir_path, file_name)
	data = open(file_path, 'r')
	data = json.load(data)
	parsed_file_name = file_name.split("KWXtract", 1)
	file_index_key = parsed_file_name[1].split(".json")[0]
	key = parsed_file_name[0] + "kEy" + file_index_key
	if key not in mega_extract_dict:
		print("Something went wrong. The file key: ", file_name, "does not exist.")
		break
	if bool(data) and "keywords" in data and bool(data["keywords"]):
		mega_extract_dict[key].append("Keyword")

tabular_dir_path = "CDIACTabularExtracted"
for file_name in os.listdir(tabular_dir_path):
	file_path = os.path.join(tabular_dir_path, file_name)
	data = open(file_path, 'r')
	data = json.load(data)
	parsed_file_name = file_name.split("TabXtract", 1)
	file_index_key = parsed_file_name[1].split(".json")[0]
	key = parsed_file_name[0] + "kEy" + file_index_key
	if key not in mega_extract_dict:
		print("Something went wrong (TabXtract). The file key:", file_name, "is not found")
		break
	if bool(data) and "tabular" in data and "error" not in data["tabular"]:
		mega_extract_dict[key].append("Tabular")

with open("best_extractors.json", "w+") as fp:
	json.dump(mega_extract_dict, fp, indent=4)
