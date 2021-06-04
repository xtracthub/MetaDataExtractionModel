"""

Basic clustering of CDIAC data files from Globus

"""

import matplotlib.pyplot as plt
from collections import Counter
import binascii
import os
from pathlib import Path

file_path = "pagman.txt"
#test file path and experiment with a .tsv file 
# feel free to change because this is my machine specific

f = open(file_path, "rb")
contents = f.read()
c = Counter(contents)

print("Metadata associated with the file: ")

split_tuple = os.path.splitext(file_path)
print("File extension: ", split_tuple[1])
print("File name: ", split_tuple[0])
print("File path: ", os.path.abspath(file_path))
print("File size is: ", os.path.getsize(file_path), "bytes")
print("Parent Directory: ", os.path.dirname(os.path.abspath(file_path)))


print("Here is a list of the 10 most frequent bytes: ")

data = []
values = []

for value, frequency in c.most_common(10):
        data.append(frequency)
        values.append(value)
        print("0x{:02x}: {}".format(value, frequency))

print(data)
plt.hist(data)
plt.xticks(range(len(values)), values, size='small')
plt.show()