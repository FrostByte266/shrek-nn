import unittest

class TestNetwork(unittest.TestCase):
    def test_always_true(self):
        self.assertTrue(True)

    def test_always_fail(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
