import numpy as np
import unittest

from src.homophone import *
from src.data_fetching import *
from src.preprocessing import *

class TestPreprocessing(unittest.TestCase):

    def setUp(self):
        self.training_set = make_training_set(pages=1)

    def test_training_set_length(self):
        test = [True if len(item) == 2 else False for item in self.training_set]
        self.assertTrue(all(test))

    def test_training_set_string(self):
        test = [True if type(item[0]) is str else False for item in self.training_set]
        self.assertTrue(all(test))

    def test_training_set_int(self):
        test = [True if type(item[1]) is int else False for item in self.training_set]
        self.assertTrue(all(test))

    def test_padding(self):
        arr = np.array([
            [1, 2, 3],
            [1, 2]
        ])
        arr = add_padding(arr)
        self.assertEqual(len(arr[0]), len(arr[1]))
