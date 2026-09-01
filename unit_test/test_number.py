import unittest

from even_or_odd import is_even


class TestNumber(unittest.TestCase):

    def test_even(self):
        self.assertTrue(is_even(4))

    def test_odd(self):
        self.assertFalse(is_even(7))


if __name__ == "__main__":
    unittest.main()
