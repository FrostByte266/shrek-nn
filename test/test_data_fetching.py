import unittest
from unittest import mock
import requests
import sys 

sys.path.append('/src/')
from src.data_fetching import fetch_puns_list


class TestExampleFetching(unittest.TestCase):

    def setUp(self):
        self.puns = fetch_puns_list(1)

    @mock.patch('requests.get')
    def test_data_fetching_not_found(self, mocked_get):
        type(mocked_get.return_value).status_code = mock.PropertyMock(return_value=404)
        with self.assertRaises(RuntimeError):
            fetch_puns_list(1)

    def test_data_fetching_ok(self):
        self.assertNotEqual(len(self.puns), 0)

    def test_no_none_in_fetch(self):
        self.assertNotIn(None, self.puns)
