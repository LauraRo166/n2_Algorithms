import unittest
from algorithms.selectionSort import selectionSort

class test_SelectionSort(unittest.TestCase):
    def test_sorted(self):
        """Should keep sorted list unchanged."""
        self.assertEqual(selectionSort([1, 2, 3]), [1, 2, 3])

    def test_unsorted(self):
        """Should sort a reversed list."""
        self.assertEqual(selectionSort([3, 2, 1]), [1, 2, 3])

    def test_duplicates(self):
        """Should sort list with duplicate values."""
        self.assertEqual(selectionSort([4, 2, 2, 3]), [2, 2, 3, 4])

    def test_empty(self):
        """Should handle an empty list."""
        self.assertEqual(selectionSort([]), [])

    def test_single(self):
        """Should handle a single-element list."""
        self.assertEqual(selectionSort([5]), [5])



