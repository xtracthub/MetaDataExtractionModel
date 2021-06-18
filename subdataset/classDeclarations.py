import numpy as np


class file_data:
	def __init__(self, file_name, one_gram_distr_zero, one_gram_distr_nonzero, two_gram_distr, best_extractors, file_index):
		self.file_name = file_name
		if not isinstance(one_gram_distr_zero, np.ndarray) or not isinstance(one_gram_distr_nonzero, np.ndarray):
			print("Invalid one gram must be ndarray")
		self.one_gram_distr_zero = one_gram_distr_zero
		self.one_gram_distr_nonzero = one_gram_distr_nonzero
		self.two_gram_distr = two_gram_distr
		self.best_extractors = best_extractors
		self.index = file_index