import json
import numpy as np
from sklearn.feature_extraction import DictVectorizer

one_gram = json.load(open('one_grams.json', 'r'))
two_gram = json.load(open('2_grams.json', 'r'))

v1 = DictVectorizer(sparse=False)
v2 = DictVectorizer(sparse=False)

distr_one_gram = v1.fit_transform(one_gram).copy()
distr_two_gram = v2.fit_transform(two_gram).copy()

for i in range(distr_one_gram.shape[0]):
        distr_one_gram[i] = distr_one_gram[i] / (np.sum(distr_one_gram[i]) + np.finfo(float).eps)
for i in range(distr_two_gram.shape[0]):
        distr_two_gram[i] = distr_two_gram[i] / (np.sum(distr_two_gram[i]) + np.finfo(float).eps)

distr_one_gram = v1.inverse_transform(distr_one_gram)
distr_two_gram = v2.inverse_transform(distr_two_gram)

with open('distr_one_gram.json', 'w+') as f1:
	json.dump(distr_one_gram, f1, indent=4)
	f1.close()
with open('distr_two_gram.json', 'w+') as f2:
	json.dump(distr_two_gram, f2, indent=4)
	f2.close()


