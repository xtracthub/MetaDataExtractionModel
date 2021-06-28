import json
import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
import dask.dataframe as dd
#one_gram_df = pd.read_json('one_grams.json')
two_gram_df = dd.read_json('two_grams.json', blocksize=8192)

'''
v1 = DictVectorizer(sparse=False)
v2 = DictVectorizer(sparse=False)

distr_one_gram = v1.fit_transform(one_gram).copy()
distr_two_gram = v2.fit_transform(two_gram).copy()
print('converting')
for i in range(distr_one_gram.shape[0]):
        distr_one_gram[i] = distr_one_gram[i] / (np.sum(distr_one_gram[i]) + np.finfo(float).eps)
for i in range(distr_two_gram.shape[0]):
        distr_two_gram[i] = distr_two_gram[i] / (np.sum(distr_two_gram[i]) + np.finfo(float).eps)
print('converting done!')
distr_one_gram = v1.inverse_transform(distr_one_gram)
distr_two_gram = v2.inverse_transform(distr_two_gram)

with open('distr_one_gram.json', 'w+') as f1:
	json.dump(distr_one_gram, f1, indent=4)
	f1.close()
with open('distr_two_gram.json', 'w+') as f2:
	json.dump(distr_two_gram, f2, indent=4)
	f2.close()
print('saving done!')
'''
