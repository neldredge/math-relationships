import unittest

class TestExample(unittest.TestCase):

    def test_tuple_equality(self):
        self.assertEqual((1, 2), (1, 2))

    def test_tuple_inequality(self):
        self.assertNotEqual((1, 2), (2, 2))
