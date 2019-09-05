import numpy
import unittest

from src.homophone import *

class TestPreprocessing(unittest.TestCase):

    def test_homophones(self):
        evaluation = [True if check_equal(pair) else False for pair in get_all_pairs('../data/homophones.csv')]
        accuracy = (evaluation.count(True)) / len(evaluation)
        print(f'\n{accuracy*100}% accuracy')
