import os, json
tabular_dir_path = "CDIACTabularExtracted"
files = []
for file_name in os.listdir(tabular_dir_path):
	key = file_name.split("TabXtract", 1)[0]
	files.append(key)

files = sorted(files)
with open('listOfFiles.txt', 'w+') as f:
	for item in files:
 	       f.write("%s\n" % item)
	f.close()
