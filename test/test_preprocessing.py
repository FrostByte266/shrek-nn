import numpy
import unittest

from src.homophone import *

class TestPreprocessing(unittest.TestCase):

    def test_fuzzy_compare(self):
        check = [check_equal(pair) for pair in get_all_pairs('../data/homophones.csv')]
        self.assertTrue(all(i is True for i in check))
