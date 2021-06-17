''' 

Disregard this, just to print out what order the files are iterated 
through 

'''
import os 
file_base = "../CDIACPub8"

file_names = []
for subdir, dirs, files in os.walk(file_base):
	for file_name in files:
		filepath = subdir + os.sep + file_name
		file_names.append(filepath)

with open('listOfFiles.txt', 'w+') as f:
	for item in file_names:
 	       f.write("%s\n" % item)
	f.close()