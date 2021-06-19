import os, json, pickle
import numpy as np
from classDeclarations import file_data
from random import sample
MAX_SAMPLE_SIZE = 100

Path = "../../CDIACPub8"

file_index = 0
imgs = []
csvs = []
pdfs = []
for subdir, dirs, files in os.walk(Path):
    for file_name in files:
        if file_name.endswith('.png'):
            imgs.append(file_name + 'kEy' + str(file_index))
        elif file_name.endswith('.csv'):
            csvs.append(file_name + 'kEy' + str(file_index))
        elif file_name.endswith('.pdf'):
            pdfs.append(file_name + 'kEy' + str(file_index))

        file_index += 1

img_sample_names = sample(imgs, MAX_SAMPLE_SIZE)
csv_sample_names = sample(csvs, MAX_SAMPLE_SIZE)
pdfs_sample_names = sample(pdfs,MAX_SAMPLE_SIZE)

print("loading files now...")
byte_distr = np.load("../byte_prob_distr.npy")
byte_prob_distr_no_zero = np.load("../byte_prob_distr_no_zero.npy")
two_grams_dicts = json.load(open("../2_grams_PP.json"))
best_extractors = json.load(open("../CorrelatingExtractors/best_extractors.json"))
print("loading files done!")

img_data = []
csv_data = []
pdf_data = []
dataset = [img_data, csv_data, pdf_data]
for idx, data_list in enumerate(dataset):
    curr_sample = []
    if idx == 0:
        curr_sample = img_sample_names
    elif idx == 1:
        curr_sample = csv_sample_names
    else:
        curr_sample = pdf_data

    for i in range(MAX_SAMPLE_SIZE):
        parsed_name = curr_sample[i].split("kEy")
        file_name = parsed_name[0]
        file_index = parsed_name[1]
        curr_file_data = file_data(file_name, byte_distr[file_index], \
            byte_prob_distr_no_zero[file_index], \
            two_grams_dicts[curr_sample[i]], best_extractors[curr_sample[i]])
        data_list.append(curr_file_data)
print('Dumping!')
with open('gathered_data.pkl', 'wb+') as handle:
    pickle.dump(data_list, protocol=pickle.HIGHEST_PROTOCOL)
print('Dumped.')


