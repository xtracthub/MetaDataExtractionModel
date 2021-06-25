import numpy as np


class file_data:
	def __init__(self, file_path, one_gram_distr, two_gram_distr, best_extractors):
		self.file_path = file_path
		self.one_gram_distr = one_gram_distr
		self.two_gram_distr = two_gram_distr
		self.best_extractors = best_extractors