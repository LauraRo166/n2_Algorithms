import unittest
from algorithms.hasDuplicates import hasDuplicates

class test_HasDuplicates(unittest.TestCase):
    def test_no_duplicates(self):
        """Should return False for a list with unique elements."""
        self.assertFalse(hasDuplicates([1, 2, 3, 4]))

    def test_with_duplicates(self):
        """Should return True for a list with repeated elements."""
        self.assertTrue(hasDuplicates([1, 2, 3, 2]))

    def test_empty(self):
        """Should return False for an empty list."""
        self.assertFalse(hasDuplicates([]))

    def test_single(self):
        """Should return False for a list with one element."""
        self.assertFalse(hasDuplicates([99]))

