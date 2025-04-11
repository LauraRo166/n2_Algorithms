import unittest
from algorithms.allPairs import allPairs

class test_AllPairs(unittest.TestCase):
    def test_basic(self):
        """Should return all pairs correctly."""
        self.assertEqual(allPairs([1, 2]), [(1, 1), (1, 2), (2, 1), (2, 2)])

    def test_empty(self):
        """Should return an empty list for an empty input."""
        self.assertEqual(allPairs([]), [])

    def test_single(self):
        """Should return one pair for a list with one element."""
        self.assertEqual(allPairs([5]), [(5, 5)])