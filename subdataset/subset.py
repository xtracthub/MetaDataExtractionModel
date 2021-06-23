import os, json, pickle, csv, pandas
import numpy as np
from classDeclarations import file_data
from random import sample
MAX_SAMPLE_SIZE = 100

Path = "../../CDIACPub8"

imgs = []
csvs = []
pdfs = []

missing_count = 0
df = pandas.read_csv('../cdiac_naivetruth_processed.csv', index_col='path')
for subdir, dirs, files in os.walk(Path):
    for file_name in files:
        file_path = os.path.abspath(os.path.join(subdir, file_name))
        if df['path'].str.contains(file_name).any():
            if file_path.endswith('.png') or file_path.endswith('.jpg'):
                imgs.append(file_path)
            elif file_path.endswith('.csv') or file_path.endswith('.tsv'):
                csvs.append(file_path)
            elif file_path.endswith('.pdf') or file_path.endswith('.txt'):
                pdfs.append(file_path)
        else:
            missing_count += 1


img_sample_names = sample(imgs, MAX_SAMPLE_SIZE)
csv_sample_names = sample(csvs, MAX_SAMPLE_SIZE)
pdfs_sample_names = sample(pdfs, MAX_SAMPLE_SIZE)

print("loading files now...")
byte_distr = np.load("../byte_prob_distr.npy")
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
        curr_sample = pdfs_sample_names

    for file_name in curr_sample:
        curr_file_data = file_data(file_name, byte_distr[file_name], two_grams_dicts[file_name], df.at[file_name, 'file_label'])
        data_list.append(curr_file_data)
print('Dumping!')

with open('gathered_data_revised.pkl', 'wb+') as handle:
    pickle.dump(dataset, file=handle, protocol=pickle.HIGHEST_PROTOCOL)
print('Dumped.')


