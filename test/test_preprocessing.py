import numpy
import unittest

from src.homophone import *
from src.data_fetching import fetch_puns_list
from src.preprocessing import *

class TestPreprocessing(unittest.TestCase):

    def setUp(self):
        self.training_set = make_training_set(pages=1)

    def test_homophones(self):
        evaluation = [True if check_equal(pair) else False for pair in get_all_pairs('../data/homophones.csv')]
        accuracy = (evaluation.count(True)) / len(evaluation)
        print(f'\nHomophone test accuracy: {accuracy*100}%')

    def test_training_set_length(self):
        test = [True if len(item) == 2 else False for item in self.training_set]
        self.assertTrue(all(test))

    def test_training_set_string(self):
        test = [True if type(item[0]) is str else False for item in self.training_set]
        self.assertTrue(all(test))

    def test_training_set_int(self):
        test = [True if type(item[1]) is int else False for item in self.training_set]
        self.assertTrue(all(test))
