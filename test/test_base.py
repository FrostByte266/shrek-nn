import unittest
from unittest import mock
from src.data_fetching import fetch_puns_list
import requests

class TestNetwork(unittest.TestCase):

    @mock.patch('requests.get')
    def test_data_fetching_not_found(self, mocked_get):
        type(mocked_get.return_value).status_code = mock.PropertyMock(return_value=404)
        with self.assertRaises(RuntimeError):
            fetch_puns_list(1)

    def test_data_fetching_ok(self):
        self.assertNotEqual(fetch_puns_list(1), 0)
